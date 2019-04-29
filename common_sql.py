#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
from flask import Flask, current_app, g
from collections import defaultdict as dd

def qs(ll):
    """return len(l) ?s sepeated by ','  to use in queries"""
    return ','.join('?' for l  in ll)

app = Flask(__name__)
with app.app_context():

    ADMINDB = 'db/admin.db'
    CORPUSDB = 'db/corpus.db'
    GOLDDB = 'db/goldcorpus.db'


    ############################################################################
    # SET UP CONNECTIONS
    ############################################################################
    def connect_admin():
        return sqlite3.connect(ADMINDB)

    def connect_corpus():
        return sqlite3.connect(CORPUSDB)

    def connect_gold():
        return sqlite3.connect(GOLDDB)

    
    def query_admin(query, args=(), one=False):
        cur = g.admin.execute(query, args)
        rv = [dict((cur.description[idx][0], value)
                   for idx, value in enumerate(row)) for row in cur.fetchall()]
        return (rv[0] if rv else None) if one else rv

    def query_corpus(query, args=(), one=False):
        cur = g.corpus.execute(query, args)
        rv = [dict((cur.description[idx][0], value)
                   for idx, value in enumerate(row)) for row in cur.fetchall()]
        return (rv[0] if rv else None) if one else rv

    def query_gold(query, args=(), one=False):
        cur = g.gold.execute(query, args)
        rv = [dict((cur.description[idx][0], value)
                   for idx, value in enumerate(row)) for row in cur.fetchall()]
        return (rv[0] if rv else None) if one else rv

    def write_admin(query, args=(), one=False):
        cur = g.admin.cursor()
        cur.execute(query, args)
        lastid = cur.lastrowid
        g.admin.commit()
        return lastid

    def write_corpus(query, args=(), one=False):
        cur = g.corpus.cursor()
        cur.execute(query, args)
        lastid = cur.lastrowid
        g.corpus.commit()
        return lastid

    def write_gold(query, args=(), one=False):
        cur = g.gold.cursor()
        cur.execute(query, args)
        lastid = cur.lastrowid
        g.gold.commit()
        return lastid


    ############################################################################
    # ADMIN SQL
    ############################################################################

    def fetch_userid(userID):
        user = None
        for r in query_admin("""SELECT userID, password, 
                                       access_level, access_group 
                                FROM users
                                WHERE userID = ?""", [userID]):
            if r['userID']:
                user = (r['userID'], r['password'], 
                        r['access_level'], r['access_group'])
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
