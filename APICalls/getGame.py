import requests
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import json
from news import Base, Game


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
        print('Here\'s one')
        newData = translateJSON(item)
        print(News.__table__.columns)
        newsItem = News(**{k:v for k, v in item.items() if k in News.__table__.columns})
        session.add(newsItem)
        session.commit()
        #for key, value{j in item.items():
        #    print(str(key)+ ': '+ str(value))
except Exception as e:
    print("[Errno {0}] ".format(e))

####################################
