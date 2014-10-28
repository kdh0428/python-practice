#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import MySQLdb

chat_db = MySQLdb.connect(host="localhost",db="lighttpdDB",user="lighttpd",passwd="1234")

chat_cursor = chat_db.cursor()

while True:
    Chat = sys.stdin.read(1024)
    
    if not Chat:
        break
    User_Name = Chat.split()[0]
    User_Chat = Chat.split()[1]
    try:
        chat_cursor.execute("INSERT INTO chat(USER_NAME,USER_CHAT) VALUES('%s','%s');" % (User_Name,User_Chat))
        chat_db.commit()
    except:
        chat_db.rollback()

    
