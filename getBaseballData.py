from listMaker import *
from dbutil import *


listObj = listFromCSV('./fantasy.2016/Game.2016.csv', 'Game')
listObj.insertRecords()
listObj = listFromCSV('./fantasy.2016/Inning.2016.csv', 'Inning')
listObj.insertRecords()
listObj = listFromCSV('./fantasy.2016/Pitch.2016.csv', 'Pitch')
listObj.insertRecords()
listObj = listFromCSV('./fantasy.2016/Play.2016.csv', 'Play')
listObj.insertRecords()
listObj = listFromCSV('./fantasy.2016/Player.2016.csv', 'Player')
listObj.insertRecords()
listObj = listFromCSV('./fantasy.2016/PlayerGame.2016.csv', 'PlayerGame')
listObj.insertRecords()
listObj = listFromCSV('./fantasy.2016/PlayerGameProjection.2016.csv', 'PlayerGameProjection')
listObj.insertRecords()
listObj = listFromCSV('./fantasy.2016/PlayerSeason.2016.csv', 'PlayerSeason')
listObj.insertRecords()
listObj = listFromCSV('./fantasy.2016/PlayerSeasonVSLeft.2016.csv', 'PlayerSeason')
listObj.insertRecords()
listObj = listFromCSV('./fantasy.2016/PlayerSeasonVSRight.2016.csv', 'PlayerSeason')
listObj.insertRecords()
listObj = listFromCSV('./fantasy.2016/PlayerSeasonHome.2016.csv', 'PlayerSeason')
listObj.insertRecords()
listObj = listFromCSV('./fantasy.2016/PlayerSeasonAway.2016.csv', 'PlayerSeason')
listObj.insertRecords()
listObj = listFromCSV('./fantasy.2016/PlayerSeasonVsSwitch.2016.csv', 'PlayerSeason')
listObj.insertRecords()
listObj = listFromCSV('./fantasy.2016/Stadium.2016.csv', 'Stadium')
listObj.insertRecords()
listObj = listFromCSV('./fantasy.2016/Team.2016.csv', 'Team')
listObj.insertRecords()
listObj = listFromCSV('./fantasy.2016/TeamGame.2016.csv', 'TeamGame')
listObj.insertRecords()
listObj = listFromCSV('./fantasy.2016/TeamSeason.2016.csv', 'TeamSeason')
listObj.insertRecords()
