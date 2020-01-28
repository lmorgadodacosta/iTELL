import sqlite3
import sys

dbfile = "lcc.db"
con = sqlite3.connect(dbfile)
curs = con.cursor()

f = open('lcc.sql', 'r')
curs.executescript(f.read())

con.commit()
con.close()
