#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import datetime
import random
import string
import json
from flask import Flask, render_template, g, request, redirect, url_for, send_from_directory, session, flash, jsonify, make_response, Markup
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from flask_mail import Mail, Message
from functools import wraps
from itsdangerous import URLSafeTimedSerializer # for safe session cookies
from collections import defaultdict as dd
from hashlib import md5
from werkzeug.utils import secure_filename


import lxml.html # to manipulate html 

from common_login import *
from common_sql import *

import lcc
import wn
import utils
import syl
import game_data
import delphin_call
import common_sql as csql
from feedback import eng_feedback


def inf_dd():
    return dd(inf_dd)


app = Flask(__name__)
# app.debug = True
app.secret_key = "!$flhgSgngNO%$#SOET!$!"
app.config["REMEMBER_COOKIE_DURATION"] = datetime.timedelta(minutes=30)

ROOT = path.dirname(path.realpath(__file__))


###############################################################################
# MODE defines which apps are available in the deployed instance              #
#                                                                             #
# 'test' MODE is used to hide incomplete applications                         #
#  The other modes include: 'lcc', 'ixue', 'callig'                           #
###############################################################################
MODE = ['lcc', 'ixue', 'callig', 'grammarium', 'test']


###############################################################################
# ALLGRAMMARS defines all available grammars that the system should look for. #
# AVAILABLE_GRAMMARS is a subset of ALLGRAMMARS organized by language, if they#
# are found compiled under appName/delphin/*                                  #
###############################################################################
AVAILABLE_GRAMMARS = dd(lambda: list())
ALLGRAMMARS = [
    ('erg2018.dat', 'eng'),
    ('mal-erg2018.dat', 'eng'),
    ('itell-erg2018.dat', 'eng'),
    ('erg_trunk.dat','eng'),
    ('mal-erg_trunk.dat','eng'),
    
    ('zhong.dat','cmn'),
    ('itell-zhong.dat','cmn'),
    
    ('jacy.dat','jpn'),
    
    ('indra.dat','ind')
]

for (grm, lang) in ALLGRAMMARS:
    if os.path.exists(path.join(ROOT,'delphin/'+grm)):
        AVAILABLE_GRAMMARS[lang].append(grm)
################################################################################


app.config.update(
    # When using gmail, we need to allow unsafe apps to use the email.
    # check: https://pythonprogramming.net/flask-email-tutorial/
    
    DEBUG=False, 
    #EMAIL SETTINGS
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME = 'openwns@gmail.com',
    MAIL_PASSWORD = 'changeme'
)


mail = Mail(app)

################################################################################
# LOGIN
################################################################################
login_manager.init_app(app)

def randomPassword(stringLength=10):
    """
    Generate a random string of letters and digits. 
    This is being used to generate random passwords.
    """
    letters_nums = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_nums) for i in range(stringLength))

@app.route("/login", methods=["GET", "POST"])
def login():
    """
    This login function checks if the username & password
    match the admin.db; if the authentication is successful,
    it passes the id of the user into login_user().
    """

    if request.method == "POST" and \
       "username" in request.form and \
       "password" in request.form:
        username = request.form["username"]
        password = request.form["password"]

        user = User.get(username)

        # If we found a user based on username then compare that the submitted
        # password matches the password in the database. The password is stored
        # is a slated hash format, so you must hash the password before comparing it.
        if user and hash_pass(password) == user.password:
            login_user(user, remember=True)
            # FIXME! Get this to work properly...
            # return redirect(request.args.get("next") or url_for("index"))
            return redirect(url_for("index"))
        else:
            flash(u"Invalid username, please try again.")
    return render_template("login.html",
                           MODE=MODE)

@app.route("/logout")
@login_required(role=0, group='open')
def logout():
    logout_user()
    return redirect(url_for("index"))
################################################################################



################################################################################
# SET UP CONNECTION WITH DATABASES
################################################################################
@app.before_request
def before_request():
    g.admin = connect_admin()
    g.callig = connect_callig()
    g.lcc = connect_lcc()

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.admin.close()
        g.callig.close()
        g.lcc.close()
################################################################################



################################################################################
# GENERAL FUNCTIONS
################################################################################
def current_time():
    '''   YYYY-MM-DD  HH:MM    '''
    d = datetime.datetime.now()
    return d.strftime('%Y-%m-%d %H:%M:%S')
################################################################################


################################################################################
# AJAX REQUESTS
################################################################################

@app.route('/_lccReport', methods=['GET', 'POST'])
@login_required(role=0, group='open')
def lccReport():
    """
    This function produces the HTML report for any given document.

    The feedback_set sets which group of errors and which feedback
    messages to show students. Originally, this was set to 'lcc'.
    But with the current addition of new sets of errors and new error
    messages, this is now a mandatory option for check_docx.
    """

    filename = request.args.get('fn', None)

    # feedback_set = 'lcc'  # original error-set and messages
    feedback_set = 'lcc2'
    docx_html = lcc.docx2html(filename)
    (docid, htmlElem, report) = lcc.parse_docx_html(docx_html, filename)

    (htmlElem, report) = lcc.check_docx_html(docid,
                                             htmlElem,
                                             report,
                                             feedback_set)

    # lxml.html.tostring returns type=bytes, must decode here
    structured_html = lxml.html.tostring(htmlElem).decode('utf-8')
    return jsonify(result=structured_html)




################################################################################
# STATIC VIEWS
################################################################################
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('welcome.html',
                           MODE=MODE)


@app.route('/team', methods=['GET', 'POST'])
def team():
    return render_template('team.html',
                           MODE=MODE)


@app.route('/callig', methods=['GET', 'POST'])
def callig_intro():
    return render_template('callig_intro.html',
                           MODE=MODE)


@app.route('/lcc', methods=['GET', 'POST'])
def lcc_intro():
    return render_template('lcc_intro.html',
                           MODE=MODE)


@app.route('/ixue', methods=['GET', 'POST'])
def ixue_intro():
    return render_template('ixue_intro.html',
                           MODE=MODE)


@app.route('/introduction', methods=['GET', 'POST'])
def itell_intro():
    return render_template('itell_intro.html',
                           MODE=MODE)


###############################################################################
# ADMIN VIEWS
###############################################################################

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html',
                           MODE=MODE)


@app.route("/useradmin", methods=["GET"])
@login_required(role=0, group='admin')
def useradmin():
    users = fetch_allusers()
    return render_template("useradmin.html",
                           users=users,
                           MODE=MODE)


###############################################################################
# GAMES VIEWS
###############################################################################
@app.route('/info/sex-with-me', methods=['GET', 'POST'])
@login_required(role=0, group='open')
def sexwithme_info():

    base_ex = [(0, "Sex with me is like a mountain... it will make you want to get on top.", "The CALLIG System", "Unknown date", "0 seconds")]

    example_list = []
    exs = fetch_sexwithme_30()
    for i, ex_id in enumerate(exs.keys()):
        r = exs[ex_id]
        prompt = r[0]
        answer = r[1]
        seconds = str(r[2]) + ' ' + 'seconds'
        language = r[3]
        username = r[4]
        timestamp = r[5].split()[0]

        example_list.append((i, prompt + '... ' + answer,
                             username, timestamp, seconds))

    if example_list:
        return render_template('sexwithme-info.html',
                               example_list=example_list,
                               MODE=MODE)

    else:  # for brand-new dbs, show a system's example
        return render_template('sexwithme-info.html',
                               example_list=base_ex,
                               MODE=MODE)


@app.route('/games/sex-with-me', methods=['GET', 'POST'])
@login_required(role=0, group='open')
def sexwithme_game():

        
    rand_word = wn.x_rand_pos(1,'n')[0]  # only 1 item on the list
    noun = rand_word[0]
    definition = rand_word[1]
    article = rand_word[2]

    seconds = 40 # this is the max amount of time to play

    return render_template('sexwithme-game.html',
                           seconds=seconds,
                           article=article,
                           noun=noun,
                           definition=definition,
                           MODE=MODE)


@app.route('/_save_sex-with-me', methods=['GET', 'POST'])
@login_required(role=0, group='open')
def save_sexwithme():
    if request.method == 'POST':
        result = request.form

        language = 'eng'
        prompt = result['prompt'].strip()
        answer = result['answer'].strip()
        seconds = result['seconds']
        username = result['username']

        # it's always treated as 1 sentence, so we can do this:
        if answer:
            parse = delphin_call.check_sents([answer])[0]
            errors = parse[1] # should be of type [('non_third_sg_fin_v_rbst', 'wants')]            
        else:
            errors = []

        tags = []
        foci = []
        for e in errors:
            tag = e[0]
            focus = e[1]
            tags.append(tag)
            foci.append(focus)

        if answer and tags and ('NoParse' not in tags):
            # we are not showing feedback for a 'NoParse'

            sex_with_me_id = None
            for tag in tags:
                write_sexwithme_feedback(answer, sex_with_me_id, tag,
                                         seconds, language, username, current_time())

            return render_template('sexwithme-feedback.html',
                                   answer=answer,
                                   tags=tags,
                                   foci=foci,
                                   eng_feedback=eng_feedback,
                                   MODE=MODE)

        if answer and tags and ('NoParse' in tags):
            sex_with_me_id = write_sexwithme(prompt, answer, seconds, language,
                                             username, current_time())

            for tag in tags:
                write_sexwithme_feedback(answer, sex_with_me_id, tag,
                                         seconds, language, username, current_time())

        elif answer:
            write_sexwithme(prompt, answer, seconds, language,
                            username, current_time())
            
        else:
            write_sexwithme(prompt, None, seconds, language,
                            username, current_time())
    
    return sexwithme_game()





### WICKED PROVERBS

@app.route('/info/wicked-proverbs', methods=['GET', 'POST'])
@login_required(role=0, group='open')
def wickedproverbs_info():

    base_ex = [(0, "My mother always said:",
                "A high school cheerleader's love is like an old bicycle in a remote village.",
                "Everyone is welcome to take a ride, but it's squeaks in wrong ways,  and as soon as you are going down you will start to regret it.",
                "The CALLIG System",
                "Unknown date",
                "0 seconds")]


    example_list = []
    exs = fetch_wickedproverbs_30()
    for i, ex_id in enumerate(exs.keys()):
        r = exs[ex_id]

        frame = r[0]
        proverb = r[1]
        explanation = r[2]
        seconds = str(r[3]) + ' ' + 'seconds'
        username = r[5]
        timestamp = r[6].split()[0]

        example_list.append((i, frame, proverb, explanation, username, timestamp, seconds))

    if example_list:
        return render_template('wickedproverbs-info.html',
                               example_list=example_list,
                               MODE=MODE)

    else: # for brand-new dbs, show a system's example
        return render_template('wickedproverbs-info.html',
                               example_list=base_ex,
                               MODE=MODE)



@app.route('/games/wicked-proverbs', methods=['GET', 'POST'])
@login_required(role=0, group='open')
def wickedproverbs_game():
    """
    For now this only decides between Noun-Noun and Noun-Verb.
    Definitions should exist come for each word.
    It gets a random frame from game_data.
    """
    game_option = random.randrange(3)  # 0, 1 or 2 
    
    if game_option == 0:
        nouns = wn.x_rand_pos(2,'n')
        w1 = nouns[0]
        w2 = nouns[1]
        
    elif game_option == 1:
        w1 = wn.x_rand_pos(1,'v')[0]
        w2 = wn.x_rand_pos(1,'n')[0]

    else:
        w1 = wn.x_rand_pos(1,'v')[0]
        w2 = wn.x_rand_pos(1,'a')[0]
            
            
    frame = random.choice(game_data.proverb_frames)            

    seconds = 90 # this is the max amount of time to play

    return render_template('wickedproverbs-game.html',
                           seconds=seconds,
                           w1=w1,
                           w2=w2,
                           frame=frame,
                           MODE=MODE)


@app.route('/_save_wicked-proverbs', methods=['GET', 'POST'])
@login_required(role=0, group='open')
def save_wickedproverbs():
    if request.method == 'POST':
        result = request.form

        frame = result['frame'].strip()
        w1 = result['w1'].strip()
        w2 = result['w2'].strip()
        proverb = result['proverb'].strip()
        explanation = result['explanation'].strip()
        seconds = result['seconds']

        if proverb and explanation:
            write_wickedproverbs(frame, w1, w2, proverb, explanation, seconds,
                                 'eng', result['username'], current_time())
        else:
            write_wickedproverbs(frame, w1, w2, None, None, seconds,
                                 'eng', result['username'], current_time())
    
    return wickedproverbs_game()
    



################################################################################
# CALLIG: FORCED LINKS
################################################################################
@app.route('/info/forced-links', methods=['GET', 'POST'])
@login_required(role=0, group='open')
def forcedlinks_info():

    example_list = []
    exs = fetch_forcedlinks()
    for i, ex_id in enumerate(exs.keys()):
        r = exs[ex_id]

        w1 = r[0]
        w2 = r[1]
        links_json = r[2]
        timestamps_json = r[3]
        seconds = str(r[4]) + ' ' + 'seconds'
        username = r[6]
        timestamp = r[7].split()[0]

        example_list.append((i, w1, w2,
                             json.loads(links_json),
                             json.loads(timestamps_json),
                             seconds, username, timestamp))

    if example_list:
        return render_template('callig_forcedlinks_info.html',
                               example_list=example_list,
                               MODE=MODE)

    else:  # for brand-new dbs, show a system's example
        return render_template('callig_forcedlinks_info.html',
                               example_list=[[0, 'moustache', 'cotton candy', ['hair', 'fluffy'],
                                              ['0', '0'], '0', "The CALLIG System", "Unknown date"]],
                               MODE=MODE)



@app.route('/games/forced-links', methods=['GET', 'POST'])
@login_required(role=0, group='open')
def forcedlinks_game():
    """
    This function generates the prompts for forced-links. This prompt includes
    2 words and an integer (i.e. the minimum number of words between the 2 
    words to be linked. And the time to complete it.
   
    We currently want only the following pairs: 
    Noun-Noun (50%), Noun-Adjective (50%).

    FIXME: We should be checking for distance between promts. We don't want
    words that are too similar. They should be distant.
    FIXME: Try to keep time spent in each link
    """

    # min_links = random.randrange(5) + 2 # (0-4)+2 = 2-6 links
    min_links = 1

    rand = random.random()
    if rand < 0.5:  # mass from list
        nouns = wn.x_rand_pos(2, 'n')
        w1 = nouns[0]
        w2 = nouns[1]

    else:  # we want to randomize the order of noun-adjective

        if rand < 0.75:
            w1 = wn.x_rand_pos(1, 'n')[0]
            w2 = wn.x_rand_pos(1, 'a')[0]
        else:
            w1 = wn.x_rand_pos(1, 'a')[0]
            w2 = wn.x_rand_pos(1, 'n')[0]

    seconds = 45  # the max amount of time to play

    return render_template('callig_forcedlinks_game.html',
                           seconds=seconds,
                           w1=w1,
                           w2=w2,
                           min_links=min_links,
                           MODE=MODE)


@app.route('/_save_forcedlinks', methods=['GET', 'POST'])
@login_required(role=0, group='open')
def save_forcedlinks():
    if request.method == 'POST':
        result = request.form

        w1 = result['w1'].strip()
        w2 = result['w2'].strip()
        seconds = result['seconds']
        username = result['username']
        links = result.getlist('links')  # list
        time_stamps = result.getlist('timestamps')  # list

        # Because the way the JS is currently designed, when users submit,
        # there might be a timestap with an empty string for word.
        # This happens when people add a word box and don't use it before
        # submission.

        links_json = json.dumps(links)
        timestamps_json = json.dumps(time_stamps)

        language = 'eng'
        timestamp = current_time()

        write_forcedlinks(w1, w2, links_json, timestamps_json,
                          seconds, language, username, timestamp)

        return forcedlinks_game()


###############################################################################
# CALLIG: HAIKU ON DEMAND
###############################################################################
@app.route('/info/haiku-on-demand', methods=['GET', 'POST'])
@login_required(role=0, group='open')
def haikuondemand_info():

    base_ex = [(0,
                "The Heavy Power Drill",
                "The drill is unplugged",
                "Like a dead and heavy man",
                "Cordless and lifeless",
                "The CALLIG System",
                "Unknown date",
                "0 seconds")]

    example_list = []
    exs = fetch_haikuondemand_30()
    for i, ex_id in enumerate(exs.keys()):
        r = exs[ex_id]
        title = r[0]
        l1 = r[1]
        l2 = r[2]
        l3 = r[3]
        username = r[4]
        timestamp = r[5].split()[0]
        seconds = str(r[6]) + ' '  + 'seconds'

        example_list.append((i, title, l1, l2, l3,
                             username, timestamp, seconds))

    if example_list:
        return render_template('haikuondemand-info.html',
                               example_list=example_list,
                               MODE=MODE)

    else: # for brand-new dbs, show a system's example
        return render_template('haikuondemand-info.html',
                               example_list=base_ex,
                               MODE=MODE)


@app.route('/games/haiku-on-demand', methods=['GET', 'POST'])
@login_required(role=0, group='open')
def haikuondemand_game():
    rand_noun = wn.x_rand_pos(1,'n')[0]
    rand_adj = wn.x_rand_pos(1,'a')[0]
    seconds = 90

    return render_template('haikuondemand-game.html',
                           seconds=seconds,
                           rand_noun=rand_noun,
                           rand_adj=rand_adj,
                           MODE=MODE)

    
@app.route('/_save_haiku-on-demand', methods=['GET', 'POST'])
@login_required(role=0, group='open')
def save_haikuondemand():
    """
    Haiku does not have grammar checking; but it checks for the
    correct number of syllables; in the future, if words are required
    to be used, this should also be checked;
    """
    
    if request.method == 'POST':
        result = request.form

        language = 'eng'
        title = result['title'].strip()
        l1 = result['line1'].strip() if 'line1' in result.keys() else '' 
        l2 = result['line2'].strip() if 'line2' in result.keys() else ''
        l3 = result['line3'].strip() if 'line3' in result.keys() else ''
        seconds = result['seconds']
        username = result['username']

        s1 = syl.num_of_syllables(l1)
        s2 = syl.num_of_syllables(l2)
        s3 = syl.num_of_syllables(l3)

        if (l1 and l2 and l3):
            if (s1 != 5) or (s2 != 7) or (s3 != 5): # SYLLABLE PROBLEM

                answer = [(l1, s1), (l2, s2), (l3, s3)]
                feedback = "syllable count"
                 
                write_haikuondemand_feedback(title, feedback, l1, l2, l3, s1, s2, s3,
                                     seconds, language, username, current_time())
                
                return render_template('haikuondemand-feedback.html',
                                       answer=answer,
                                       title=title,
                                       MODE=MODE)

            else:
                write_haikuondemand(title, l1, l2, l3,
                                    seconds, language, username, current_time())
                return haikuondemand_game()

            
        else: # SKIPPED TITLE
            write_haikuondemand(title, None, None, None,
                            seconds, language, username, current_time())
            
            return haikuondemand_game()




################################################################################
# EMAIL VIEWS
################################################################################
@app.route('/test-email-settings')
@login_required(role=0, group='admin')
def send_mail():
	try:
	    msg = Message("Send Mail Tutorial!",
		          sender="openwns@gmail.com",
		          recipients=["luis.passos.morgado@gmail.com"])
	    msg.body = "Yo!\nHave you heard the good word of Python???"
	    mail.send(msg)
	    return 'Mail sent!'
	except Exception as e:
	    return(str(e))
        

@app.route('/register-mail', methods=['GET', 'POST'])
def register_mail():
    if request.method == 'POST':
        result = request.form

        email = result['email'].strip()
        name = result['name'].strip()

        pw = randomPassword()
        hashed_pw = hash_pass(pw) 
        

        
        ########################################################################
        # Group is a field defines what uses can see and/or can access.
        # it should be a string of the form "grp1-grp2-grp3". All users should
        # start their group with "user-..." e.g. "user-grp1-grp2", while admins
        # should start with "admin-..." instead. However, order of the other
        # groups should not be relevant.
        ########################################################################
        group = 'user'
        if 'callig' in result.keys():
            group += "-callig"

        if 'lccapp' in result.keys():
            group += "-lccapp"

        if group == "user":
            group = "user-callig-lccapp"
        ########################################################################


        
        # print(email) #TEST
        # print(name) #TEST
        # print(pw) #TEST
        # print(hashed_pw) #TEST
        # print(group) #TEST

        # TODO: check if the email already exists... if it does, reject!
        # if it doesn't then create a new user in the DB
        # prepare an html template in case something goes wrong
        #
        
        try:
            msg = Message("Welcome!", # Subject
                          sender="openwns@gmail.com",
                          recipients=["luis.passos.morgado@gmail.com"])

            # msg.body = "..." # if a text-only version is needed
            msg.html = render_template('email-register.html',
                                       name=name,
                                       username=email,
                                       password=pw)

            mail.send(msg)
            return render_template('registration_confirmation.html')

        except Exception as e:
            print(str(e))
            return 'Something went wrong! Please report this.'














################################################################################
# IXUE VIEWS
################################################################################
@app.route('/ixue-jumbled', methods=['GET', 'POST'])
def ixue_jumbled():
    return render_template('ixue_jumbledsents.html',
                           MODE=MODE)




################################################################################
# LCC VIEWS
################################################################################
@app.route('/upload', methods=['GET', 'POST'])
@login_required(role=0, group='open')
def upload():
    return render_template('upload.html',
                           MODE=MODE)


@app.route('/single-sentence', methods=['GET', 'POST'])
@login_required(role=0, group='open')
def lcc_sentence():
    return render_template('lcc_sentence.html',
                           MODE=MODE)


@app.route('/report', methods=['GET', 'POST'])
@login_required(role=0, group='open')
def report():
    """
    This function saves the uploaded file and starts the process that will 
    check the uploaded document. The document check is actually called 
    asynchronously via javascript from within the report template.
    """
    passed, filename = lcc.uploadFile(current_user.id)

    if passed == False:
        error = """There was a problem while uploading your your file. """
        error += """Please check that the file type you are using is '.docx'"""
        error += """ and not '.doc', for example."""
        return render_template('error.html',
                               error=error,
                               MODE=MODE)

    else:
        return render_template('report.html',
                               passed=passed,
                               filename=filename,
                               MODE=MODE)

@app.route('/_save_singlesentence', methods=['GET', 'POST'])
@login_required(role=0, group='open')
def save_lcc_sentence():
    if request.method == 'POST':
        result = request.form

        sent = result['sentence'].strip()
        username = result['username']

        ########################################################################
        # WRITE SENTENCE IN DATABASE
        ########################################################################
        docid = csql.fetch_max_doc_id() + 1
        csql.insert_into_doc(docid, 'single_sentence')

        sid = docid * 100000
        pid = 0
        csql.insert_into_sent(sid, docid, pid, sent)
        word_list = lcc.pos_lemma(lcc.sent2words(sent))        
        for w in word_list:
            wid = csql.fetch_max_wid(sid) + 1
            (surface, pos, lemma) = w
            csql.insert_into_word(sid, wid, surface, pos, lemma)

        words = csql.fetch_words_by_sid(sid, sid)[sid]
        app_errors, non_app_errors = lcc.full_check_sent(sent, words, 'lcc2')

        ########################################################################
        # WRITE ERRORS TO CORPUS DB
        ########################################################################
        all_errors = app_errors | non_app_errors
        for i, (label, loc) in enumerate(all_errors):
            csql.insert_into_error(sid, i, label, loc)
            
        errors = []
        
        for e in app_errors:
            tag = e[0]
            focus = e[1]
            if tag in eng_feedback:
                if 'lcc2' in eng_feedback[tag]:
                    #print(eng_feedback[tag])
                    feedback = eng_feedback[tag]['lcc2'][0].format(focus)
                    errors.append(feedback)
            

        return render_template('lcc_feedback.html',
                               sent=sent,
                               errors=errors,
                               eng_feedback=eng_feedback,
                               MODE=MODE)






@app.route('/lcc-db', methods=['GET', 'POST'])
@login_required(role=0, group='admin')
def inspect_lcc_db():

# <!-- Things we might want: -->

# <!-- - SELECT docid, title FROM doc  (doc.title can be either the file name or single_sentence) -->
# <!-- docid are just keys -->
# <!-- - We definitely don't want to know the doc title, but we might want to check if it was a single sentence -->
# <!-- We might be able to get by just selecting all docsIDs that pertain to a single sentence -->
# <!-- Everything else should belonf to a larger document. -->

# <!-- SELECT sid docID sent from sent; -->
# <!-- - docID is just to know if it actually belongs to a single sent or not. -->
# <!-- sid id we won't need to show for sure, but we need to keep track;  -->
# <!-- sent is where the text exists.  -->


# <!-- SELECT sid eid label comment FROM error;  -->
# <!-- one sid can have multiple eid -->
# <!-- More than one error can exist for each sentence, and these appear in multiple lines of this table -->
# <!-- label is where the LCC error code is stored  -->
# <!-- comment is where the error focus is stored (currently just the words) -->
    
    sents = fetch_all_sents()
    errors_by_sent, errors_by_label = fetch_all_errors()

    db_data = dd(lambda: list())
    for sid in sents.keys():
        db_data[sid].append(sents[sid][0])

        lcc_errors = []
        other_errors = []
        for eid in errors_by_sent[sid]:
            label = eid[1]
            comment = eid[2] 

            if label in eng_feedback.keys():
                if 'lcc2' in eng_feedback[label].keys():
                    lcc_errors.append(label+': '+comment)

                else:
                    other_errors.append((label,comment))
            else:
                other_errors.append((label,comment))
                    
            
        db_data[sid].append(lcc_errors)
        db_data[sid].append(other_errors)
    
    return render_template('lcc_db.html',
                           lang='eng',
                           grammars=AVAILABLE_GRAMMARS[lang],
                           db_data=db_data,
                           # sents=sents,
                           # errors=errors,
                           MODE=MODE)


    
        
        
################################################################################
# GRAMMARIUM VIEWS
################################################################################

@app.route('/delphin/select-profile', methods=['GET', 'POST'])
@login_required(role=0, group='admin')
def delphin_select_profile():
    
    # Not all grammar strucutres are similar. E.g., Zhong is a mess
    # Because of this, I need to have the path to the tsdb folder of each
    # grammar in question; Since we import the grammars via remotes,
    # these shouldn't really change

    # print(delphin_call.get_shell_script_output_using_check_output())

    erg_gold_names = next(os.walk(path.join(ROOT,'delphin/erg2018/tsdb/gold/')))[1]

    zhong_gold_names = next(os.walk(path.join(ROOT,'delphin/zhong/cmn/zhs/tsdb/gold/')))[1]
    zhong_skeleton_names = next(os.walk(path.join(ROOT,'delphin/zhong/cmn/zhs/tsdb/skeletons/')))[1]


    # print(zhong_skeleton_names)
    # print(erg_gold_profiles)

    # Skeletons are actually messier, even in the ERG.
    # erg_skeleton_profiles = next(os.walk('delphin/erg2018/tsdb/skeletons/'))[1]
    # print(erg_skeleton_profiles)

    return render_template('delphin_profiles_selector.html',
                           erg_gold_names=sorted(erg_gold_names),
                           zhong_gold_names=sorted(zhong_gold_names),
                           zhong_skeleton_names=sorted(zhong_skeleton_names),
                           MODE=MODE)


@app.route('/delphin/regression-testing', methods=['GET', 'POST'])
@login_required(role=0, group='open')
def delphin_regression_testing():
    
    # check/create folder 'delphin/regressions/'
    # if not os.path.exists(path.join(ROOT,'delphin/regressions')):
    #     os.makedirs(path.join(ROOT,'delphin/regressions'))

    prev_regressions = next(os.walk(path.join(ROOT,'delphin/regressions/')))[1]

    return render_template('delphin_regression_testing.html',
                           grammars=AVAILABLE_GRAMMARS,
                           prev_regressions=sorted(prev_regressions, reverse=True),
                           MODE=MODE)




@app.route('/delphin_regression_output', methods=['GET', 'POST'])
@login_required(role=0, group='open')
def delphin_regression_output():
    if request.method == 'POST':
        result = request.form

        if 'selected_grammar' in result.keys():
            selected_grammar = result['selected_grammar'].strip()
        else:
            selected_grammar = ''

        if 'regression_dir1' in result.keys():
            regression_dir1 = result['regression_dir1'].strip()
        else:
            regression_dir1 = ''
  
        if 'regression_dir2' in result.keys():
            regression_dir2 = result['regression_dir2'].strip()
        else:
            regression_dir2 = ''

            
        return render_template('delphin_regression_output.html',
                               selected_grammar=selected_grammar,
                               regression_dir1=regression_dir1,
                               regression_dir2=regression_dir2,
                               MODE=MODE)
        
        


@app.route('/_delphin_run_regression', methods=['GET', 'POST'])
@login_required(role=0, group='open')
def delphin_run_regression():

    selected_grammar = request.args.get('selected_grammar', None)  
    dir1 = request.args.get('dir1', None)
    dir2 = request.args.get('dir2', None)

    dir1_path = "delphin/regressions/" + dir1 + '/'
    prof1 = delphin_call.tsdb_min(path.join(ROOT, dir1_path))

    
    # if selected_grammar and dir1 exist, then it's a new regression test
    if (selected_grammar and dir1):    
        stdout, stderr, newdir_path = delphin_call.new_regression(dir1, selected_grammar)

        prof2 = delphin_call.tsdb_min(path.join(ROOT, newdir_path))
        dir2_path = newdir_path
        
    # if dir1 and dir2 exist, then it's just printing previous results
    elif (dir1 and dir2):
        dir2_path = "delphin/regressions/" + dir2 + '/'
        prof2 = delphin_call.tsdb_min(path.join(ROOT, dir2_path))
        stderr = ''
        stdout = ''
    else:
        return "Something went wrong!"


    ############################################################################
    # GATHER SUMMARY STATISTICS
    #
    # We can assume both profiles have the same size and i_id keys
    ############################################################################
    summary = dd()
    summary["prof1"] = dir1_path
    summary["prof2"] = dir2_path
    
    summary["num_of_sents_prof1"] = len(prof1.keys())
    summary["num_of_sents_prof2"] = len(prof2.keys())
    
    summary["sent_length_sum_prof1"] = 0
    summary["sent_length_sum_prof2"] = 0
    
    summary["parsed_sent_length_sum_prof1"] = 0
    summary["parsed_sent_length_sum_prof2"] = 0
    
    summary["total_num_parses_prof1"] = 0
    summary["total_num_parses_prof2"] = 0
    
    summary["num_of_sents_parsed_prof1"] = 0
    summary["num_of_sents_parsed_prof2"] = 0


    ############################################################################
    # Create new structure from both profiles 
    ############################################################################
    profs = dd(lambda: dd())
    for i_id in prof1:
        profs[i_id]['i-wf'] = prof1[i_id]['i-wf']
        profs[i_id]['i-input'] = prof1[i_id]['i-input']
        profs[i_id]['i-comment'] = prof1[i_id]['i-comment']
        profs[i_id]['i-length'] = prof1 [i_id]['i-length']
        profs[i_id]['i-origin'] = prof1 [i_id]['i-origin']
        profs[i_id]['i-translation'] = prof1 [i_id]['i-translation']

        summary["sent_length_sum_prof1"] += int(prof1[i_id]['i-length'])
        summary["sent_length_sum_prof2"] += int(prof2[i_id]['i-length'])

        if 'readings' in prof1[i_id]:
            profs[i_id]['old_readings'] = prof1[i_id]['readings']
            if int(prof1[i_id]['readings'])>0:
                summary['num_of_sents_parsed_prof1'] += 1
                summary['total_num_parses_prof1'] += int(prof1[i_id]['readings'])
                summary["parsed_sent_length_sum_prof1"] += int(prof1[i_id]['i-length'])
        else:
            profs[i_id]['old_readings'] = 0

        if 'readings' in prof2[i_id]:
            profs[i_id]['new_readings'] = prof2[i_id]['readings']
            if int(prof2[i_id]['readings'])>0:
                summary['num_of_sents_parsed_prof2'] += 1
                summary['total_num_parses_prof2'] += int(prof2[i_id]['readings'])
                summary["parsed_sent_length_sum_prof2"] += int(prof2[i_id]['i-length'])

        else:
            profs[i_id]['new_readings'] = 0



    return jsonify(
        html=render_template('delphin_regression_results.html',
                             profs=profs,
                             selected_grammar=selected_grammar),
        summary=render_template('delphin_regression_summary.html',
                                summary=summary),        
        result= '<br>' + utils.stdout2html(stderr))






@app.route('/delphin/see-profile', methods=['GET', 'POST'])
@login_required(role=0, group='admin')
def delphin_see_profile():
    if request.method == 'POST':
        result = request.form

    if 'erg2018_gold_prof' in result.keys():
        profile = 'delphin/erg2018/tsdb/gold/' + result['erg2018_gold_prof'].strip()
        profile_type = 'gold'
        # grammars = ["erg2018.dat"]
        lang = "eng"
        
    elif 'zhong_gold_prof' in result.keys():
        profile = 'delphin/zhong/cmn/zhs/tsdb/gold/' + result['zhong_gold_prof'].strip()
        profile_type = 'gold'
        # grammars = ["zhong.dat"]
        lang = "cmn"
        
    elif 'zhong_skeleton_prof' in result.keys():
        profile = 'delphin/zhong/cmn/zhs/tsdb/skeletons/' + result['zhong_skeleton_prof'].strip()
        profile_type = 'skeleton'
        # grammars = ["zhong.dat"]
        lang = "cmn"
        
    else:
        profile = None
        profile_type = None
        grammars = []
        lang = None
        
    if profile:
        tsdb_min = delphin_call.tsdb_min(profile)
    
        return render_template('delphin_simple_profile.html',
                               tsdb_min=tsdb_min,
                               grammars=AVAILABLE_GRAMMARS[lang],
                               profile_type=profile_type,
                               lang=lang,
                               MODE=MODE)
    else:
        return "Some tampering was detected. This should not happen."
    


@app.route('/delphin_analyser', methods=['GET', 'POST'])
@login_required(role=0, group='admin')
def delphin_analyser():
    """
    This view generates the main input receiver for grammars. 
    It is expecting a language, which is used to provide a collection 
    of available grammars for that language. This can also generate a 
    small list of examples (especially for some non-english languages). 
    """
    # if request.method == 'POST':
    #     result = request.form

    #     lang = result['lang'].strip()

    #     if 'selected_grammar' in result.keys():
    #         selected_grammar = result['selected_grammar']
    #     else:
    #         selected_grammar = None

    #     if 'max_parses' in result.keys():
    #         max_parses = result['max_parses'].strip()
    #     else:
    #         max_parses = None
        
        # grammars = sorted(AVAILABLE_GRAMMARS[lang])
        
    return render_template('delphin_analyser.html',
                               # lang=lang,
                               grammars=AVAILABLE_GRAMMARS,
                               # selected_grammar=selected_grammar,
                               # max_parses=max_parses,
                               MODE=MODE)
            



# @app.route('/_delphin_analyser_output', methods=['GET', 'POST'])
# @login_required(role=0, group='open')
# def delphin_analyser_output():
#     if request.method == 'POST':
#         result = request.form

#         lang = result['lang'].strip()
#         sent = result['sentence'].strip()
#         selected_grammar = result['selected_grammar'].strip()
#         max_parses = result['max_parses'].strip()

#         results = delphin_call.full_parse(sent, selected_grammar, max_parses)

#         # print(results[0]['mrs_simplemrs'])
        
#         return render_template('delphin_analyser_output.html',
#                                lang=lang,
#                                sent=sent,
#                                results=results,
#                                selected_grammar=selected_grammar,
#                                max_parses=max_parses,
#                                MODE=MODE)


@app.route('/_delphin_parse_output', methods=['GET', 'POST'])
@login_required(role=0, group='open')
def delphin_parse_output():
    """
    This function is returning the data structre required to 
    populate the parsing overlay pane.
    """

    sent = request.args.get('sentence', None)
    selected_grammar = request.args.get('selected_grammar', None)  
    max_parses = request.args.get('max_parses', 'all')

    results = delphin_call.full_parse(sent, selected_grammar, max_parses)
    
    return jsonify(html=render_template('delphin_parse_output.html',
                                        sent=sent,
                                        results=results,
                                        selected_grammar=selected_grammar,
                                        max_parses=max_parses,
                                        MODE=MODE),
                   results=results)


    
        
@app.route('/_delphin-parse', methods=['GET', 'POST'])
@login_required(role=0, group='open')
def delphin_parse():

    sent = request.args.get('sentence', None)
    selected_grammar = request.args.get('selected_grammar', None)  
    max_parses = request.args.get('max_parses', 'all')


    print(sent)
    print(selected_grammar)
    print(max_parses)

    
    if sent and selected_grammar and max_parses:

        
        results = delphin_call.full_parse(sent, selected_grammar, max_parses)

        # values = 0 must be returned as string "0", otherwise it will 
        # interfere with 'ifs' when displaying results.
        return jsonify(result=str(len(results.keys())), full_result=results)

    else:
        return jsonify(result='!')
        
        




@app.route("/delphin/update-grammars", methods=['GET', 'POST'])
@login_required(role=0, group='admin')
def delphin_update_grammars():
    return render_template("delphin_update_grammars.html",
                           MODE=MODE)



@app.route('/delphin/_update_erg2018', methods=['GET', 'POST'])
@login_required(role=0, group='open')
def delphin_update_erg2018():
    "Update the ERG2018 repository and build the grammars with ACE."
    
    bash_stdout, bash_stderr = delphin_call.update_erg2018()
    bash_stdout = utils.stdout2html(bash_stdout)
    bash_stderr = "<br><br><b>ACE WARNINGS:</b><br>" + utils.stdout2html(bash_stderr)        
    return jsonify(result=bash_stdout+bash_stderr)

@app.route('/delphin/_update_itell-erg2018', methods=['GET', 'POST'])
@login_required(role=0, group='open')
def delphin_update_itell_erg2018():
    "Update the ERG2018 and ITELL-ERG repository and build the grammar with ACE."
    
    bash_stdout, bash_stderr = delphin_call.update_itell_erg2018()
    bash_stdout = utils.stdout2html(bash_stdout)
    bash_stderr = "<br><br><b>ACE WARNINGS:</b><br>" + utils.stdout2html(bash_stderr)        
    return jsonify(result=bash_stdout+bash_stderr)

@app.route('/delphin/_update_ergTRUNK', methods=['GET', 'POST'])
@login_required(role=0, group='open')
def delphin_update_ergTRUNK():
    "Update the ERG-TRUNK repository and build the grammars with ACE."
    
    bash_stdout, bash_stderr = delphin_call.update_ergTRUNK()
    bash_stdout = utils.stdout2html(bash_stdout)
    bash_stderr = "<br><br><b>ACE WARNINGS:</b><br>" + utils.stdout2html(bash_stderr)        
    return jsonify(result=bash_stdout+bash_stderr)


@app.route('/delphin/_update_zhong', methods=['GET', 'POST'])
@login_required(role=0, group='open')
def delphin_update_zhong():
    "Update ZHONG's repository and build the grammars with ACE."

    bash_stdout, bash_stderr = delphin_call.update_zhong()
    bash_stdout = utils.stdout2html(bash_stdout)
    bash_stderr = "<br><br><b>ACE WARNINGS:</b><br>" + utils.stdout2html(bash_stderr)
    return jsonify(result=bash_stdout+bash_stderr)

@app.route('/delphin/_update_itell-zhong', methods=['GET', 'POST'])
@login_required(role=0, group='open')
def delphin_update_itell_zhong():
    "Update ZHONG and ITELL-ZHONG repository and build the grammar with ACE."
    
    bash_stdout, bash_stderr = delphin_call.update_itell_zhong()
    bash_stdout = utils.stdout2html(bash_stdout)
    bash_stderr = "<br><br><b>ACE WARNINGS:</b><br>" + utils.stdout2html(bash_stderr)        
    return jsonify(result=bash_stdout+bash_stderr)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', threaded=True)
