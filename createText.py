# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 22:34:51 2022

@author: hasan
"""
import sys
import os
from datetime import datetime

class conSqlite():
    
    DB_NAME = None
    
    def __init__(self,db):
       self.DB_NAME = db
       
       
    def opendb(self):
        try:
            result= os.path.isfile(self.DB_NAME)
            if(result == True):
                return True
            else:
                return False
        except sqlite3.Error:
            print("Error open db.\n")
            return False
            cur = conn.cursor()
            print("Error open db.\n")
            return [conn, cur]
    
        
    def get_database_connection(self):
       con = ""
           
       return con
        
    
    
    def create_tableVapros(self):
        """
        Creates a table ready to accept our data.        
        write code that will execute the given sql statement
        on the database
        """
        
        create_table = """ CREATE TABLE sorular(
        soruId INTEGER PRIMARY KEY AUTOINCREMENT,
        soru TEXT NOT NULL,
        ders TEXT NOT NULL,
        cevapId INTEGER NULL,
        optionName Char NULL,
        date CHAR(15) NOT NULL
        )
        """
        
       
    def create_tableOptions(self):
        
        create_table = """ CREATE TABLE options(
        optionId INTEGER PRIMARY KEY AUTOINCREMENT,
        soruId INTEGER NOT NULL,
        option TEXT NOT NULL,
        optionName TEXT NOT NULL,
        correct TEXT NULL,
        date CHAR(15) NOT NULL
        )
        """
        
   

    def addSoru(self,soru,ders,date):

        add_data_stmt = ''' INSERT INTO sorular(soru,ders,date) VALUES(?,?,?) '''
        
# =============================================================================
#         con = self.get_database_connection()
#         con.executemany(add_data_stmt, contract_list)
#         con.commit()
#         con.close()
# =============================================================================
        con = self.get_database_connection()       
        cursor=con.cursor()

        cursor.execute('INSERT INTO sorular(soru,ders,date) VALUES(?,?,?)', (soru,ders,date))
       # con.commit()
        soruId=cursor.lastrowid
        #soruId=con.lastrowid
       
        print("soru:",soru)
        file_object = open( 'C:/denemeler/inkilapTarihi.txt' , 'a' )
        file_object.write(soru)
        file_object.close()
        return soruId
        
    def setOption(self,soruId,option,optionName,insertdate,correct):
        soruId=str(soruId)
        option=str(option)
        optionName=str(optionName)
        insertdate=str(insertdate)
        print(option,correct)
        file_object = open( 'C:/denemeler/inkilapTarihi.txt' , 'a' )
        file_object.write(option+" "+correct+"\n")
        file_object.close()
        #print(option,optionName,insertdate)
     
        veri= [soruId,option,optionName,insertdate,correct]
        #add_data_stmt = ''' INSERT INTO options(soruId,option,optionName,date) VALUES(?,?,?,?); '''
        
        con = self.get_database_connection()
        cursor=con.cursor()
        #cursor.executemany('INSERT INTO options(soruId,option,optionName,date) VALUES(?,?,?,?)',veri)
        #cursor.execute('INSERT INTO options(soruId,option,optionName,date) VALUES(?,?,?,?)',veri)
        con.execute('INSERT INTO options(soruId,option,optionName,date,correct) VALUES(?,?,?,?,?)',veri)
       # cursor.commit()
       # cursor.close()
        #con.close()
        return True
    
    
    def setClose(self):
        con = self.get_database_connection()       
        #cursor=con.cursor()
        #cursor.close()
        #cursor.commit()
        con.commit()
       
        con.close()