import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,Boolean, create_engine
from sqlalchemy.dialects.mysql import DATETIME
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
class Play(Base):
    __tablename__='Play'
    PlayID= Column(Integer, primary_key=True)
    GameID = Column(Integer)
    InningID = Column(Integer)
    InningNumber = Column(Integer)
    InningHalf = Column(String(1))
    PlayNumber = Column(Integer)
    InningBatterNumber = Column(Integer)
    AwayTeamRuns = Column(Integer)
    HomeTeamRuns = Column(Integer)
    HitterID = Column(Integer)
    PitcherID = Column(Integer)
    HitterTeamID = Column(Integer)
    PitcherTeamID = Column(Integer)
    HitterName = Column(String(50))
    PitcherName = Column(String(50))
    PitcherThrowHand = Column(String(10))
    HitterBatHand = Column(String(1))
    HitterPosition = Column(String(10))
    Outs = Column(Integer)
    Balls = Column(Integer)
    Strikes = Column(Integer)
    PitchNumberThisAtBat = Column(Integer)
    Result = Column(String(50))
    NumberOfOutsOnPlay = Column(Integer)
    RunsBattedIn = Column(Integer)
    AtBat = Column(Boolean)
    Strikeout = Column(Boolean)
    Walk = Column(Boolean)
    Hit = Column(Boolean)
    Out = Column(Boolean)
    Sacrifice = Column(Boolean)
    Error = Column(Boolean)
    Updated = Column(DATETIME)
    Description = Column(String(250))

    def __repr__(self):
        return "Play( GameID = '{0}', PlayID = '{1}')>".format(self.GameID,
                self.PlayID)

engine = create_engine('mysql+pymysql://root:uerbc0707@localhost/baseball', echo = True)
Base.metadata.create_all(engine)



