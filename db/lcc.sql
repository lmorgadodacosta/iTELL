CREATE TABLE meta (
       title TEXT
       ,license TEXT
, lang, version, master);
CREATE TABLE corpus (
       corpusID INTEGER PRIMARY KEY
       ,corpus TEXT
       ,title TEXT
       ,language TEXT
);
CREATE TABLE doc (
       docid INTEGER PRIMARY KEY
       ,doc TEXT
       ,title TEXT
       ,url TEXT
       ,subtitle TEXT
       ,corpusID INTEGER
       ,FOREIGN KEY (corpusID) REFERENCES corpus(corpusID)
);
CREATE TABLE sent (
       sid INTEGER PRIMARY KEY
       ,docID INTEGER
       ,pid TEXT
       ,sent TEXT
       ,comment TEXT
       , usrname TEXT,FOREIGN KEY(docID) REFERENCES doc(docID)
);
CREATE TABLE stype (
       sid INTEGER
       ,stype INTEGER
       ,FOREIGN KEY(sid) REFERENCES sent(sid)
);
CREATE TABLE concept (
sid INTEGER
,cid INTEGER
,clemma TEXT
,tag TEXT
,tags TEXT
,comment TEXT
,ntag TEXT
, usrname TEXT,PRIMARY KEY (sid, cid)
        ,FOREIGN KEY(sid) REFERENCES sent(sid)
);
CREATE TABLE cwl (
       sid INTEGER,
       wid INTEGER,
       cid INTEGER
, usrname TEXT);
CREATE TABLE word (
sid INTEGER,
wid INTEGER,
word TEXT,
pos TEXT,
lemma TEXT,
cfrom INTEGER,
cto INTEGER,
comment TEXT, usrname TEXT,
        PRIMARY KEY (sid, wid),
        FOREIGN KEY(sid) REFERENCES sent(sid)
);
CREATE TABLE cwl_log (sid_new INTEGER, sid_old INTEGER,
                             wid_new INTEGER, wid_old INTEGER,
                             cid_new INTEGER, cid_old INTEGER,
                             usrname_new TEXT, usrname_old TEXT,
                             date_update DATE);
CREATE TABLE concept_log (sid_new INTEGER, sid_old INTEGER,
                                 cid_new INTEGER, cid_old INTEGER,
                                 clemma_new TEXT, clemma_old TEXT,
                                 tag_new TEXT, tag_old TEXT,
                                 tags_new TEXT, tags_old TEXT,
                                 comment_new TEXT, comment_old TEXT,
                                 ntag_new TEXT, ntag_old TEXT,
                                 usrname_new TEXT, usrname_old TEXT,
                                 date_update DATE);
CREATE TABLE sent_log (sid_new INTEGER, sid_old INTEGER,
                              docID_new INTEGER, docID_old INTEGER,
                              pid_new INTEGER, pid_old INTEGER,
                              sent_new INTEGER, sent_old INTEGER,
                              comment_new INTEGER, comment_old INTEGER,
                              usrname_new TEXT, usrname_old TEXT,
                              date_update DATE);
CREATE TABLE word_log (sid_new INTEGER, sid_old INTEGER,
                              wid_new INTEGER, wid_old INTEGER,
                              word_new TEXT, word_old TEXT,
                              pos_new TEXT, pos_old TEXT,
                              lemma_new TEXT, lemma_old TEXT,
                              cfrom_new INTEGER, cfrom_old INTEGER,
                              cto_new INTEGER, cto_old INTEGER,
                              comment_new INTEGER, comment_old INTEGER,
                              usrname_new TEXT, usrname_old TEXT,
                              date_update DATE);
CREATE TABLE sentiment
                 (sid INTEGER, cid INTEGER, score FLOAT,
                  username TEXT, PRIMARY KEY (sid, cid),
                 FOREIGN KEY(sid) REFERENCES sent(sid),
                 FOREIGN KEY(cid) REFERENCES concept(cid));
CREATE TABLE sentiment_log
                 (sid_new INTEGER, sid_old INTEGER, 
                  cid_new INTEGER, cid_old INTEGER, 
                  score_new FLOAT, score_old FLOAT,
                  username_new TEXT, username_old TEXT,
                  date_update DATE);
CREATE TABLE chunks
                 (sid INTEGER, xid INTEGER, score FLOAT,
                  comment TEXT, username TEXT, 
                 PRIMARY KEY (sid, xid),
                 FOREIGN KEY(sid) REFERENCES sent(sid));
CREATE TABLE chunk_log
                 (sid_new INTEGER, sid_old INTEGER,
                  xid_new INTEGER, xid_old INTEGER,
                  score_new FLOAT, score_old FLOAT,
                  comment_new TEXT, comment_old TEXT,
                  username_new TEXT, username_old TEXT,
                  date_update DATE);
CREATE TABLE xwl
                 (sid INTEGER, wid INTEGER, xid INTEGER,
                  username TEXT, PRIMARY KEY (sid, wid, xid),
                 FOREIGN KEY(sid) REFERENCES sent(sid),
                 FOREIGN KEY(wid) REFERENCES word(wid),
                 FOREIGN KEY(xid) REFERENCES chunks(xid));
CREATE TABLE xwl_log
                 (sid_new INTEGER, sid_old INTEGER,
                  wid_new INTEGER, wid_old INTEGER,
                  xid_new INTEGER, xid_old INTEGER,
                  username_new TEXT, username_old TEXT,
                  date_update DATE);
CREATE INDEX concept_cid ON concept (cid);
CREATE INDEX concept_sid ON concept (sid);
CREATE INDEX concept_clemma ON concept (clemma);
CREATE INDEX cwl_sid ON cwl (sid);
CREATE INDEX cwl_cid ON cwl (cid);
CREATE INDEX word_sid ON word (sid);
CREATE TRIGGER update_cwl_log AFTER UPDATE ON cwl
    BEGIN
    INSERT INTO cwl_log (sid_new, sid_old,
                         wid_new, wid_old,
                         cid_new, cid_old,
                         usrname_new, usrname_old,
                         date_update)
    VALUES (new.sid, old.sid, 
            new.wid, old.wid,
            new.cid, old.cid, 
            new.usrname, old.usrname,
            DATETIME('NOW'));
    END;
CREATE TRIGGER insert_cwl_log AFTER INSERT ON cwl
    BEGIN
    INSERT INTO cwl_log  (sid_new,
                          wid_new,
                          cid_new,
                          usrname_new,
                          date_update)
    VALUES (new.sid, 
            new.wid, 
            new.cid,
            new.usrname, 
            DATETIME('NOW'));
    END;
CREATE TRIGGER delete_cwl_log AFTER DELETE ON cwl
    BEGIN
    INSERT INTO cwl_log  (sid_old,
                          wid_old,
                          cid_old,
                          usrname_old,
                          date_update)
    VALUES (old.sid, 
            old.wid, 
            old.cid,
            old.usrname,
            DATETIME('NOW'));
    END;
CREATE TRIGGER update_concept_log AFTER UPDATE ON concept
    BEGIN
    INSERT INTO concept_log  (sid_new, sid_old,
                              cid_new, cid_old,
                              clemma_new, clemma_old,
                              tag_new, tag_old,
                              tags_new, tags_old,
                              comment_new, comment_old,
                              ntag_new, ntag_old,
                              usrname_new, usrname_old,
                              date_update)
    VALUES (new.sid, old.sid,
            new.cid, old.cid,
            new.clemma, old.clemma,
            new.tag, old.tag,
            new.tags, old.tags,
            new.comment, old.comment,
            new.ntag, old.ntag,
            new.usrname, old.usrname,
            DATETIME('NOW'));
    END;
CREATE TRIGGER insert_concept_log AFTER INSERT ON concept
    BEGIN
    INSERT INTO concept_log  (sid_new,
                              cid_new,
                              clemma_new,
                              tag_new,
                              tags_new,
                              comment_new,
                              ntag_new,
                              usrname_new,
                              date_update)
    VALUES (new.sid,
            new.cid,
            new.clemma,
            new.tag,
            new.tags,
            new.comment,
            new.ntag,
            new.usrname,
            DATETIME('NOW'));
    END;
CREATE TRIGGER delete_concept_log AFTER DELETE ON concept
    BEGIN
    INSERT INTO concept_log  (sid_old,
                              cid_old,
                              clemma_old,
                              tag_old,
                              tags_old,
                              comment_old,
                              ntag_old,
                              usrname_old,
                              date_update)
    VALUES (old.sid,
            old.cid,
            old.clemma,
            old.tag,
            old.tags,
            old.comment,
            old.ntag,
            old.usrname,
            DATETIME('NOW'));
    END;
CREATE TRIGGER update_sent_log AFTER UPDATE ON sent
    BEGIN
    INSERT INTO sent_log (sid_new, sid_old,
                          docID_new, docID_old,
                          pid_new, pid_old,
                          sent_new, sent_old,
                          comment_new, comment_old,
                          usrname_new, usrname_old,
                          date_update)
    VALUES (new.sid, old.sid, 
            new.docID, old.docID,
            new.pid, old.pid,
            new.sent, old.sent, 
            new.comment, old.comment, 
            new.usrname, old.usrname,
            DATETIME('NOW'));
    END;
CREATE TRIGGER insert_sent_log AFTER INSERT ON sent
    BEGIN
    INSERT INTO sent_log  (sid_new,
                          docID_new,
                          pid_new,
                          sent_new,
                          comment_new,
                          usrname_new,
                          date_update)
    VALUES (new.sid,
            new.docID,
            new.pid,
            new.sent,
            new.comment,
            new.usrname,
            DATETIME('NOW'));
    END;
CREATE TRIGGER delete_sent_log AFTER DELETE ON sent
    BEGIN
    INSERT INTO sent_log  (sid_old,
                          docID_old,
                          pid_old,
                          sent_old,
                          comment_old,
                          usrname_old,
                          date_update)
    VALUES (old.sid, 
            old.docID,
            old.pid,
            old.sent, 
            old.comment, 
            old.usrname,
            DATETIME('NOW'));
    END;
CREATE TRIGGER update_word_log AFTER UPDATE ON word
    BEGIN
    INSERT INTO word_log (sid_new, sid_old,
                          wid_new, wid_old,
                          word_new, word_old,
                          pos_new, pos_old,
                          lemma_new, lemma_old,
                          cfrom_new, cfrom_old,
                          cto_new, cto_old,
                          comment_new, comment_old,
                          usrname_new, usrname_old,
                          date_update)
    VALUES (new.sid, old.sid, 
            new.wid, old.wid,
            new.word, old.word,
            new.pos, old.pos,
            new.lemma, old.lemma,
            new.cfrom, old.cfrom,
            new.cto, old.cto,
            new.comment, old.comment, 
            new.usrname, old.usrname,
            DATETIME('NOW'));
    END;
CREATE TRIGGER insert_word_log AFTER INSERT ON word
    BEGIN
    INSERT INTO word_log  (sid_new,
                           wid_new,
                           word_new,
                           pos_new,
                           lemma_new,
                           cfrom_new,
                           cto_new,
                           comment_new,
                           usrname_new,
                           date_update)
    VALUES (new.sid,
            new.wid,
            new.word, 
            new.pos,
            new.lemma, 
            new.cfrom, 
            new.cto, 
            new.comment, 
            new.usrname,
            DATETIME('NOW'));
    END;
CREATE TRIGGER delete_word_log AFTER DELETE ON word
    BEGIN
    INSERT INTO word_log (sid_old,
                          wid_old,
                          word_old,
                          pos_old,
                          lemma_old,
                          cfrom_old,
                          cto_old,
                          comment_old,
                          usrname_old,
                          date_update)
    VALUES (old.sid, 
            old.wid,
            old.word,
            old.pos,
            old.lemma,
            old.cfrom,
            old.cto,
            old.comment, 
            old.usrname,
            DATETIME('NOW'));
    END;
CREATE TRIGGER delete_sentiment_log
                 AFTER DELETE ON sentiment
                 BEGIN
                 INSERT INTO sentiment_log (sid_old,
                                            cid_old,
                                            score_old,
                                            username_old,
                                            date_update)
                 VALUES (old.sid,
                         old.cid,
                         old.score,
                         old.username,
                         DATETIME('NOW'));
                 END;
CREATE TRIGGER insert_sentiment_log
                 AFTER INSERT ON sentiment
                 BEGIN
                 INSERT INTO sentiment_log (sid_new,
                                            cid_new,
                                            score_new,
                                            username_new,
                                            date_update) 
                 VALUES (new.sid,
                         new.cid,
                         new.score,
                         new.username,
                         DATETIME('NOW'));
                 END;
		 
CREATE TABLE error
                 (sid INTEGER, eid INTEGER, label TEXT,
                  comment TEXT, username TEXT, 
                 PRIMARY KEY (sid, eid),
                 FOREIGN KEY(sid) REFERENCES sent(sid));
CREATE TABLE error_log
                 (sid_new INTEGER, sid_old INTEGER,
                  eid_new INTEGER, eid_old INTEGER,
                  label_new TEXT, label_old TEXT,
                  comment_new TEXT, comment_old TEXT,
                  username_new TEXT, username_old TEXT,
                  date_update DATE);
CREATE TABLE ewl
                 (sid INTEGER, wid INTEGER, eid INTEGER,
                  username TEXT, PRIMARY KEY (sid, wid, eid),
                 FOREIGN KEY(sid) REFERENCES sent(sid),
                 FOREIGN KEY(wid) REFERENCES word(wid),
                 FOREIGN KEY(eid) REFERENCES error(eid));
CREATE TABLE ewl_log
                 (sid_new INTEGER, sid_old INTEGER,
                  wid_new INTEGER, wid_old INTEGER,
                  eid_new INTEGER, eid_old INTEGER,
                  username_new TEXT, username_old TEXT,
                  date_update DATE);
