import os
import sqlite3  
 
dataPath = 'data\hotels\data'
dbPath = 'data\dataBase.db' 

# this function initialize database for store stracture data.
def initializeDataBase():
    conn = sqlite3.connect(dbPath)
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS hotels (id INTEGER PRIMARY KEY AUTOINCREMENT, city TEXT, name TEXT)')
    cur.execute('CREATE TABLE IF NOT EXISTS comments (id INTEGER PRIMARY KEY AUTOINCREMENT, hotelId INTEGER, date DATE, comment TEXT)')
    conn.commit()
    cur.close()

def storeFilesOnDatabase():
    totalHotelsCount = 0
    totalCommentsCount = 0
    conn = sqlite3.connect(dbPath)
    cur = conn.cursor()
    for fileName in os.walk(dataPath): 
            splitLength = fileName[0].split('\\').__len__()
            city = fileName[0].split('\\')[splitLength-1]   
            for file in fileName[2] :
                comments = []
                totalHotelsCount += 1
                hotelName = file.split(city,1)[1].replace('_',' ').strip().capitalize()
                cur.execute('INSERT INTO hotels (city, name) VALUES (?,?)', (city, hotelName))
                hotelId = cur.lastrowid 
                #print('**',city,'**','**', hotelName,'***************************** ',fileName[0],'/',file) 
                with open(os.path.join(f'{fileName[0]}/{file}')) as f:
                    cn = f.readlines()
                for line in cn: 
                    totalCommentsCount += 1
                    date = line.split('\t')[0]
                    comment = line.replace(date,'')
                    comments.append(( hotelId, date.strip(), comment.strip()))

                if(comments.__len__() > 0):
                    cur.executemany('INSERT INTO comments (hotelId, date, comment) VALUES (?,?,?)', comments)
                    
            
    print('# hotelsCount:', totalHotelsCount,' CommentsCount:', totalCommentsCount,'#########################################################################')
    conn.commit()
    cur.close()

def getHotels():
    conn = sqlite3.connect(dbPath)
    cur = conn.cursor()
    cur.execute('SELECT * FROM hotels') 
    rows = cur.fetchall()
    print('*** HOTELS ***********************************************************')
    for row in rows:
        print(row)
    conn.commit()
    cur.close()

def getHotelsCount():
    conn = sqlite3.connect(dbPath)
    cur = conn.cursor()
    cur.execute('SELECT count(1) FROM hotels')
    hotelsCount = cur.fetchone()[0]
    conn.commit()
    cur.close()
    return hotelsCount

def getComments():
    conn = sqlite3.connect(dbPath)
    cur = conn.cursor()
    cur.execute('SELECT * FROM comments') 
    rows = cur.fetchall()

    """  
    print('*** COMMENTS ***********************************************************') 
    for row in rows:
        print(row[0],'  ',row[1],'  ', row[2],'  ', row[3][:75])  
    """
    
    conn.commit()
    cur.close()
    return rows
 
def getCommentsCount():
    conn = sqlite3.connect(dbPath)
    cur = conn.cursor()
    cur.execute('SELECT count(1) FROM comments LIMIT 20')
    commentsCount = cur.fetchone()[0]
    conn.commit()
    cur.close()
    return commentsCount