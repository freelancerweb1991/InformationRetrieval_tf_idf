import datetime 
import dataProvider as dataProvider
import nltk
import re
import numpy as np   
import pandas as pd
import tokenizer as tokenizer 
from termcolor import colored
from math import sqrt
 
def tokenizeSearchQuery(query):
    startTime = datetime.datetime.now()
    stop_words = set(nltk.corpus.stopwords.words('english'))
    lemmatizer = nltk.stem.WordNetLemmatizer()
    ps = nltk.stem.PorterStemmer()
    cmnt = re.sub('[^a-zA-Z]',' ',query) 
    allTokens = [word.lower() for word in nltk.word_tokenize(cmnt)]
    filteredTokens = [word for word in allTokens if not word in stop_words]
    lemmatizedTokens = [lemmatizer.lemmatize(word) for word in filteredTokens]
    stemmedTokens = [ps.stem(word) for word in lemmatizedTokens]
    print('query tokenize time:',datetime.datetime.now() - startTime)

    freq = []
    terms = []
    for i in stemmedTokens:
        freq.append((i,1))
        if(i not in terms):
            terms.append(i)


    df = pd.DataFrame(freq, columns=['term','tf'])
    df = df.groupby(['term'], as_index= True, sort= True).count()
    df['tf-wt'] = 1 + np.log10(df['tf']) 
      
    print(colored('-------------------------------', 'cyan'))
    print(colored('inital query matrix:  (tf-wt) = 1+log(tf)', 'cyan'))
    print(colored('-------------------------------', 'cyan'))
    print(df)
     
    #print('\n' * 2)
     
    tfidf = tokenizer.getDocsMatrix(terms)
    totalDocsount =  tfidf[0]
    termsDocFreq =  tfidf[1]
    normalizedDocsMatrix =  tfidf[2]
    allDocs =  tfidf[3]
    print(colored('-------------------------------', 'blue')) 

    df['idf'] = termsDocFreq
    df['wt'] = (df['tf-wt']*termsDocFreq).fillna(0)
     
    df['wt'] = df['wt'] / sqrt((df['wt']*df['wt']).sum())
    normQueryVector = df['wt']
    print(colored('-------------------------------', 'cyan'))
    print(colored('Normalized query vector:', 'cyan'))
    print(colored('-------------------------------', 'cyan'))
    print(df)

    for doc in allDocs:
        normalizedDocsMatrix[doc] = normalizedDocsMatrix[doc] * normQueryVector 

    """ for idx in normQueryVector.sort_index():
        normalizedDocsMatrix[idx] = normalizedDocsMatrix[idx] * normQueryVector[idx] """

    cosinVectors = normalizedDocsMatrix #*normQueryVector
    print(colored('-------------------------------', 'cyan'))
    print(colored('effect of query vector on docs vector to calculate cosinuse similarity:', 'cyan'))
    print(colored('-------------------------------', 'cyan'))
    print(normalizedDocsMatrix)

    
    allcosinSimilaryRanks = []
    for doc in allDocs:
        allcosinSimilaryRanks.append((doc, normalizedDocsMatrix[doc].sum())) 
    df = pd.DataFrame(allcosinSimilaryRanks, columns=['docId', 'score']) 
    df = df.sort_values('score', ascending= False)
    
    #cosinVectors = normalizedDocsMatrix.groupby(['docId'], as_index= True).sum()
    print(colored('-------------------------------', 'cyan'))
    print(colored('all cosinuse similarity score:', 'cyan'))
    print(colored('-------------------------------', 'cyan'))
    print(df)

    result = df.nlargest(21, ['score'])
    print(colored('-------------------------------', 'cyan'))
    print(colored('Top 20 cosinuse similarity score:', 'cyan'))
    print(colored('-------------------------------', 'cyan'))
    print(result)

    print('-----------------------------------------------------------------------')

    docList = []  
    for ind in result.index:
        docId = result['docId'][ind]
        score = result['score'][ind]
        cmnt = dataProvider.getComment(docId, terms)
        hotelId =  cmnt[0]
        comment = tokenizer.getText(cmnt[1],terms,5)
        date =cmnt[2]
        docList.append((score, hotelId, comment, date))
        print(colored('-------------------------------', 'cyan'))
        print(colored(score, 'cyan'), '    ', colored(date, 'cyan'))
        print(colored('-------------------------------', 'cyan'))
        print(comment)
        print('********************************************')
       
    print(colored('-------------------------------', 'cyan'))
    print(colored('search result order by score:', 'cyan'))
    print(colored('-------------------------------', 'cyan'))
    #print(docList)

    return {word: stemmedTokens.count(word) for word in set(stemmedTokens)}

 