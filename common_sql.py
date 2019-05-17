#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
from flask import Flask, current_app, g
from collections import defaultdict as dd
from os import path

def qs(ll):
    """return len(l) ?s sepeated by ','  to use in queries"""
    return ','.join('?' for l  in ll)

app = Flask(__name__)
with app.app_context():

    ROOT  = path.dirname(path.realpath(__file__))    
    ADMINDB = 'db/admin.db'
    CALLIGDB = 'db/callig.db'


    ############################################################################
    # SET UP CONNECTIONS
    ############################################################################
    def connect_admin():
        return sqlite3.connect(path.join(ROOT, ADMINDB))

    def connect_callig():
        return sqlite3.connect(path.join(ROOT, CALLIGDB))
    
    def query_admin(query, args=(), one=False):
        cur = g.admin.execute(query, args)
        rv = [dict((cur.description[idx][0], value)
                   for idx, value in enumerate(row)) for row in cur.fetchall()]
        return (rv[0] if rv else None) if one else rv

    def query_callig(query, args=(), one=False):
        cur = g.callig.execute(query, args)
        rv = [dict((cur.description[idx][0], value)
                   for idx, value in enumerate(row)) for row in cur.fetchall()]
        return (rv[0] if rv else None) if one else rv

    def write_admin(query, args=(), one=False):
        cur = g.admin.cursor()
        cur.execute(query, args)
        lastid = cur.lastrowid
        g.admin.commit()
        return lastid

    def write_callig(query, args=(), one=False):
        cur = g.callig.cursor()
        cur.execute(query, args)
        lastid = cur.lastrowid
        g.callig.commit()
        return lastid


    ############################################################################
    # ADMIN SQL
    ############################################################################

    def fetch_userid(userID):
        user = None
        for r in query_admin("""SELECT userID, password, 
                                       access_level, access_group, full_name
                                FROM users
                                WHERE userID = ?""", [userID]):
            if r['userID']:
                user = (r['userID'], r['password'], 
                        r['access_level'], r['access_group'], r['full_name'])
        return user


    def fetch_id_from_userid(userID):
        for r in query_admin("""SELECT id 
                                FROM users
                                WHERE userID = ?""", [userID]):
            return r['id']


    def fetch_allusers():
        users = dd()
        for r in query_admin("""SELECT * FROM users"""):
            users[r['id']] = r

        return users


    ############################################################################
    # CALLIG SQL
    ############################################################################

    def write_sexwithme(prompt, answer, seconds, language, username, timestamp):
        """
        Returns the ID of the recently added entry.
        """
        return write_callig("""INSERT INTO sex_with_me (prompt, answer, 
                                                      seconds, language, 
                                                      username, timestamp)
                               VALUES (?,?,?,?,?,?)""",
                            [prompt, answer, seconds,
                             language, username, timestamp])

    def write_sexwithme_feedback(answer, sex_with_me_id, feedback,
                                 seconds, language, username, timestamp):
        """
        Returns the ID of the recently added entry.
        """
        return write_callig("""INSERT INTO sex_with_me_feedback 
                                           (answer, sex_with_me_id, feedback,
                                            seconds, language, username, timestamp)
                               VALUES (?,?,?,?,?,?,?)""",
                            [answer, sex_with_me_id, feedback,
                             seconds, language, username, timestamp])

    
    def fetch_sexwithme_30():
        result = dd()
        for r in query_callig("""SELECT * FROM sex_with_me WHERE answer IS NOT NULL 
                                 ORDER BY timestamp DESC LIMIT 30"""):
            result[r['id']] = [r['prompt'], r['answer'],r['seconds'],r['language'],
                               r['username'], r['timestamp']]
        return result



    def write_wickedproverbs(frame, w1, w2, proverb, explanation, seconds,
                             language, username, timestamp):
        """
        Returns the ID of the recently added entry.
        """
        return write_callig("""INSERT INTO wicked_proverbs 
                               (frame, w1, w2, proverb, explanation, seconds,
                                language, username, timestamp)
                               VALUES (?,?,?,?,?,?,?,?,?)""",
                            [frame, w1, w2, proverb, explanation, seconds,
                             language, username, timestamp])


    def fetch_wickedproverbs_30():
        result = dd()
        for r in query_callig("""SELECT * FROM wicked_proverbs 
                                 WHERE proverb IS NOT NULL
                                 AND explanation IS NOT NULL
                                 ORDER BY timestamp DESC LIMIT 30"""):
            result[r['id']] = [r['frame'], r['proverb'],r['explanation'],
                               r['seconds'],r['language'],
                               r['username'], r['timestamp']]
        return result

