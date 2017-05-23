import requests
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, update
import json
from news import Base, News


def translateJSON(data):
    parsedData = ''
    theCount = 1
    for key, value in data.items():
        if theCount == 1:
            parsedData = str(key)+"='"+str(value)+"'"
            theCount+=1
        else:
            parsedData +=', '+ str(key)+'="'+str(value)+'"'
    print(parsedData)
    return parsedData

engine = create_engine('mysql+pymysql://root:uerbc0707@localhost/baseball', echo = True)
Session = sessionmaker(bind=engine)
session = Session()
headers = { # Request headers
            'Ocp-Apim-Subscription-Key':'dae600ece2454c71acc62def1108c7dd', }
params = {}
url = 'https://api.fantasydata.net/mlb/v2/JSON/News'
try:
    r = requests.get(url, headers=headers, params = params)
#conn.request("GET", "/mlb/v2/JSON/News?%s" % params, "{body}",
    #    headers) #response = conn.getresponse()
    data = r.json()
    for item in data:
        theID = item['NewsID']
        query = session.query(News).filter(News.NewsID == theID).scalar()

        newsItem = News(**{k:v for k, v in item.items() if k in News.__table__.columns})
        if query is None:
            session.add(newsItem)
        else:
            query = session.merge(newsItem)#session.query(News).filter(News.NewsID == theID).update(newsItem)
        session.commit()

        #for key, value{j in item.items():
        #    print(str(key)+ ': '+ str(value))
except Exception as e:
    print("[Errno {0}] ".format(e))

####################################
