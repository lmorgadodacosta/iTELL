#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3, datetime
from flask import Flask, current_app, url_for
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user#, wraps
from functools import wraps
from itsdangerous import URLSafeTimedSerializer # for safe session cookies
from hashlib import md5

from common_sql import *

app = Flask(__name__)
with app.app_context():

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = '/login'
    login_manager.login_message = "You don't seem to have permission to see this content."
    app.secret_key = "!$flhgSgngNO%$#SOET!$!"
    app.config["REMEMBER_COOKIE_DURATION"] = datetime.timedelta(minutes=30)
    login_serializer = URLSafeTimedSerializer(app.secret_key)

    def hash_pass(password):
        """ Return the md5 hash of the password+salt """
        salted_password = password + app.secret_key
        return md5(salted_password.encode('utf-8')).hexdigest()


    def login_required(role=0, group='open'):
        """
        This is a redefinition of the decorator login_required,
        to include a 'role' argument to allow users with different
        roles access different views and a group access to close some
        views by groups. For example:
        @login_required(role=0, group='ntuwn')   0 = for all
        """
        def wrapper(fn):
            @wraps(fn)
            def decorated_view(*args, **kwargs):
                if not current_user.is_authenticated:
                    return login_manager.unauthorized()
                if current_user.role < role:
                    return login_manager.unauthorized()
                if group != 'open' and current_user.group != group:
                    return login_manager.unauthorized()

                return fn(*args, **kwargs)
            return decorated_view
        return wrapper


    class User(UserMixin):
        def __init__(self, userID, password, role, group):
            self.id = userID
            self.password = password
            self.role = role
            self.group = group

        def get_auth_token(self):
            """ Encode a secure token for cookie """
            data = [str(self.id), self.password]
            return login_serializer.dumps(data)

        def get_role(self):
            """ Returns the role (access level) for the user """
            return self.role

        @staticmethod
        def get(userid):
            """
            Static method to search the database and see if userid exists.
            If it does exist then return a User Object. If not then return
            None, as required by Flask-Login.
            """
            user = fetch_userid(userid)

            if user:
                return User(user[0], user[1], user[2], user[3])
            else:
                return None


    @login_manager.user_loader
    def load_user(userID):
        """ This function, given an user_id, needs to check 
        whether this user 'is active'. The userid was stored 
        in the session environment by Flask-Login. user_loader 
        stores the returned User object in current_user during 
        every flask request.
        """
        return User.get(userID)


    @login_manager.request_loader
    def load_user_from_request(request):

        # first, try to login using the api_key url arg
        api_key = request.args.get('api_key')
        if api_key:
            user = User.query.filter_by(api_key=api_key).first()
            if user:
                return user

        # next, try to login using Basic Auth
        api_key = request.headers.get('Authorization')
        if api_key:
            api_key = api_key.replace('Basic ', '', 1)
            try:
                api_key = base64.b64decode(api_key)
            except TypeError:
                pass
            user = User.query.filter_by(api_key=api_key).first()
            if user:
                return user

        # finally, return None if both methods did not login the user
        return None
