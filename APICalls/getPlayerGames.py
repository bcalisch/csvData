import requests
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import json
from playerGame import Base, PlayerGame
from util import *
from datetime import datetime

def getRequest(theDate):
    prettyDate = translateDate(theDate)
    headers = { # Request headers
            'Ocp-Apim-Subscription-Key':'dae600ece2454c71acc62def1108c7dd', }
    params = {}
    print(prettyDate)
    url = 'https://api.fantasydata.net/mlb/v2/JSON/PlayerGameStatsByDate/{0}'.format(prettyDate)
    try:
        r = requests.get(url, headers=headers, params=params)
        return r
    except Exception as e:
        print("[Errno {0}] ".format(e))
        return None

def getRequestByPlayer(theDate, PlayerID):
    prettyDate = translateDate(theDate)
    headers = { # Request headers
            'Ocp-Apim-Subscription-Key':'dae600ece2454c71acc62def1108c7dd', }
    params = {}
    url = 'https://api.fantasydata.net/mlb/v2/JSON/PlayerGameStatsByDate/{0}/{1}'.format(theDate,
            PlayerID)
    try:
        r = requests.get(url, headers=headers, params=params)
        return r
    except Exception as e:
        print("[Errno {0}] ".format(e))
        return None

def getPlayerGameByDate(theDate):
    session = getSession()
    try:
        r = getRequest(theDate)
#conn.request("GET", "/mlb/v2/JSON/News?%s" % params, "{body}",
        #    headers) #response = conn.getresponse()
        if r != None:
            data = r.json()
            for item in data:
                theID = item['StatID']
                query = session.query(PlayerGame).filter(PlayerGame.StatID == theID).scalar()
                thisGame= PlayerGame(**{k:v for k, v in item.items() if k in
                    PlayerGame.__table__.columns})
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

def getPlayerGameByPlayer(theDate, playerID):
    session = getSession()
    try:
        r = getRequestByPlayer(theDate, playerID)
#conn.request("GET", "/mlb/v2/JSON/News?%s" % params, "{body}",
        #    headers) #response = conn.getresponse()
        if r != None:
            data = r.json()
            for item in data:
                theID = item['StatID']
                query = session.query(PlayerGame).filter(PlayerGame.StatID== theID).scalar()
                thisGame= PlayerGame(**{k:v for k, v in item.items() if k in PlayerGame.__table__.columns})
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
