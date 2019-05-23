CREATE TABLE sex_with_me (
       id INTEGER PRIMARY KEY,
       prompt TEXT,
       answer TEXT,
       seconds REAL, 
       language TEXT,
       username TEXT,
       timestamp TEXT
);

CREATE TABLE sex_with_me_feedback (
       id INTEGER PRIMARY KEY,
       answer TEXT,
       sex_with_me_id INTEGER,
       feedback TEXT,
       seconds REAL, 
       language TEXT,
       username TEXT,
       timestamp TEXT
);

CREATE TABLE wicked_proverbs (
       id INTEGER PRIMARY KEY,
       frame TEXT,
       w1 TEXT,
       w2 TEXT,
       proverb TEXT,
       explanation TEXT,
       seconds REAL, 
       language TEXT,
       username TEXT,
       timestamp TEXT
);

CREATE TABLE haiku_on_demand (
       id INTEGER PRIMARY KEY,
       title TEXT,
       l1 TEXT,
       l2 TEXT,
       l3 TEXT,
       seconds REAL, 
       language TEXT,
       username TEXT,
       timestamp TEXT
);


CREATE TABLE haiku_on_demand_feedback (
       id INTEGER PRIMARY KEY,
       title TEXT,
       feedback TEXT,
       l1 TEXT,
       l2 TEXT,
       l3 TEXT,
       s1 INTEGER,
       s2 INTEGER,
       s3 INTEGER,
       seconds REAL, 
       language TEXT,
       username TEXT,
       timestamp TEXT
);
