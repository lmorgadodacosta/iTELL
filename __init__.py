#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys, sqlite3, datetime, urllib, gzip, requests, codecs
from time import sleep
from flask import Flask, render_template, g, request, redirect, url_for, send_from_directory, session, flash, jsonify, make_response, Markup
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from functools import wraps
from itsdangerous import URLSafeTimedSerializer # for safe session cookies
from collections import defaultdict as dd
from collections import OrderedDict as od
from hashlib import md5
from werkzeug import secure_filename


from common_login import *
from common_sql import *

import wn

app = Flask(__name__)
app.secret_key = "!$flhgSgngNO%$#SOET!$!"
app.config["REMEMBER_COOKIE_DURATION"] = datetime.timedelta(minutes=30)
ROBUSTEXCEPT = False
#error_logging = open("corpus_inputting_error_log", "a")#, "utf-8")    ####tk####

################################################################################
# LOGIN
################################################################################
login_manager.init_app(app)

@app.route("/login", methods=["GET", "POST"])
def login():
    """ This login function checks if the username & password
    match the admin.db; if the authentication is successful,
    it passes the id of the user into login_user() """

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

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.admin.close()
        g.callig.close()
################################################################################



################################################################################
# GENERAL FUNCTIONS
################################################################################
def current_time():
    '''   2017-8-17  14:35    '''
    d = datetime.datetime.now()
    return d.strftime('%Y-%m-%d %H:%M:%S')
################################################################################


################################################################################
# AJAX REQUESTS
################################################################################


################################################################################
# STATIC VIEWS
################################################################################
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('welcome.html')

@app.route('/team', methods=['GET', 'POST'])
def team():
    return render_template('team.html')

@app.route('/improvisation', methods=['GET', 'POST'])
def improvisation():
    return render_template('improvisation.html')


################################################################################
# GAMES VIEWS
################################################################################

@app.route('/games/sex-with-me', methods=['GET', 'POST'])
@login_required(role=0, group='open')
def sexwithme_game():

    noun, definition = wn.random_countable_noun('eng')

    # problems "mass nouns" (they should not take 'a' or 'an')
    # we should block concepts with 3 or more words 
    # block = "family ...", "genus..."
    # block   nouns starting with uppercase
    while noun[0].isupper() or\
       noun.startswith(('family ', 'genus ')) or\
       len(noun.split())>2:
        noun, definition = wn.random_countable_noun('eng')

    if noun.lower().startswith(('a','e','i','o','u')):
        article = 'an'
    else:
        article ='a'

    seconds = 30 # this is the max amount of time to play

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

        prompt = result['prompt'].strip()
        answer = result['answer'].strip()
        seconds = result['seconds']

        if answer:
            write_sexwithme(prompt, answer, seconds, 'eng',
                            result['username'], current_time())
        else:
            write_sexwithme(prompt, None, seconds, 'eng',
                            result['username'], current_time())
    
    return sexwithme_game()


@app.route('/info/sex-with-me', methods=['GET', 'POST'])
@login_required(role=0, group='open')
def sexwithme_info():

    base_ex = [("Sex with me is like a mountain... it will make you want to get on top.", "The CALLIG System", "Unknown date", "0 seconds")]

    example_list = []
    exs = fetch_sexwithme_30()
    for ex_id in exs.keys():
        r = exs[ex_id]
        prompt = r[0]
        answer = r[1]
        seconds = str(r[2]) + ' '  + 'seconds'
        language = r[3]
        username = r[4]
        timestamp = r[5].split()[0]

        example_list.append((prompt + '... ' + answer,
                             username, timestamp, seconds))

    if example_list:
        return render_template('sexwithme-info.html',
                               example_list=example_list)

    else: # for brand-new dbs, show a system's example
        return render_template('sexwithme-info.html',
                               example_list=base_ex)
        
    

################################################################################
# ADMIN VIEWS
################################################################################

@app.route("/useradmin",methods=["GET"])
@login_required(role=99, group='admin')
def useradmin():
    users = fetch_allusers()
    return render_template("useradmin.html", users=users)

@app.route('/upload', methods=['GET', 'POST'])
@login_required(role=0, group='open')
def upload():
    return render_template('upload.html')

@app.route('/report', methods=['GET', 'POST'])
@login_required(role=0, group='open')
def report():
    passed, filename = uploadFile(current_user.id)
    return render_template('report.html',
                           passed=passed,
                           filename=filename)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', threaded=True)
