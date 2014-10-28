#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb

chat_db = MySQLdb.connect(host="localhost",db="lighttpdDB",user="lighttpd",passwd="1234")

chat = chat_db.cursor()

if not chat.execute("SELECT * FROM chat"):
    print ""
    exit(0)

for chat_line in chat.fetchall():
    print "{0} :\n {1}\n".format(chat_line[0],chat_line[1])


