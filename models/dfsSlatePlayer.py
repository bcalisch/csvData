import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,Boolean, create_engine
from sqlalchemy.dialects.mysql.base import DECIMAL
from sqlalchemy.dialects.mysql import DATETIME
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
class DfsSlatePlayer(Base):
    __tablename__='DfsSlatePlayer'
    SlatePlayerID = Column(Integer, primary_key = True)
    SlateID = Column(Integer, primary_key = True)
    SlateGameID = Column(Integer)
    PlayerID = Column(Integer)
    PlayerGameProjectionStatID = Column(Integer)
    OperatorPlayerID = Column(String(25))
    OperatorSlatePlayerID = Column(String(50))
    OperatorPlayerName = Column(String(50))
    OperatorPosition = Column(String(10))
    OperatorSalary = Column(Integer)
    def __repr__(self):
        return '<OperatorPlayerName: %r>'%(self.OperatorPlayerName)

engine = create_engine('mysql+pymysql://root:uerbc0707@localhost/baseball', echo = True)
Base.metadata.create_all(engine)



