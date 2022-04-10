# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 00:39:41 2022

@author: hasan
"""

import sys
import os
from sqliteconnect import conSqlite
from datetime import date


class Options:
    pass



    def addSoru(self,soru,ders,date,sira):
      

        soruSira= "\nSoruno:#" +str(sira)
        print("soru:",soru)
        satir= soruSira+" \n\n"+soru+" \n"
        file_object = open( 'C:/denemeler/'+ders+'.txt' , 'a' )
        file_object.write(satir)
        file_object.close()
       # return soruId
        
    def setOption(self,ders,option,insertdate,correct):
       # soruId=str(soruId)
        option=str(option)
      #  optionName=str(optionName)
        insertdate=str(insertdate)
        print("option:",option,"correct:",correct)
        file_object = open( 'C:/denemeler/'+ders+'.txt' , 'a' )
        file_object.write(option+" "+correct+"\n")
        file_object.close()

 
       
        
    def addOptions(self,ders,siklar,today):
  
    
        for siktr in siklar:
            
            correct=''
            option=siktr.text.strip()
            
        
            if option != "Boş":
                optionName = option[0]
                dogruMu= siktr.find("td", { "class" : "span2" }).find("div", { "class" : "text-center" }).find("i", { "class" : "icon-ok green" })
                if(dogruMu!=None):
                    #dogru= optionName
                    correct= "#(Dogru)"                    
             
              
                self.setOption(ders,option, today, correct)
                print(option)
               #<i class="icon-ok green"></i>
           
      
      

            
       