# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 20:32:22 2022

@author: hasan
deneme sınavlari parser
"""
import sys
from bs4 import BeautifulSoup
from sqliteconnect import conSqlite
from options import Options
from datetime import date

#html = #the HTML code you've written above
path ="C:/denemeler"
#htmlfile = "Atatürk İlkeleri ve İnkılap Tarihi II --5.html"
#htmlfile = "14.html"
htmlfile = "tarih.html"
filepath = path+"/"+htmlfile
ders="Atatürk İlkeleri ve İnkılap Tarihi II"
today = date.today()
Sorular = []
sira =0
try: 
    html = open(path+'/'+htmlfile, encoding="utf8").read() 
except ImportError:
    sys.exit("BeautifulSoup modulü yüklenemedi")
    
else:    
    connector = conSqlite("vapros.db")
    
    #the HTML code you've written above
    parsed_html = BeautifulSoup(html, "lxml")
    objects=parsed_html.body.findAll('div', attrs={'class':'soru-report'})
    print("soru sayi:",len(objects))

    for row in objects:
        soruNo=row.div.div.div.text
      #  print("objects",row.text)
        #sys.exit()
        soru = row.find("div", { "class" : "portlet-body" }).find("h4").text
        if soru in Sorular:
            print('tekrar')
        else:   
            sira +=1
            Sorular.append(soru) 
            option = Options()    
            soruId= option.addSoru(soru,ders,today,sira)
            siklar = row.find("table").find('tbody').findAll("tr")
            #print(siklar)
               
            option.addOptions(ders,siklar,today)
   
     


        print("soru sayi:",sira)
        
       # print(Sorular)


    
 
    
    
    
    