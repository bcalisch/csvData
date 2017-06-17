import requests
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import json
from stadium import Base, Stadium
from util import *

def getRequest():
    headers = { # Request headers
            'Ocp-Apim-Subscription-Key':'dae600ece2454c71acc62def1108c7dd', }
    params = {}
    url = 'https://api.fantasydata.net/mlb/v2/JSON/Stadiums'
    try:
        r = requests.get(url, headers=headers, params=params)
        return r
    except Exception as e:
        print("[Errno getting request {0}] ".format(e))
        return None

def getStadium():
    session = getSession()
    try:
        r = getRequest()
#conn.request("GET", "/mlb/v2/JSON/News?%s" % params, "{body}",
        #    headers) #response = conn.getresponse()
        if r != None:
            data = r.json()
            for item in data:
                theID = item['StadiumID']
                query = session.query(Stadium).filter(Stadium.StadiumID== theID).scalar()
                thisStadium= Stadium(**{k:v for k, v in item.items() if k in
                    Stadium.__table__.columns})
                if query is None:
                    session.add(thisStadium)
                else:
                    query = session.merge(thisStadium)#session.query(News).filter(News.NewsID == theID).update(newsItem)
                session.commit()
                print(thisStadium)
    #for key, value{j in item.items():
        #    print(str(key)+ ': '+ str(value))
    except Exception as e:
        print("[Errno {0}] ".format(e))
