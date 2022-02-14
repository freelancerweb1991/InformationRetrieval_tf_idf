import datetime
from fileinput import filename
from math import sqrt
from operator import index
import sqlite3   
import dataProvider as dataProvider
import nltk
import re
import pandas as pd
import numpy as np 
import searchEngine as searchEngine 
from sklearn.preprocessing import Normalizer
from termcolor import colored


corpus = {}
dbPathRI = 'data\dataBaseRI.db'
def initializeDataBaseRI():
    conn = sqlite3.connect(dbPathRI)
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS terms (id INTEGER PRIMARY KEY AUTOINCREMENT, token TEXT, frequeny INTEGER, info TEXT)') 
    conn.commit()
    cur.close()

def tokenizeComents(): 
    startTime = datetime.datetime.now()
    print ('Creatin RI database start time:', startTime)
    stop_words = set(nltk.corpus.stopwords.words('english'))
    lemmatizer = nltk.stem.WordNetLemmatizer()
    ps = nltk.stem.PorterStemmer()

    allComments = dataProvider.getComments(bool(0))
    allCommentsCount = allComments.__len__()
    tokenizedCommentsCount = 0

    for comment in allComments:
        tokenizedCommentsCount+=1
        cmnt = re.sub('[^a-zA-Z]',' ',comment[3]) 
        allTokens = [word.lower() for word in nltk.word_tokenize(cmnt)]
        filteredTokens = [word for word in allTokens if not word in stop_words]
        lemmatizedTokens = [lemmatizer.lemmatize(word) for word in filteredTokens]
        stemmedTokens = [ps.stem(word) for word in lemmatizedTokens]

        df = pd.DataFrame(stemmedTokens, columns=['term','count']) 
        grouped = df.groupby(['term'], as_index= False).count()
        print(grouped)
        
        #freq = {word: stemmedTokens.count(word) for word in set(stemmedTokens)}

        #updateTokens(comment[0], freq)  

        """ print ('** allTokens:',allTokens.__len__(),' ** after deleting stop words filteredTokens:', filteredTokens.__len__(), ' --', lemmatizedTokens.__len__(), ' --', stemmedTokens.__len__()) """
        if(tokenizedCommentsCount%1000 == 0):
            print('commects tokenize:', tokenizedCommentsCount/allCommentsCount*100) 

    endTime = datetime.datetime.now()
    print('complete creating RI database:', endTime)
    print('Total duration:', endTime - startTime)    

def updateTokens(docId, terms):
    conn = sqlite3.connect(dbPathRI)
    cur = conn.cursor()
    for term in terms:
        frmtupdt= ',{}:{}'
        cur.execute('SELECT count(1) FROM terms WHERE token = ?', [term])
        isExisted = cur.fetchone()[0]
        if(isExisted > 0):
            cur.execute('UPDATE terms SET info = info || ? where token= ?  ', (frmtupdt.format(docId, terms[term]), term)) 
        else:
            frmtupdt= '{}:{}'
            cur.execute('INSERT INTO terms (info, token) VALUES (?, ?)', (frmtupdt.format(docId, terms[term]), term))
    conn.commit()
    cur.close()

def getTerms(isPrintResult):
    conn = sqlite3.connect(dbPathRI)
    cur = conn.cursor()
    cur.execute('SELECT id, token, info FROM terms order by token')
    rows = cur.fetchall()

    if(isPrintResult):
        for row in rows:
            print(row)
        if(rows.__len__() == 0):
            print ('terms is empty table.')

    conn.commit()
    cur.close()
    return rows

    
def getTermsSummary(isPrintResult):
    conn = sqlite3.connect(dbPathRI)
    cur = conn.cursor()
    cur.execute('SELECT count(id) FROM terms order by token')
    rows = cur.fetchall()

    if(isPrintResult):
        for row in rows:
            print(row)
        if(rows.__len__() == 0):
            print ('terms is empty table.')

    conn.commit()
    cur.close()
    return rows

def getTotalDocsCount(words):
    startTime = datetime.datetime.now()
    totalDocsount = 0
    allDocs = []
    wordsFreqs = []
    docFreqs = []
    conn = sqlite3.connect(dbPathRI)
    
    for word in words:
        cur = conn.cursor()
        cur.execute('SELECT info FROM terms WHERE token = ?', [word])
        rows = cur.fetchone()
        if(rows == None):
            continue
        docs = rows[0].split(',') 
        tf = docs.__len__()
        for doc in docs:
            docId = doc.split(':')[0]
            frq = doc.split(':')[1]
            if(not docId in allDocs):
                allDocs.append(docId)
            wordsFreqs.append((word, docId, frq ))
            docFreqs.append(word)
    totalDocsount = allDocs.__len__() 
    
    df = pd.DataFrame(wordsFreqs) 
    
    df
    #freq = {word[0]: wordsFreqs.count(word[1]) for word in set(wordsFreqs)}
     
    print('Total Docs Count calculation time:',datetime.datetime.now() - startTime) 
    return totalDocsount
    
def getTotalDocsIds(words):
    startTime = datetime.datetime.now() 
    allDocs = [] 
    conn = sqlite3.connect(dbPathRI) 
    for word in words:
        cur = conn.cursor()
        cur.execute('SELECT info FROM terms WHERE token = ?', [word])
        rows = cur.fetchone()
        if(rows == None):
            continue
        docs = rows[0].split(',') 
        tf = docs.__len__()
        for doc in docs:
            docId = doc.split(':')[0] 
            if(not docId in allDocs):
                allDocs.append(docId)  
     
    print('Total Docs Count calculation time:',datetime.datetime.now() - startTime) 
    return allDocs

def getDocsMatrix(terms): 
    startTime = datetime.datetime.now()
    totalDocsount = 0
    allDocs = []
    wordsFreqs = []
    docFreqs = []
    conn = sqlite3.connect(dbPathRI)

    for term in terms:
        cur = conn.cursor()
        cur.execute('SELECT info FROM terms WHERE token = ?', [term])
        rows = cur.fetchone()
        if(rows == None):
            continue
        docs = rows[0].split(',') 
        tf = docs.__len__()
        for doc in docs:
            docId = doc.split(':')[0]
            frq = doc.split(':')[1]
            if(not docId in allDocs):
                allDocs.append(docId)
            wordsFreqs.append((term, docId, frq ))
            docFreqs.append(term)
    totalDocsount = allDocs.__len__() 

    

    df = pd.DataFrame(wordsFreqs, columns=['term','docId','freq']) 
    grouped = df.groupby(['term'], as_index= True).count() 
     
    grouped['idf'] =  np.log10(totalDocsount/ grouped['freq'])  # add function to support smart coding
    #grouped['tf-raw'] = qur[grouped['term']] 
    #grouped['tf-wt'] = qur[grouped['term']] 
    termsDocFreq = grouped['idf']
    print(colored('-------------------------------', 'cyan'))
    print(colored('total commenct count:', 'cyan'), totalDocsount)
    print(colored('-------------------------------', 'cyan'))
    print(termsDocFreq) 

    weightedWordsFreqs = []
    for word in wordsFreqs:
        freq = int(word[2])
        wt = (1 + np.log10(freq)) # add function to support smart coding
        weightedWordsFreqs.append((word[0], word[1], wt))

    pv1 = df.pivot(index='term', columns='docId')['freq'].fillna(0) 
    
     
    print(colored('-------------------------------', 'magenta'))
    print(colored('Raw Frequency docs for terms:', 'magenta'), totalDocsount)
    print(colored('-------------------------------', 'magenta'))
    print(pv1)
    
    df = pd.DataFrame(weightedWordsFreqs, columns=['term','docId','freq'])
    pv = df.pivot(index='term', columns='docId')['freq'].fillna(0) 
    normalizedDocsMatrix = df.pivot(index='term', columns='docId')['freq'].fillna(0) 

    for doc in allDocs:
        normalizedDocsMatrix[doc] =  normalizedDocsMatrix[doc] / sqrt((normalizedDocsMatrix[doc]*normalizedDocsMatrix[doc]).sum())
    
    """ transformer = Normalizer().fit(df2)
    tt = transformer.transform(df2) """
    

    
    print(colored('-------------------------------', 'yellow'))
    print(colored('waited documents:', 'yellow'), totalDocsount)
    print(colored('-------------------------------', 'yellow'))
    print(pv)
    print(colored('-------------------------------', 'green'))
    print(colored('normalized documents:', 'green'), totalDocsount)
    print(colored('-------------------------------', 'green'))
    print(normalizedDocsMatrix)
    return (totalDocsount, termsDocFreq,normalizedDocsMatrix)
 
""" query = 'what is best hotel meriland area'
qur = searchEngine.tokenizeSearchQuery(query)
startTime = datetime.datetime.now()
totalDocsount = 0
allDocs = []
wordsFreqs = []
docFreqs = []
conn = sqlite3.connect(dbPathRI)

for word in qur:
    cur = conn.cursor()
    cur.execute('SELECT info FROM terms WHERE token = ?', [word])
    rows = cur.fetchone()
    if(rows == None):
        continue
    docs = rows[0].split(',') 
    tf = docs.__len__()
    for doc in docs:
        docId = doc.split(':')[0]
        frq = doc.split(':')[1]
        if(not docId in allDocs):
            allDocs.append(docId)
        wordsFreqs.append((word, docId, frq ))
        docFreqs.append(word)
totalDocsount = allDocs.__len__() 

df = pd.DataFrame(wordsFreqs, columns=['term','docId','freq']) 
grouped = df.groupby(['term'], as_index= True).count()
grouped['idf'] = (1+ np.log(1)) *  np.log(totalDocsount/ grouped['freq'])
#grouped['tf-raw'] = qur[grouped['term']] 
#grouped['tf-wt'] = qur[grouped['term']] 
 

print(grouped)
print('total commenct count:', totalDocsount) """



   