from fileinput import filename
import os
import sqlite3
import nltk
import math 
import dataProvider as dataProvider 
import tokenizer as tokenizer 
import searchEngine as searchEngine 
  

#dataProvider.initializeDataBase()  
#dataProvider.storeFilesOnDatabase()
 

#tokenizer.initializeDataBaseRI()
#tokenizer.tokenizeComents()
#tokenizer.getTermsSummary(bool(1))

#tokenizer.getTerms(bool(1))

query = 'what is best hotel meriland area best of area'
qur = searchEngine.tokenizeSearchQuery(query)
 

#searchEngine.printQueryVector()
 
""" N = tokenizer.getTotalDocsCount(qur) 
print(N) """
 
 

