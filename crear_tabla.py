#!/usr/bin/python3

import sqlite3

conn = sqlite3.connect('fi.db')
print ("Opened database successfully");

conn.execute("DROP TABLE IF EXISTS TUTORIAS")

conn.execute('''CREATE TABLE TUTORIAS
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         USER           TEXT     NOT NULL,
         EMAIL          TEXT     NOT NULL,
         PASSWORD       TEXT     NOT NULL,
         IMAGEN		TEXT	NULL,
	 IS_ADMIN		BOOLEAN NOT NULL DEFAULT 0);''')
print ("Table created successfully");

conn.close()
