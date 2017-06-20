import requests
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import json
from util import *
from teamGame import Base, TeamGame
from datetime import datetime

def getRequest(theDate):
    prettyDate = translateDate(theDate)
    headers = { # Request headers
            'Ocp-Apim-Subscription-Key':'dae600ece2454c71acc62def1108c7dd', }
    params = {}
    print(prettyDate)
    url = 'https://api.fantasydata.net/mlb/v2/JSON/TeamGameStatsByDate/{0}'.format(prettyDate)
    try:
        r = requests.get(url, headers=headers, params=params)
        return r
    except Exception as e:
        print("[Errno {0}] ".format(e))
        return None

def getTeamGameByDate(theDate):
    session = getSession()
    try:
        r = getRequest(theDate)
#conn.request("GET", "/mlb/v2/JSON/News?%s" % params, "{body}",
        #    headers) #response = conn.getresponse()
        if r != None:
            data = r.json()
            for item in data:
                theID = item['StatID']
                query = session.query(TeamGame).filter(TeamGame.StatID== theID).scalar()
                thisTeamGame= TeamGame(**{k:v for k, v in item.items() if k in TeamGame.__table__.columns})
                if query is None:
                    ''
                    session.add(thisTeamGame)
                else:
                    query = session.merge(thisTeamGame)#session.query(News).filter(News.NewsID == theID).update(newsItem)
                session.commit()
            #for key, value{j in item.items():
                #    print(str(key)+ ': '+ str(value))
                print(theTeamGame)
    except Exception as e:
        print("[Errno {0}] ".format(e))



####################################
