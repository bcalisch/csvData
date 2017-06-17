import requests
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import json
from playerSeason import Base, PlayerSeason
from util import *
from datetime import datetime

def getRequest(year):
    headers = { # Request headers
            'Ocp-Apim-Subscription-Key':'dae600ece2454c71acc62def1108c7dd', }
    params = {}
    print(year)
    url = 'https://api.fantasydata.net/mlb/v2/JSON/PlayerSeasonStats/{0}'.format(year)
    try:
        r = requests.get(url, headers=headers, params=params)
        return r
    except Exception as e:
        print("[Errno {0}] ".format(e))
        return None

def getRequestByPlayer(year, PlayerID):
    headers = { # Request headers
            'Ocp-Apim-Subscription-Key':'dae600ece2454c71acc62def1108c7dd', }
    params = {}
    url = 'https://api.fantasydata.net/mlb/v2/JSON/PlayerSeasonStatsByPlayer/{0}/{1}'.format(year,
            PlayerID)
    try:
        r = requests.get(url, headers=headers, params=params)
        return r
    except Exception as e:
        print("[Errno {0}] ".format(e))
        return None

def getRequestByTeam(year, team):
    headers = { # Request headers
            'Ocp-Apim-Subscription-Key':'dae600ece2454c71acc62def1108c7dd', }
    params = {}
    url = 'https://api.fantasydata.net/mlb/v2/JSON/PlayerSeasonStatsByTeam/{0}/{1}'.format(year,
            team)
    try:
        r = requests.get(url, headers=headers, params=params)
        return r
    except Exception as e:
        print("[Errno {0}] ".format(e))
def getPlayerSeason(year):
    session = getSession()
    try:
        r = getRequest(year)
#conn.request("GET", "/mlb/v2/JSON/News?%s" % params, "{body}",
        #    headers) #response = conn.getresponse()
        if r != None:
            data = r.json()
            for item in data:
                theID = item['StatID']
                query = session.query(PlayerSeason).filter(PlayerSeason.StatID == theID).scalar()
                thisSeason= PlayerSeason(**{k:v for k, v in item.items() if k in
                    PlayerSeason.__table__.columns})
                if query is None:
                    ''
                    session.add(thisSeason)
                else:
                    print(thisSeason.StatID)
                    query = session.merge(thisSeason)#session.query(News).filter(News.NewsID == theID).update(newsItem)
                session.commit()
                print(thisSeason)
            #for key, value{j in item.items():
                #    print(str(key)+ ': '+ str(value))
    except Exception as e:
        print("[Errno {0}] ".format(e))

def getPlayerSeasonByPlayer(year, playerID):
    session = getSession()
    try:
        r = getRequestByPlayer(year, playerID)
#conn.request("GET", "/mlb/v2/JSON/News?%s" % params, "{body}",
        #    headers) #response = conn.getresponse()
        if r != None:
            data = r.json()
            for item in data:
                theID = item['StatID']
                query = session.query(PlayerSeason).filter(PlayerSeason.StatID== theID).scalar()
                thisSeason= PlayerSeason(**{k:v for k, v in item.items() if k in PlayerSeason.__table__.columns})
                if query is None:
                    ''
                    session.add(thisSeason)
                else:
                    print(thisSeason.StatID)
                    query = session.merge(thisSeason)#session.query(News).filter(News.NewsID == theID).update(newsItem)
                session.commit()
                print(thisSeason)
            #for key, value{j in item.items():
                #    print(str(key)+ ': '+ str(value))
    except Exception as e:
        print("[Errno {0}] ".format(e))

def getPlayerSeasonByTeam(year, teamID):
    session = getSession()
    try:
        r = getRequestByTeam(year, teamID)
#conn.request("GET", "/mlb/v2/JSON/News?%s" % params, "{body}",
        #    headers) #response = conn.getresponse()
        if r != None:
            data = r.json()
            for item in data:
                theID = item['StatID']
                query = session.query(PlayerSeason).filter(PlayerSeason.StatID== theID).scalar()
                thisSeason= PlayerSeason(**{k:v for k, v in item.items() if k in PlayerSeason.__table__.columns})
                if query is None:
                    ''
                    session.add(thisSeason)
                else:
                    print(thisSeason.StatID)
                    query = session.merge(thisSeason)#session.query(News).filter(News.NewsID == theID).update(newsItem)
                session.commit()
                print(thisSeason)
            #for key, value{j in item.items():
                #    print(str(key)+ ': '+ str(value))
    except Exception as e:
        print("[Errno {0}] ".format(e))

####################################
