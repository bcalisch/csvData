from datetime import datetime
from getGame import getGameByDate, getGameByYear, getAllGames
from getPlayerGames import getPlayerGameByDate
from getPlayerSeason import *
from getNews import getNewsByDate
from getStanding import *
from getPlay import *
import calendar

def gamesForYear():
    today= datetime.today()
    year = today.year
    month = today.month
    for x in range(1,month):
        for y in range(1,calendar.monthrange(year,x)[1]+1):
            date = datetime(year,x,y)
            getGameByDate(date)

def gamesForMonth():
    today= datetime.today()
    year = today.year
    month = today.month
    for y in range(1,calendar.monthrange(year,month)[1]+1):
        date = datetime(year,month,y)
        print(date)
        getGameByDate(date)

def gamesByYear():
    for y in range(2003,2018):
        getGameByYear(y)

def newsForYear():
    today = datetime.today()
    year = today.year
    month = today.month
    for x in range(1,month):
        for y in range(1,calendar.monthrange(year,x)[1]+1):
            date = datetime(year,x,y)
            getNewsByDate(date)

def newsForMonth():
    today= datetime.today()
    year = today.year
    month = today.month
    for y in range(1,calendar.monthrange(year,month)[1]+1):
        date = datetime(year,month,y)
        print(date)
        getNewsByDate(date)

def playerGamesForYear():
    today= datetime.today()
    year = today.year
    month = today.month
    for x in range(1,month):
        for y in range(1,calendar.monthrange(year,x)[1]+1):
            date = datetime(year,x,y)
            getPlayerGameByDate(date)

def playerSeason():
    for y in range(2003,2018):
        getPlayerSeason(y)

def getAllPlays():
    gameList = getAllGames()
    for game in gameList:
        if game > 33517 and game < 40000:
            print(game)
            getPlaysByGame(game)

def getAllPlays2():
    gameList = getAllGames()
    for game in sorted(list(gameList),reverse=True):
        if game < 38000 and game > 3400:
            print(game)
            getPlaysByGame(game)

def getAllStandings():
    for y in range(2003,2018):
        getStanding(y)

def getStandingsThisYear():
    year = datetime.today().year
    getStanding(year)

