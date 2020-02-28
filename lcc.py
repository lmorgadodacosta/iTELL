#!/usr/bin/env python3

import os, sys, re
from os import path
from flask import Flask, current_app
from flask import render_template, g, request, redirect, url_for, send_from_directory, session, flash
import requests
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from functools import wraps
from common_login import *

from itsdangerous import URLSafeTimedSerializer # for safe session cookies

from werkzeug.utils import secure_filename
import datetime


import mammoth # to parse the docx into html
import lxml.html # to manipulate the html 

import nltk
from nltk import tokenize
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.stem import WordNetLemmatizer

import delphin_call
from feedback import eng_feedback

import lcc_data
import common_sql as csql


################################################################################
# Spelling checker (pip install pyspellchecker)
################################################################################
from spellchecker import SpellChecker
spell = SpellChecker()
# To make sure some words are not flagged as misspelled

new_words = []
for c in " '":
    for w in lcc_data.contractions | lcc_data.wordcase:
        new_words = new_words + w.split(c)
        
spell.word_frequency.load_words(new_words)

################################################################################

from collections import defaultdict as dd
def inf_dd():
    return dd(inf_dd)


UPLOAD_FOLDER = 'lcc_uploads'
ALLOWED_EXTENSIONS = set(['docx'])
ROOT  = path.dirname(path.realpath(__file__))    

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



################################################################################
# This helps achieve better sentence segmentation
################################################################################
extra_abbreviations = ['dr', 'vs', 'mr', 'mrs', 'prof', 'inc', 'i.e', 'e.g',
                       'pte', 'et', 'al', 'et. al', 'fig', 'mfg']
sentence_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
sentence_tokenizer._params.abbrev_types.update(extra_abbreviations)
################################################################################

def remove_nested_parens(input_str):
    """
    Returns a copy of 'input_str' with any parenthesized (..) [..] text removed.
    Nested parentheses are handled. It also returns a Boolean asserting if
    the parenthesis were well balanced (True) or not (False).
    """
    result1 = ''
    paren_level = 0
    for ch in input_str:
        if ch == '(':
            paren_level += 1
        elif (ch == ')') and paren_level:
            paren_level -= 1
        elif not paren_level:
            result1 += ch
    result2 = ''
    paren_level2 = 0
    for ch in result1:
        if ch == '[':
            paren_level2 += 1
        elif (ch == ']') and paren_level2:
            paren_level2 -= 1
        elif not paren_level2:
            result2 += ch

    if (paren_level==0) and (paren_level2==0):
        balanced = True
    else:
        balanced = False
    return (balanced, result2)


with app.app_context():

    
    def allowed_file(filename):
        return '.' in filename and \
               filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


    def uploadFile(current_user):

        format = "%Y_%b%d_%H:%M:%S"
        now = datetime.datetime.now().strftime(format)

        try:
            file = request.files['file']
            lic = request.form['license']
        except:
            file = None
            lic = None


        if file and lic and allowed_file(file.filename):

            if lic == '1':
                lic_txt = 'CC0'
            else:
                lic_txt = 'PRIVATE'
            
            ####################################################################
            # While trying to simplify anonymization, we don't keep the file
            # name. Instead, we keep a normalized username reference that can
            # be anonymized easily.
            ####################################################################            
            f_ext = '.' + file.filename.rsplit('.', 1)[1] # .docx
            filename = lic_txt + '_' + now + '_' +str(current_user) + f_ext 
            filename = secure_filename(filename)
            file.save(os.path.join(ROOT, app.config['UPLOAD_FOLDER'], filename))
            file_uploaded = True

        else:
            filename = False
            file_uploaded = False

        return file_uploaded, filename




    def docx2html(docname):
        """
        This function reads the uploaded file using mammoth and converts it to HTML.
        An artificial documentRoot is added to make it XML compatible.
        """
        with open(os.path.join(ROOT,
                               app.config['UPLOAD_FOLDER'],
                               docname), 'rb') as docx_file:


            result = mammoth.convert_to_html(docx_file)
            docx_html = result.value
            docx_html = docx_html.replace(u'\xa0', ' ') # replacing non-breaking with a space
            docx_html = docx_html.replace("\'", "’")
            docx_html = docx_html.replace('\t', "<tab/> ")
            docx_html = "<documentRoot>" + docx_html + "</documentRoot>"

            return(docx_html)

    def parse_docx_html(html, filename):
        """
        This function gives some structure to the HTML, including <span> tags for 
        each sentence that will be checked and writes them to the database.
        There is also a heavy selection of what sentences should be checked.
        E.g. Sentences after a section named "References" will not be checked.
        """

        ########################################################################
        # Insert DOCUMENT, with html into db.  
        ########################################################################
        docid = csql.fetch_max_doc_id() + 1
        csql.insert_into_doc(docid, filename)
        csql.update_html_into_doc(docid, html)
        
        ########################################################################
        # In order to allow multiple documents to be uploaded at the same time,
        # sids are limited to 100,000 per document, and the sids are given in
        # relation to the docid.  #FIXME: this must be ensured elsewhere
        ########################################################################
        sid = docid * 100000
        max_sid = sid + 99999
        
        
        report = inf_dd()
        REFERENCES = False
        root = lxml.html.fromstring(html)
        for element in root:

            EXCLUDE = False
            
            element_type = element.tag # p, ol, li, table, etc.
            element_text = element.text_content().strip()
            # element_text also includes the text of every children

            # print("\n\n") #TEST
            # print(element_type) #TEST
            # print(element.text_content()) #TEST
            # for subElement in element.getchildren(): #TEST
            #     print(subElement.tag) #TEST

            

            ####################################################################
            # Recuperate bolded paragraphs (likely section titles)
            ####################################################################
            BOLD = False
            if (element.text == None) and (len(element.getchildren())==1):
                if (element[0].tag == "strong"):
                    # We assume the whole element is bold
                    BOLD = True


            ####################################################################
            # Check for very specific keywords to exclude element.
            # There should not be many of these!  
            ####################################################################
            for s in lcc_data.exclude_sents_containing:
                if s in element_text:
                    EXCLUDE = True
                    
            ####################################################################
            # Check for sections (i.e. no punctuation, few words)
            # Includes special case for 'References' in numbered sections
            # All sentneces after 'References' are ignored.
            ####################################################################
            if (element_text) and\
               (element_text[-1] not in lcc_data.punctuation) and\
               (len(element_text.split())<5):
                EXCLUDE = True

                # References
                for w in lcc_data.refs_section:
                    if w in element_text.lower() and\
                       (not element_text[-1].isdigit()): # for TOCs
                        REFERENCES = True
                
            elif (element_text.lower() in lcc_data.exclude_sents):
                EXCLUDE = True

                if element_text.lower() in lcc_data.refs_section:
                    # this is necessary for the cases where punctuation
                    # is used at the end of the section (e.g. ':')
                    REFERENCES = True
                    

            ####################################################################
            # Check for tabs (\t), i.e. "quasi-tables"
            # - this excludes tabs at the beggining of a line (happens often) 
            ####################################################################
            if (element_text):
                for subElement in element.getchildren():
                    if subElement.tag == "tab": 
                        EXCLUDE = True
                
            ####################################################################
            # Check for special sentence starts (e.g. from mandatory cover page)
            ####################################################################
            if (element_text) and\
               element_text.lower().startswith(
                   tuple(lcc_data.exclude_sents_swith)):
                EXCLUDE = True

            ####################################################################
            # Check for some titles and names 
            # - camel-case or ALLCAPS with no punctuation 
            ####################################################################
            if (element_text) and\
               (element_text[-1] not in lcc_data.punctuation):
                
                if element_text.title() == element_text:
                    EXCLUDE = True
                if element_text.upper() == element_text:
                    EXCLUDE = True                    
                    
            ####################################################################
            # Check for figure/table legends (e.g. "Fig" with no punctuation)
            ####################################################################
            if (element_text) and\
               (element_text[-1] not in lcc_data.punctuation) and\
               element_text.lower().startswith(
                   ('fig.', 'figure', '(fig.', '(figure', 'fig:',
                    'image', 'img.',
                    'table', 'tab.')):
                EXCLUDE = True

                #FIXME, this is currently not catching, e.g., "Fig1:"                

            ####################################################################
            # Check if lines are just aesthetic ===== ----- ...... _____
            ####################################################################
            line_separators = '.=-_'
            if (element_text):
                for c in line_separators:
                    if element_text.strip().strip(c) == '':
                        EXCLUDE = True

            ####################################################################
            # Check if lines should be a table:
            # X = 80;  X - 120$;  X : 1000USD
            ####################################################################
            semi_table_separators = '=-:–$'
            if (element_text) and\
               (len(element_text.split())<15) and\
               (element_text[-1] not in lcc_data.punctuation):
                for c in semi_table_separators:
                    if c in element_text:
                        EXCLUDE = True
                        
            
                
                
            ####################################################################
            # Split each paragraph into sentences
            ####################################################################
            sents = []
            if (element_type not in ['table','ol','ul']) and\
               (REFERENCES == False) and\
               (EXCLUDE == False):
                
                for sent in tokenize.sent_tokenize(element_text):
                    sents.append(sent)


            if sents:

                ################################################################
                # We want to clean the element (from text and sub-elements) as #
                # we will reconstruct it from the sentences.                   #
                # This could be improved, to maintain some of the styles, but  #
                # it currently optimises for practicallity.                    #
                ################################################################
                element.text = None                                            #
                for subelement in element:                                     #
                    element.remove(subelement)                                 #
                ################################################################

                
                for sent in sents:
                    sent = sent.strip()
                    sid += 1
                    
                    if BOLD:
                        metaSection = lxml.html.etree.SubElement(element, "strong")
                    else:
                        metaSection = element
                        
                    
                    if sent:
                        sentSpan = lxml.html.etree.SubElement(metaSection, "span")
                        sentSpan.set('id', 'sid{}'.format(sid))
                        # sentSpan.set('class', 'sid{} doccheck'.format(sid)) #TEST
                        
                        # sentSpan.set('data-toggle', 'tooltip')
                        # sentSpan.set('data-placement', 'bottom')
                        # sentSpan.set('data-html', 'true')
                        # sentSpan.set('title', """<em>Lorem ipsum dolor sit amet.</em>""")
                        sentSpan.text = sent

                        
                        #TEST Sentence Boundaries
                        # sentSpan = lxml.html.etree.SubElement(metaSection, "br") #TEST
                        # sentSpan = lxml.html.etree.SubElement(metaSection, "br") #TEST
                    else:
                        sentSpan = lxml.html.etree.SubElement(metaSection, "br")
                        


                    ############################################################
                    # Preprocess sentences before writing them to the db.
                    # We don't want to include certain kinds of sentences, that
                    # are not worth checking; we also want to remore parenthetic 
                    # remarks (because they are usually references) and just
                    # break ERG.
                    ############################################################
                    if ('(' in sent) or ('[' in sent):

                        ########################################################
                        # FIXME: There is a known problem in cases where the 
                        # IEEE references are used as part of the text, e.g.:
                        # As can be seen in [3], this is a problem.
                        ########################################################
                        (balanced, noparen_sent) = remove_nested_parens(sent)
                        noparen_sent = noparen_sent.strip()

                        if (',,' in noparen_sent) and (',,' not in sent):
                            while (',,' in noparen_sent):
                                noparen_sent = noparen_sent.replace(',,',',')

                        if (', ,' in noparen_sent) and (', ,' not in sent):
                            while (', ,' in noparen_sent):
                                noparen_sent = noparen_sent.replace(', ,',',')

                        if (',.' in noparen_sent) and (',.' not in sent):
                            while (',.' in noparen_sent):
                                noparen_sent = noparen_sent.replace(',.','.')

                        if (' .' in noparen_sent) and (' .' not in sent):
                            while (' .' in noparen_sent):
                                noparen_sent = noparen_sent.replace(' .','.')

                        if (' ,' in noparen_sent) and (' ,' not in sent):
                            while (' ,' in noparen_sent):
                                noparen_sent = noparen_sent.replace(' ,',',')

                        if ('  ' in noparen_sent) and ('  ' not in sent):
                            while ('  ' in noparen_sent):
                                noparen_sent = noparen_sent.replace('  ',' ')

                        noparen_sent = noparen_sent.strip('. ')
                        

                        if balanced:
                            sent = noparen_sent
                            #FIXME ELSE should be registered as an error 



                    ############################################################
                    # FIXME: Quotes "ABC DEF" could be handled in a was similar
                    # to parenthesis. They could be changed into something
                    # without spaces.
                    ############################################################

                            
                    ############################################################
                    # This strips the beginning of sentences that are
                    # being enumerated. This is often not well handled by ERG   
                    ############################################################
                    enumeration_starters = [
                        '1.','2.','3.','4.','5.','6.','7.','8.',
                        '9.','10.','11.','12.','13.','14.','15.',
                        '16.','17.','18.','19.','20.',

                        '1)','2)','3)','4)','5)','6)','7)','8)',
                        '9)','10)','11)','12)','13)','14)','15)',
                        '16)','17)','18)','19)','20)',
                        
                        'A.','B.','C.','D.','E.','F.','G.','H.',
                        'I.','J.','K.','M.','N.','O.','P.','Q.',
                        'R.','S.','T.','U.','V.','W.','X.','Y.','Z.',

                        'a)','b)','c)','d)','e)','f)','g)','h)',
                        'i)','j)','k)','m)','n)', 'o)','p)','q)',
                        'r)','s)','t)','u)','v)','w)','x)','y)','z)'
                    ]
                    if (sent[:2] in enumeration_starters):
                        sent = sent[2:].lstrip()




                    ############################################################
                    # If, after all the exceptions are implemented, the value
                    # of sent is not empty, then insert it into the db.
                    ############################################################
                    if sent and (sid < max_sid):
                        pid = 0 # we are ignoring paragraph IDs
                        # print(sid, docid, pid, sent) #TEST
                        csql.insert_into_sent(sid, docid, pid, sent)

                        # INSERT INTO WORD TABLE
                        word_list = pos_lemma(sent2words(sent))
                        # e.g. [('He', 'PRP', 'he'), ('runs', 'VB', 'run')]

                        for w in word_list:
                            wid = csql.fetch_max_wid(sid) + 1
                            (surface, pos, lemma) = w
                            csql.insert_into_word(sid, wid, surface, pos, lemma)

                        
        return(docid, root, report)

    
    def sent2words(sent):
        """Given a sentence string, get a list of (word,pos) elements."""
        return pos_tag(word_tokenize(sent))


    def pos_converter(lemma, pos):
        """
        This converts POS tags into wordnet tags, to be used in lemmatization step.
        FIXME I'm not sure why we are using the this lemmatizer.
        """
        if pos in ['CD', 'NN', 'NNS', 'NNP', 'NNPS', 'WP', 'PRP']: 
                # include proper nouns and pronouns
                ## fixme flag for proper nouns
            return 'n'
        elif pos.startswith('V'):
            return('v')
        elif pos.startswith('J') or pos in ['WDT',  'WP$', 'PRP$', 'PDT', 'PRP'] or \
                    (pos=='DT' and not lemma in ['a', 'an', 'the']):  ### most determiners
            return('a')
        elif pos.startswith('RB') or pos == 'WRB':
            return('r')
        else:
            return 'x'

    def pos_lemma(tagged_sent):
        # Lemmatize = lru_cache(maxsize=5000)(wnl.lemmatize)
        wnl = WordNetLemmatizer()
        lemmatize = wnl.lemmatize

        
        record_list = []
        wid = 0
        for word, pos in tagged_sent:
            lemma = word
            if wid == 0:
                lemma = lemma.lower()
                wid = 1
            wn_pos = pos_converter(lemma, pos)
            if wn_pos in "avnr":
                lemma = lemmatize(lemma, wn_pos)
            record_list.append((word, pos, lemma))
        return record_list



    def check_docx_html(docid, htmlRoot, report, feedback_set):
        """
        This function receives the docID,  HTML element, and Report dictionary
        and checks each sentences with the ERG and other NLP checks.
        It then adds these errors and feedback messages directly on the HTML.
        The sentences stored in the DB have been edited (e.g. removed 
        parenthetic comments, references, etc.) but the sids will match the 
        HTML span IDs.
        """

        ########################################################################
        # Fetch sents and words from the database
        ########################################################################
        sents = csql.fetch_sents_by_docid(docid)
        sid_min = min(sents.keys())
        sid_max = max(sents.keys())
        words = csql.fetch_words_by_sid(sid_min, sid_max)


        for sid in sents:

            sent_text = sents[sid]
            sent_words = words[sid]
            (app_errors, non_app_errors) = full_check_sent(sent_text,
                                                           sent_words,
                                                           feedback_set)


            # print(sents[sid]) #TEST
            # print("lcc_errors") #TEST
            # print(app_errors) #TEST
            # print("non_lcc_errors") #TEST
            # print(non_app_errors) #TEST
            # print('\n\n') #TEST



            ####################################################################
            # ADD ERRORS TO HTML
            ####################################################################
            sentSpan = htmlRoot.get_element_by_id('sid'+str(sid))

            if app_errors:
                feedback_msg = ''
                feedback_conf = 0
                for i, (label, loc) in enumerate(app_errors):
                    msg = eng_feedback[label][feedback_set][0]
                    conf = eng_feedback[label][feedback_set][1]

                    if conf > feedback_conf:
                        feedback_conf = conf
                        
                    if i > 0:
                        feedback_msg +='<br><br>'

                    feedback_msg += msg.format(loc)

                if feedback_conf > 0.51:
                    sentSpan.set('class', 'seriouserror'.format(sid))
                else:
                    sentSpan.set('class', 'milderror'.format(sid))
                    
                sentSpan.set('data-toggle', 'tooltip')
                sentSpan.set('data-placement', 'bottom')
                sentSpan.set('data-trigger', 'click')
                sentSpan.set('data-html', 'true')
                sentSpan.set('container', 'validation_div')
                sentSpan.set('title', feedback_msg)


            ####################################################################
            # WRITE ERRORS TO CORPUS DB
            ####################################################################
            all_errors = app_errors | non_app_errors
            for i, (label, loc) in enumerate(all_errors):
                csql.insert_into_error(sid, i, label, loc)
            
            
        return(htmlRoot, report)



    def NLP_checks_sent(sent, words):
        """
        Given a list of sentences, it checks each of them for multiple problems. 
        """
        errors = [] # take the form (ErrorLabel, StringSurroundingError)
        ########################################################################
        # Check Sentence Length
        ########################################################################
        seriousthreshold = 50
        mildthreshold = 40            
        sentlen = len(list(words.keys()))
        if sentlen >= seriousthreshold:
            errors.append(("VeryLongSentence", '')) 
        elif sentlen >= mildthreshold:
            errors.append(("LongSentence", ''))

            
        ########################################################################
        # Check Contractions
        ########################################################################
        for c in lcc_data.contractions:
            if re.search(r'\b{}\b'.format(c), sent, re.IGNORECASE):
                errors.append(("Contraction", c))


        ########################################################################
        # Check Wordcase
        ########################################################################
        for exp in lcc_data.wordcase:
            # we were getting lots of url matches with word boundary;
            # check for space before and beginning of sentence 
            if re.search(r' {}\b'.format(exp), sent, re.IGNORECASE) and\
               (re.search(r'\b{}\b'.format(exp), sent, re.IGNORECASE).group() != exp):
                errors.append(("WordCase", exp))

            if re.search(r'${}\b'.format(exp), sent, re.IGNORECASE) and\
               (re.search(r'\b{}\b'.format(exp), sent, re.IGNORECASE).group() != exp):
                errors.append(("WordCase", exp))

            #FIXME, Ntu at the beginning of a sentence is not being picked up
                

        ########################################################################
        # Check Phrase Choice
        ########################################################################
        for exp in lcc_data.wordchoice:
            if re.search(r'\b{}\b'.format(exp), sent, re.IGNORECASE):
                errors.append(("WordChoice", exp))
            if re.search(r'${}\b'.format(exp), sent, re.IGNORECASE):
                errors.append(("WordChoice", exp))



        ########################################################################
        # Check Spelling
        ########################################################################
        for c in lcc_data.punctuation:
            sent = sent.replace(c," ")

        for word in sent.split():
            # ignore uppercased words or numerical (e.g. 130kg)
            if (not word[0].isupper()) and (not word[0].isnumeric()): 
                misspelled = spell.unknown([word])
                if misspelled:
                    suggestion = spell.correction(word)
                    errors.append(("Spelling", word+'|'+suggestion))

                

        ########################################################################
        # WORD LEVEL CHECKS
        ########################################################################
        for wid in words.keys():

            lemma = words[wid][2].lower()            
            word_truecase = words[wid][0]
            word = words[wid][0].lower()

            ####################################################################
            # Check Repeated Words 
            ####################################################################
            if (wid+1 in words) and (words[wid+1][0].lower() == word):
                exp = word_truecase + ' ' + word_truecase
                errors.append(("RepeatedWord", exp))

            ####################################################################
            # Check Word Style (e.g. Formal, Pronouns, etc.)
            ####################################################################
            for error_label in lcc_data.wordcheck:
                if lemma in lcc_data.wordcheck[error_label]:
                    errors.append((error_label, word_truecase))

                    
        return errors



    def full_check_sent(sent, words, feedback_set):
        """
        Feedback set refers to which set of errors and error messages are 
        being taken by the app. 'lcc' was the original error set and 
        feedback messages. But 'callig' is another possible value; 
        We're currently working on 'lcc2'; 
        """
        
        nlp_errors = NLP_checks_sent(sent, words)

        LongSentenceSkip = False
        for e in nlp_errors:
            error_label = e[0]
            string_location = e[1]

            if error_label in ["LongSentence","VeryLongSentence"]:
                LongSentenceSkip = True

        if not LongSentenceSkip: # Don't parse long sentences
            erg_errors = delphin_call.check_sents([sent])[0][1]
        else:
            erg_errors= []

        app_errors = set()
        non_app_errors = set()
        for e in nlp_errors + erg_errors:
            label = e[0]
            if label in eng_feedback.keys():
                if feedback_set in eng_feedback[label].keys():
                    app_errors.add(e)
                else:
                    non_app_errors.add(e)
            else:
                non_app_errors.add(e)

        return (app_errors, non_app_errors)
