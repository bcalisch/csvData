import requests
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import json
from standing import Base,Standing
from util import *

def getRequest(year):
    headers = { # Request headers
            'Ocp-Apim-Subscription-Key':'dae600ece2454c71acc62def1108c7dd', }
    params = {}
    url = 'https://api.fantasydata.net/mlb/v2/JSON/Standings/{0}'.format(year)
    try:
        r = requests.get(url, headers=headers, params=params)
        return r
    except Exception as e:
        print("[Errno getting request {0}] ".format(e))
        return None

def getStanding(year):
    session = getSession()
    try:
        r = getRequest(year)
#conn.request("GET", "/mlb/v2/JSON/News?%s" % params, "{body}",
        #    headers) #response = conn.getresponse()
        if r != None:
            data = r.json()
            for item in data:
                theSeason = item['Season']
                theSeasonID = item['SeasonType']
                theTeamID = item['TeamID']
                theKey = item['Key']
                print(str(theSeason) + ' : '+ str(theSeasonID)+
                        ' : ' + str(theTeamID)+ ' : ' + str(theKey))
                query = session.query(Standing).filter(Standing.Season ==
                        theSeasonID, Standing.SeasonType == theSeasonID,
                        Standing.TeamID == theTeamID, Standing.Key == theKey).scalar()
                thisStanding = Standing(**{k:v for k, v in item.items() if k in
                    Standing.__table__.columns})
                if query is None:
                    session.add(thisStanding)
                else:
                    query = session.merge(thisStanding)#session.query(News).filter(News.NewsID == theID).update(newsItem)
                session.commit()
                print(thisStanding)
    #for key, value{j in item.items():
        #    print(str(key)+ ': '+ str(value))
    except Exception as e:
        print("[Errno {0}] ".format(e))
