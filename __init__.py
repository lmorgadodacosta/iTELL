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
#from lxml import etree

## profiler
#from werkzeug.contrib.profiler import ProfilerMiddleware


from common_login import *
from common_sql import *
# from corpus import *
# from check import *


# from math import log


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
    g.corpus = connect_corpus()
    g.gold = connect_gold()

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.admin.close()
        g.corpus.close()
        g.gold.close()
################################################################################



################################################################################
# GENERAL FUNCTIONS
################################################################################
def current_time():
    '''   2017-8-17  14:35    '''
    d = datetime.datetime.now()
    return d.strftime('%Y-%m-%d_%H:%M:%S')
################################################################################


################################################################################
# AJAX REQUESTS
################################################################################

@app.route('/_file2db', methods=['GET', 'POST'])
@login_required(role=0, group='open')
def file2db():

    error_logging = open("corpus_inputting_error_log", "a")
    filename = request.args.get('fn', None)

    if ROBUSTEXCEPT:
        
        try:                                                   ####tk####
            r = docx2html(filename)

        except TimeoutError:                                                       ####tk####
            current_time = current_time()                                          ####tk####
            error_logging.write(current_time+"\n")                                 ####tk####
            error_logging.write("DOCNAME: {}\n".format(filename))                         ####tk####
            error_logging.write("Type: Timeout\n\n")                            ####tk####

            #return render_template("exception.html")                               ####tk####
            #return jsonify(result=False)#  docx2html_exception()                            ####tk####
            r = False
            error_logging.close()          

        except Exception as e:                                                     ####tk####
            current_time = current_time()                                          ####tk####
            error_logging.write(current_time+"\n")                                 ####tk####
            error_logging.write("DOCNAME: {}\n".format(filename))                         ####tk####
            error_logging.write("Type: {type}\n".format(type=type(e)))               ####tk####
            error_logging.write("Args: {args}\n".format(args=e.args))                ####tk####

            if hasattr(e, 'message'):
                error_logging.write("Message: {message}\n".format(message=e.message))    ####tk####

            error_logging.write("Error: {error}\n\n".format(error=e))             ####tk####
            error_logging.close()          
            r = False
            #return render_template("exception.html")                            ####tk####
            #return jsonify(result=False)#docx2html_exception()                            ####tk####

    else:
            r = docx2html(filename)

    return jsonify(result=r)




################################################################################
# VIEWS
################################################################################
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('welcome.html')

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
