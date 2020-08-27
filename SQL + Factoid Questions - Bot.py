# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 17:49:35 2020

@author: Nithin
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 12:59:57 2020

@author: Nithin
"""

import pymysql as sql
import pandas as pd
from pandas import DataFrame, Series
import pandas as pd
import numpy as np
import pickle
import operator
import random
import nltk
from DocumentRetrievalModel import DocumentRetrievalModel as DRM
from ProcessedQuestion import ProcessedQuestion as PQ
import re
import sys



db = sql.connect("localhost","root","root","im" )
cursor = db.cursor()


flag = False

while flag!=True:
    print("Welcome")
    print("Please choose the service")
    print('''
      Type 1 for FAQ
      Type 2 to check the status
      ''')
    choice=int(input("Enter your choice: "))

    if(choice==2):
    
        No=int(input("Enter the Employee No: "))

        sql="select * from Employee where empno='%d'" % (No)
        cursor.execute(sql)
        result=cursor.fetchall()
        for i in result:
            print(i)
        
        ans=input("Enter Q to quit or P to go back to Main Menu: ")
        if(ans.lower()=='q'):
            flag=True


    if(choice==1):

        datasetName = "dataset/Alloy.txt"
        # Loading Dataset
        try:
        	datasetFile = open(datasetName,"r")
        except FileNotFoundError:
        	print("Bot> Oops! I am unable to locate \"" + datasetName + "\"")
        	exit()
        
        # Retrieving paragraphs : Assumption is that each paragraph in dataset is
        # separated by new line character
        paragraphs = []
        for para in datasetFile.readlines():
        	if(len(para.strip()) > 0):
        		paragraphs.append(para.strip())
        
        # Processing Paragraphs
        drm = DRM(paragraphs,True,True)
        
        print("Bot> Hey! I am ready. Ask me factoid based questions only :P")
        print("Bot> You can say me Bye anytime you want")
        
        # Greet Pattern
        greetPattern = re.compile("^\ *((hi+)|((good\ )?morning|evening|afternoon)|(he((llo)|y+)))\ *$",re.IGNORECASE)
        
        isActive = True
        while isActive:
        	userQuery = input("You> ")
        	if(not len(userQuery)>0):
        		print("Bot> You need to ask something")
        
        	elif greetPattern.findall(userQuery):
        		response = "Hello!"
        	elif userQuery.strip().lower() == "bye":
        		response = "Bye Bye!"
        		isActive = False
                
        	else:
        		# Proocess Question
        		pq = PQ(userQuery,True,False,True)
        
        		# Get Response From Bot
        		response =drm.query(pq)
        	print("Bot>",response)        
            
        ans=input("Enter Q to quit or P to go back to Main Menu: ")
        if(ans.lower()=='q'):
            flag=True












