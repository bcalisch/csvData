import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,Boolean, create_engine
from sqlalchemy.dialects.mysql.base import DECIMAL
from sqlalchemy.dialects.mysql import DATETIME
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
class Standing(Base):
    __tablename__='Standing'
    Season = Column(Integer, primary_key = True)
    SeasonType = Column(Integer, primary_key = True)
    TeamID = Column(Integer, primary_key = True)
    Key = Column(String(10), primary_key = True)
    City = Column(String(50))
    Name = Column(String(50))
    League = Column(String(20))
    Division = Column(String(20))
    Wins = Column(Integer)
    Losses = Column(Integer)
    Percentage = Column(DECIMAL(11,8))
    DivisionWins = Column(Integer)
    DivisionLosses = Column(Integer)

    def __repr__(self):
        return '<Standing: %r>'%(self.Name)

engine = create_engine('mysql+pymysql://root:uerbc0707@localhost/baseball', echo = True)
Base.metadata.create_all(engine)



