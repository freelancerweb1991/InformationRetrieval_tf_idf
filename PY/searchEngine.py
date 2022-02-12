import datetime
from fileinput import filename
import sqlite3   
import dataProvider as dataProvider
import nltk
import re

query = 'what is best hotel'



def tokenizeSearchQuery(query):
    stop_words = set(nltk.corpus.stopwords.words('english'))
    lemmatizer = nltk.stem.WordNetLemmatizer()
    ps = nltk.stem.PorterStemmer()
    cmnt = re.sub('[^a-zA-Z]',' ',query) 
    allTokens = [word.lower() for word in nltk.word_tokenize(cmnt)]
    filteredTokens = [word for word in allTokens if not word in stop_words]
    lemmatizedTokens = [lemmatizer.lemmatize(word) for word in filteredTokens]
    stemmedTokens = [ps.stem(word) for word in lemmatizedTokens]
    return {word: stemmedTokens.count(word) for word in set(stemmedTokens)}