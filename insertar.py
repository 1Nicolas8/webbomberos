#!/usr/bin/python3

import sqlite3

conn = sqlite3.connect('fi.db')
print ("Opened database successfully");

conn.execute("INSERT INTO TUTORIAS (ID,NAME,USER,EMAIL,PASSWORD,IMAGEN, IS_ADMIN) \
      VALUES (41318517, 'Paul', 'lfeli99','lfeli99@gmail.com', '1234567',NULL, 0)");

conn.execute("INSERT INTO TUTORIAS (ID,NAME,USER,EMAIL,PASSWORD,IMAGEN, IS_ADMIN) \
      VALUES (1, 'Admin', 'admin','admin@gmail.com','admin',NULL, 1)");

conn.commit()
print ("Records created successfully");
conn.close()

