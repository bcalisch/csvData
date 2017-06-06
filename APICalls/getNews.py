import requests

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, update
import json
from news import Base, News
from util import *


def getRequest():
    headers = { # Request headers
            'Ocp-Apim-Subscription-Key':'dae600ece2454c71acc62def1108c7dd', }
    params = {}
    url = 'https://api.fantasydata.net/mlb/v2/JSON/News'
    try:
        r = requests.get(url, headers=headers, params=params)
        return r
    except Exception as e:
        print("[Errno {0}] ".format(e))

def getRequestByDate(theDate):
    """Returns request for news items given the right date"""
    prettyDate = translateDate(theDate)
    headers = { # Request headers
            'Ocp-Apim-Subscription-Key':'dae600ece2454c71acc62def1108c7dd', }
    params = {}
    url = 'https://api.fantasydata.net/mlb/v2/JSON/NewsByDate/{0}'.format(prettyDate)
    try:
        r = requests.get(url, headers=headers, params=params)
        return r
    except Exception as e:
        print("[Errno {0}] ".format(e))

def getRequestByPlayer(playerID):
    """Returns request given playerID"""
    headers = { # Request headers
            'Ocp-Apim-Subscription-Key':'dae600ece2454c71acc62def1108c7dd', }
    params = {}
    url= 'https://api.fantasydata.net/mlb/v2/JSON/NewsByPlayerID/{0}'.format(playerID)
    try:
        r = requests.get(url, headers=headers, params=params)
        return r
    except Exception as e:
        print("[Errno {0}] ".format(e))

def getNews():
    r = getRequest()
    if r != None:
        session = getSession()
        try:
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
        #    print(str(key)+ ': '+ str(value))
        except Exception as e:
            print("[Errno {0}] ".format(e))

def getNewsByDate(theDate):
    r = getRequestByDate(theDate)
    if r != None:
        session = getSession()
        try:
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
        #    print(str(key)+ ': '+ str(value))
        except Exception as e:
            print("[Errno {0}] ".format(e))

def getNewsByPlayer(playerID):
    r = getRequestByPlayer(playerID)
    if r != None:
        session = getSession()
        try:
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
        #    print(str(key)+ ': '+ str(value))
        except Exception as e:
            print("Errno getting news By PlayerID: {0}] ".format(e))

