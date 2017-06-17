import requests
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import json
from play import Base, Play
from pitch import Base, Pitch
from util import *

def getRequest(gameID):
    headers = { # Request headers
            'Ocp-Apim-Subscription-Key':'dae600ece2454c71acc62def1108c7dd', }
    params = {}
    print(prettyDate)
    url = 'https://api.fantasydata.net/mlb/v2/JSON/PlayByPlay/{0}'.format(gameID)
    try:
        r = requests.get(url, headers=headers, params=params)
        return r
    except Exception as e:
        print("[Errno {0}] ".format(e))
        return None

def getPlaysByGame(gameID):
    session = getSession()
    try:
        r = getRequest(gameID)
#conn.request("GET", "/mlb/v2/JSON/News?%s" % params, "{body}",
        #    headers) #response = conn.getresponse()
        if r != None:
            data = r.json()
            for item in data:
                theID = item['GameID']
                query = session.query(Game).filter(Game.GameID== theID).scalar()
                thisGame= Game(**{k:v for k, v in item.items() if k in Game.__table__.columns})
                if query is None:
                    ''
                    session.add(thisGame)
                else:
                    print(thisGame.DateTime)
                    print(query.DateTime)
                    query = session.merge(thisGame)#session.query(News).filter(News.NewsID == theID).update(newsItem)
                session.commit()
                print(thisGame)
            #for key, value{j in item.items():
                #    print(str(key)+ ': '+ str(value))
    except Exception as e:
        print("[Errno {0}] ".format(e))

def getGameByYear(year):
    session = getSession()
    try:
        r = getRequestByYear(year)
#conn.request("GET", "/mlb/v2/JSON/News?%s" % params, "{body}",
        #    headers) #response = conn.getresponse()
        if r != None:
            data = r.json()
            for item in data:
                theID = item['GameID']
                query = session.query(Game).filter(Game.GameID== theID).scalar()
                thisGame= Game(**{k:v for k, v in item.items() if k in Game.__table__.columns})
                if query is None:
                    ''
                    session.add(thisGame)
                else:
                    print(thisGame.DateTime)
                    print(query.DateTime)
                    query = session.merge(thisGame)#session.query(News).filter(News.NewsID == theID).update(newsItem)
                session.commit()
                print(thisGame)
            #for key, value{j in item.items():
                #    print(str(key)+ ': '+ str(value))
    except Exception as e:
        print("[Errno {0}] ".format(e))

####################################
