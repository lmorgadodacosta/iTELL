import sqlite3
import sys

dbfile = "ntucleX.db"
con = sqlite3.connect(dbfile)
curs = con.cursor()

f = open('lcc.sql', 'r')
curs.executescript(f.read())

con.commit()
con.close()
