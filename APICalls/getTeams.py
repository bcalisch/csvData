import requests
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import json
from team import Base, Team
from util import *
from datetime import datetime

def getRequest():
    headers = { # Request headers
            'Ocp-Apim-Subscription-Key':'dae600ece2454c71acc62def1108c7dd', }
    params = {}
    url = 'https://api.fantasydata.net/mlb/v2/JSON/AllTeams'
    try:
        r = requests.get(url, headers=headers, params=params)
        return r
    except Exception as e:
        print("[Errno {0}] ".format(e))
        return None

def getAllTeams():
    session = getSession()
    try:
        r = getRequest()
#conn.request("GET", "/mlb/v2/JSON/News?%s" % params, "{body}",
        #    headers) #response = conn.getresponse()
        if r != None:
            data = r.json()
            print(r.json())
            for item in data:
                theID = item['TeamID']
                query = session.query(Team).filter(Team.TeamID== theID).scalar()
                thisTeam = Team(**{k:v for k, v in item.items() if k in Team.__table__.columns})
                if query is None:
                    ''
                    session.add(thisTeam)
                else:
                    query = session.merge(thisTeam)#session.query(News).filter(News.NewsID == theID).update(newsItem)
                session.commit()
                print(thisTeam)
            #for key, value{j in item.items():
                #    print(str(key)+ ': '+ str(value))
    except Exception as e:
        print("[Errno {0}] ".format(e))

####################################
