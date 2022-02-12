from fileinput import filename
import os
import sqlite3
import nltk
import math 
import dataProvider as dataProvider 
import tokenizer as tokenizer 
 


#dataProvider.initializeDataBase()  
#dataProvider.storeFilesOnDatabase()

#tokenizer.initializeDataBaseRI()
#tokenizer.tokenizeComents()
#tokenizer.getTerms(bool(1))

tokenizer.updateTokens1('''area''')
tokenizer.updateTokens1('area')
  

      
"""    

hotel_list = []
for fileName in os.listdir(dataPath):
    country = fileName.split('_')[1]
    city = fileName.split('_')[2]
    hotelName = fileName.split('_')[3]
    hotel_list.__add__({country, city, hotelName})
   # cur.execute('INSERT INTO hotels VALUES (:country, :city , :hotelName)', {'country': country, 'city':city, 'hotelName': hotelName})
    
cur.executemany('INSERT INTO hotels VALUES (?,?)', hotel_list)    

for fileName in os.listdir(dataPath):
    with open(os.path.join(f'{dataPath}{fileName}')) as f:
        cn = f.read()
        content = [word.lower() for word in nltk.word_tokenize(cn)]
        freq = {word: content.count(word) for word in set(content)}
        corpus[fileName] = freq
        print (corpus)
        print ('**')

for fileName in corpus:
    corpus[fileName] = sorted(corpus[fileName].items(), key= lambda x : x[1])
"""

