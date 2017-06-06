import requests
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import json
from team import Base, Team
from player import Base, Player
from util import *
from datetime import datetime

def getRequest(teamID):
    headers = { # Request headers
            'Ocp-Apim-Subscription-Key':'dae600ece2454c71acc62def1108c7dd', }
    params = {}
    url = 'https://api.fantasydata.net/mlb/v2/JSON/Players/{0}'.format(teamID)
    try:
        r = requests.get(url, headers=headers, params=params)
        return r
    except Exception as e:
        print("[Errno {0}] ".format(e))
        return None

def getRequestByPlayer(playerID):
    headers = { # Request headers
            'Ocp-Apim-Subscription-Key':'dae600ece2454c71acc62def1108c7dd', }
    params = {}
    url = 'https://api.fantasydata.net/mlb/v2/JSON/Player/{0}'.format(playerID)
    try:
        r = requests.get(url, headers=headers, params=params)
        return r
    except Exception as e:
        print("[Errno {0}] ".format(e))
        return None

def getAllPlayers():
    session = getSession()
    try:
        query = session.query(Team).all()
        for team in query:
            if team.Active:
                print(team.Key)
                r = getRequest(team.Key)
                if r != None:
                    data = r.json()
                    for item in data:
                        theID = item['PlayerID']
                        query = session.query(Player).filter(Player.PlayerID== theID).scalar()
                        thisPlayer = Player(**{k:v for k, v in item.items() if k in Player.__table__.columns})
                        if query is None:
                            session.add(thisPlayer)
                        else:
                            query = session.merge(thisPlayer)#session.query(News).filter(News.NewsID == theID).update(newsItem)
                        session.commit()
                        print(thisPlayer)
            #for key, value{j in item.items():
                #    print(str(key)+ ': '+ str(value))
    except Exception as e:
        print("[Errno {0}] ".format(e))

def getPlayer(playerID):
    session = getSession()
    try:
        r = getRequestByPlayer(playerID)
        if r != None:
            data = r.json()
            theID = data['PlayerID']
            query = session.query(Player).filter(Player.PlayerID == theID).scalar()
            thisPlayer = Player(**{k:v for k, v in data.items() if k in Player.__table__.columns})
            if query is None:
                session.add(thisPlayer)
            else:
                query = session.merge(thisPlayer)
            session.commit()
            print(thisPlayer)
    except Exception as e:
        print("[Errno attempting to save player by ID: {0}] ".format(e) )

####################################
