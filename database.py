# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 22:50:33 2022
tablo database olustur
@author: hasan
"""
import sys
from sqliteconnect import conSqlite




# =============================================================================
# connect = conSqlite("vapros.db")
# =============================================================================
# =============================================================================
# connect = conSqlite("vapros.db")
# con = connect.get_database_connection()
# cursor = con.cursor()
# cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
# print("tablolar:",cursor.fetchall())
# sys.exit('Ok')
# =============================================================================
# =============================================================================
# res=con.opendb()
# print('Db varmi:',res)
# =============================================================================
#con = connect.get_database_connection()

# =============================================================================
# =============================================================================
connect = conSqlite("vapros.db")
# con =connect.get_database_connection()
# cursor = con.cursor()
# #dropTableStatement = "DROP TABLE options"
# # 
# res=cursor.execute(dropTableStatement)
# 
# =============================================================================
#connect.create_tableVapros()
connect.create_tableOptions()
#print("res:",res)
sys.exit('Ok')
# =============================================================================


# =============================================================================
#con.create_tableVapros()
# =============================================================================
# connect = conSqlite("vapros.db")
# connect.create_tableVapros()
# #connect.create_tableOptions()
# # 
# print(connect)
# sys.exit('Ok')
# =============================================================================
# =============================================================================
# =============================================================================
# con = con.get_database_connection()
# cursor = con.cursor()
# cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
# print("tablolar:",cursor.fetchall())
# 
# =============================================================================

