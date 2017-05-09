import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,Boolean, create_engine
from sqlalchemy.dialects.mysql.base import DECIMAL
from sqlalchemy.dialects.mysql import DATETIME
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
class Player(Base):
    __tablename__='Player'

    PlayerID= Column(Integer, primary_key=True)
    SportsDataID = Column(String(50))
    Status = Column(Integer)
    TeamID = Column(Integer)
    Team = Column(String(10))
    Jersey = Column(Integer)
    PositionCategory = Column(String(10))
    Position = Column(String(10))
    MLBAMID = Column(Integer)
    FirstName = Column(String(50))
    LastName = Column(String(50))
    BatHand = Column(String(1))
    ThrowHand = Column(String(1))
    Height = Column(Integer)
    Weight = Column(Integer)
    BirthDate = Column(DATETIME)
    BirthCity = Column(String(50))
    BirthState = Column(String(50))
    BirthCountry = Column(String(50))
    HighSchool = Column(String(50))
    College = Column(String(50))
    ProDebut = Column(DATETIME)
    Salary = Column(Integer)
    PhotoUrl = Column(String(250))
    SportRadarPlayerID = Column(String(50))
    RotoWirePlayerID = Column(Integer)
    RotoworldPlayerID = Column(Integer)
    FantasyAlarmPlayerID = Column(Integer)
    StatsPlayerID = Column(Integer)
    SportsDirectPlayerID = Column(Integer)
    XmlTeamPlayerID = Column(Integer)
    InjuryStatus = Column(String(50))
    InjuryBodyPart = Column(String(50))
    InjuryStartDate = Column(DATETIME)
    InjuryNotes = Column(String(250))
    FanDuelPlayerID = Column(Integer)
    DraftKingsPlayerID = Column(Integer)
    YahooPlayerID = Column(Integer)
    UpcomingGameID = Column(Integer)
    FanDuelName = Column(String(50))
    DraftKingsName = Column(String(50))
    YahooName = Column(String(50))
    GlobalTeamID = Column(Integer)
    FantasyDraftName = Column(String(50))
    FantasyDraftPlayerID = Column(Integer)

    def __repr__(self):
        return '<Player: {0} {1}r>'.format(self.FirstName, self.LastName)

engine = create_engine('mysql+pymysql://root:uerbc0707@localhost/baseball', echo = True)
Base.metadata.create_all(engine)



