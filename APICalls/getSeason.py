import requests
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import json
from season import Base, Season
from util import *
from datetime import datetime

def getRequest():
    headers = { # Request headers
            'Ocp-Apim-Subscription-Key':'dae600ece2454c71acc62def1108c7dd', }
    params = {}
    url = 'https://api.fantasydata.net/mlb/v2/JSON/currentSeason'
    try:
        r = requests.get(url, headers=headers, params=params)
        return r
    except Exception as e:
        print("[Errno {0}] ".format(e))
        return None

def getSeason():
    session = getSession()
    try:
        r = getRequest()
#conn.request("GET", "/mlb/v2/JSON/News?%s" % params, "{body}",
        #    headers) #response = conn.getresponse()
        if r != None:
            item= r.json()
            theID = item['Season']
            query = session.query(Season).filter(Season.Season== theID).scalar()
            thisSeason= Season(**{k:v for k, v in item.items() if k in
                Season.__table__.columns})
            if query is None:
                session.add(thisSeason)
            else:
                query = session.merge(thisSeason)#session.query(News).filter(News.NewsID == theID).update(newsItem)
            session.commit()
            print(thisSeason)
    #for key, value{j in item.items():
        #    print(str(key)+ ': '+ str(value))
    except Exception as e:
        print("[Errno {0}] ".format(e))
