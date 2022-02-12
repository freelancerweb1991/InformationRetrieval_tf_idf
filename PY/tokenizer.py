import datetime
from fileinput import filename
import sqlite3   
import dataProvider as dataProvider
import nltk
import re


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

    for comment in dataProvider.getComments():
        cmnt = re.sub('[^a-zA-Z]',' ',comment[3]) 
        allTokens = [word.lower() for word in nltk.word_tokenize(cmnt)]
        filteredTokens = [word for word in allTokens if not word in stop_words]
        lemmatizedTokens = [lemmatizer.lemmatize(word) for word in filteredTokens]
        stemmedTokens = [ps.stem(word) for word in lemmatizedTokens]
        
        """ for i in filteredTokens:
            print(i) """
        freq = {word: stemmedTokens.count(word) for word in set(stemmedTokens)}
        print('document.id=', comment[0], ':')
        print(freq)

        updateTokens(comment[0], freq)  

        print ('** allTokens:',allTokens.__len__(),' ** after deleting stop words filteredTokens:', filteredTokens.__len__(), ' --', lemmatizedTokens.__len__(), ' --', stemmedTokens.__len__())

    
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

def updateTokens1(term):
    conn = sqlite3.connect(dbPathRI)
    cur = conn.cursor()
    frmtupdt= ',{}:{}'
    cur.execute('SELECT count(1) FROM terms WHERE token == ?',(term,))
    isExisted = cur.fetchone()[0]
    if(isExisted > 0):
        print('update .......') 
    else:
        print('insert .......') 
    conn.commit()
    cur.close()



