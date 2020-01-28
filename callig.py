#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys, sqlite3, datetime, urllib, gzip, requests, codecs
import random, string 
from flask import Flask, render_template, g, request, redirect, url_for, send_from_directory, session, flash, jsonify, make_response, Markup
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from flask_mail import Mail, Message
from functools import wraps
from itsdangerous import URLSafeTimedSerializer # for safe session cookies
from collections import defaultdict as dd
from hashlib import md5
from werkzeug import secure_filename


import lxml.html # to manipulate html 

from common_login import *
from common_sql import *

from collections import defaultdict as dd
def inf_dd():
    return dd(inf_dd)


import lcc
import wn
import syl
import game_data
import erg_call
import common_sql as csql
from feedback import eng_feedback

app = Flask(__name__)
#app.debug = True
app.secret_key = "!$flhgSgngNO%$#SOET!$!"
app.config["REMEMBER_COOKIE_DURATION"] = datetime.timedelta(minutes=30)

app.config.update(
    # When using gmail, we need to allow unsafe apps to use the email.
    # check: https://pythonprogramming.net/flask-email-tutorial/
    
    DEBUG=True, 
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
    return render_template("login.html")

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
    """

    filename = request.args.get('fn', None)

    docx_html = lcc.docx2html(filename)
    (docid, htmlElem, report) = lcc.parse_docx_html(docx_html, filename) 

    (htmlElem, report) = lcc.check_docx_html(docid, htmlElem, report)
    
    
    # lxml.html.tostring returns type=bytes, must decode here
    structured_html = lxml.html.tostring(htmlElem).decode('utf-8')
    return jsonify(result=structured_html)




################################################################################
# STATIC VIEWS
################################################################################
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('welcome.html')

@app.route('/team', methods=['GET', 'POST'])
def team():
    return render_template('team.html')

@app.route('/callig', methods=['GET', 'POST'])
def callig_intro():
    return render_template('callig_intro.html')

@app.route('/lcc', methods=['GET', 'POST'])
def lcc_intro():
    return render_template('lcc_intro.html')


@app.route('/improvisation', methods=['GET', 'POST'])
def improvisation():
    return render_template('improvisation.html')


################################################################################
# ADMIN VIEWS
################################################################################

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')


################################################################################
# GAMES VIEWS
################################################################################

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
        seconds = str(r[2]) + ' '  + 'seconds'
        language = r[3]
        username = r[4]
        timestamp = r[5].split()[0]

        example_list.append((i, prompt + '... ' + answer,
                             username, timestamp, seconds))

    if example_list:
        return render_template('sexwithme-info.html',
                               example_list=example_list)

    else: # for brand-new dbs, show a system's example
        return render_template('sexwithme-info.html',
                               example_list=base_ex)

    
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
                           definition=definition)


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
            parse = erg_call.check_sents([answer])[0]
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
                                   eng_feedback=eng_feedback)

        if answer and tags and ('NoParse' in tags):
            sex_with_me_id = write_sexwithme(prompt, answer, seconds, language,
                                             username, current_time())

            for tag in tags:
                write_sexwithme_feedback(answer, sex_with_me_id, tag,
                                         seconds, language, username, current_time())

        elif answer:
            print(write_sexwithme(prompt, answer, seconds, language,
                            username, current_time()))
            
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
        seconds = str(r[3]) + ' '  + 'seconds'
        language = r[4]
        username = r[5]
        timestamp = r[6].split()[0]

        example_list.append((i, frame, proverb, explanation, username, timestamp, seconds))

    if example_list:
        return render_template('wickedproverbs-info.html',
                               example_list=example_list)

    else: # for brand-new dbs, show a system's example
        return render_template('wickedproverbs-info.html',
                               example_list=base_ex)



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
                           frame=frame)


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
    




### HAIKU ON DEMAND

@app.route('/info/haiku-on-demand', methods=['GET', 'POST'])
@login_required(role=0, group='open')
def haikuondemand_info():

    base_ex = [(0,
                "The Heavy Power Drill", "The drill is unplugged", "Like a dead and heavy man", "Cordless and lifeless",
                "The CALLIG System", "Unknown date", "0 seconds")]
    
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
                               example_list=example_list)

    else: # for brand-new dbs, show a system's example
        return render_template('haikuondemand-info.html',
                               example_list=base_ex)


@app.route('/games/haiku-on-demand', methods=['GET', 'POST'])
@login_required(role=0, group='open')
def haikuondemand_game():
    rand_noun = wn.x_rand_pos(1,'n')[0]
    rand_adj = wn.x_rand_pos(1,'a')[0]
    seconds = 90

    return render_template('haikuondemand-game.html',
                           seconds=seconds,
                           rand_noun=rand_noun,
                           rand_adj=rand_adj)

    
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
                                       title=title)

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


        
        print(email) #TEST
        print(name) #TEST
        print(pw) #TEST
        print(hashed_pw) #TEST
        print(group) #TEST

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
# LCC VIEWS
################################################################################
@app.route('/upload', methods=['GET', 'POST'])
@login_required(role=0, group='open')
def upload():
    return render_template('upload.html')


@app.route('/single-sentence', methods=['GET', 'POST'])
@login_required(role=0, group='open')
def lcc_sentence():
    return render_template('lcc_sentence.html')


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
        return render_template('error.html', error=error)

    else:
        return render_template('report.html',
                               passed=passed,
                               filename=filename)

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
        print()
        word_list = lcc.pos_lemma(lcc.sent2words(sent))        
        for w in word_list:
            wid = csql.fetch_max_wid(sid) + 1
            (surface, pos, lemma) = w
            csql.insert_into_word(sid, wid, surface, pos, lemma)

        words = csql.fetch_words_by_sid(sid, sid)[sid]
        app_errors, non_app_errors = lcc.full_check_sent(sent, words, 'lcc')

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
                if 'lcc' in eng_feedback[tag]:
                    print(eng_feedback[tag])
                    feedback = eng_feedback[tag]['lcc'][0].format(focus)
                    errors.append(feedback)
            

        return render_template('lcc_feedback.html',
                               sent=sent,
                               errors=errors,
                               eng_feedback=eng_feedback)
    


        # if answer and tags and ('NoParse' not in tags):
        #     # we are not showing feedback for a 'NoParse'

        #     sex_with_me_id = None
        #     for tag in tags:
        #         write_sexwithme_feedback(answer, sex_with_me_id, tag,
        #                                  seconds, language, username, current_time())

        #     return render_template('lcc_feedback.html',
        #                            answer=answer,
        #                            tags=tags,
        #                            foci=foci,
        #                            eng_feedback=eng_feedback)

        # if answer and tags and ('NoParse' in tags):
        #     sex_with_me_id = write_sexwithme(prompt, answer, seconds, language,
        #                                      username, current_time())

        #     for tag in tags:
        #         write_sexwithme_feedback(answer, sex_with_me_id, tag,
        #                                  seconds, language, username, current_time())

        # elif answer:
        #     print(write_sexwithme(prompt, answer, seconds, language,
        #                     username, current_time()))
            
        # else:
        #     write_sexwithme(prompt, None, seconds, language,
        #                     username, current_time())
    
    return sexwithme_game()


        
        
################################################################################
# ADMIN VIEWS
################################################################################

@app.route("/useradmin",methods=["GET"])
@login_required(role=99, group='admin')
def useradmin():
    users = fetch_allusers()
    return render_template("useradmin.html", users=users)




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', threaded=True)
