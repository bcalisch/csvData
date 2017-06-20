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
            gameID = data['Game']['GameID']
            plays = data['Plays']
            for play in plays:
                theID = play['PlayID']
                query = session.query(Play).filter(Play.PlayID== theID).scalar()
                thisPlay= Play(**{k:v for k, v in play.items() if k in Play.__table__.columns})
                thisPlay.GameID = gameID
                if query is None:
                    ''
                    session.add(thisPlay)
                else:
                    query = session.merge(thisPlay)#session.query(News).filter(News.NewsID == theID).update(newsItem)
                pitches = play['Pitches']
                for pitch in pitches:
                    theID = pitch['PitchID']
                    query = session.query(Pitch).filter(Pitch.PitchID ==
                            theID).scalar()
                    thisPitch = Pitch(**{k:v for k, v in pitch.items() if k in
                        Pitch.__table__.columns})
                    if query is None:
                        session.add(thisPitch)
                    else:
                        query = session.merge(thisPitch)
                session.commit()
    except Exception as e:
        print("[Errno {0}] ".format(e))
    session.close()

####################################
