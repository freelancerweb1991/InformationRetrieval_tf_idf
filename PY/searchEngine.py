import datetime
from distutils.log import info
from fileinput import filename
import sqlite3   
import dataProvider as dataProvider
import nltk
import re  

query = 'what is best hotel'


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
    return {word: stemmedTokens.count(word) for word in set(stemmedTokens)}


"""  
def cosine_similarity_T(k, tokens):
    q_df = pd.DataFrame(columns=['q_clean'])
    q_df.loc[0,'q_clean'] =tokens 
    d_cosines = []
    
    query_vector = gen_vector_T(q_df['q_clean'])
    for d in tfidf_tran.A:
        d_cosines.append(cosine_sim(query_vector, d))
                    
    out = np.array(d_cosines).argsort()[-k:][::-1]
    #print("")
    d_cosines.sort()
    a = pd.DataFrame()
    for i,index in enumerate(out):
        a.loc[i,'index'] = str(index)
        a.loc[i,'Subject'] = df_news['Subject'][index]
    for j,simScore in enumerate(d_cosines[-k:][::-1]):
        a.loc[j,'Score'] = simScore
    return a

def gen_vector_T(tokens):
    Q = np.zeros(20000)    
    x= tfidf.transform(tokens)
    #print(tokens[0].split(','))
    for token in tokens[0].split(','):
        #print(token)
        try:
            ind = vocabulary.index(token)
            Q[ind]  = x[0, tfidf.vocabulary_[token]]
        except:
            pass
    return Q
            
def cosine_sim(a, b):
    cos_sim = np.dot(a, b)/(np.linalg.norm(a)*np.linalg.norm(b))
    return cos_sim
 """
""" tokens = tokenizeSearchQuery(query)
ids = tokenizer.getTotalDocsIds(tokens)
comments = dataProvider.getFilteredComments(ids)

## Create Vocabulary
vocabulary = set()
for doc in comments:
    vocabulary.update(doc.split(','))
vocabulary = list(vocabulary)
# Intializating the tfIdf model
tfidf = TfidfVectorizer(vocabulary=vocabulary)
# Fit the TfIdf model
tfidf.fit(comments)
# Transform the TfIdf model
tfidf_tran=tfidf.transform(comments) """

