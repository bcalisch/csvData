import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,Boolean, create_engine
from sqlalchemy.dialects.mysql.base import DECIMAL
from sqlalchemy.dialects.mysql import DATETIME
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
class DfsSlateGame(Base):
    __tablename__='DfsSlateGame'
    SlateGameID = Column(Integer, primary_key = True)
    SlateID = Column(Integer)
    GameID = Column(Integer)
    OperatorGameID = Column(Integer)

    def __repr__(self):
        return '<SlateID: %r>'%(self.SlateGameID)

engine = create_engine('mysql+pymysql://root:uerbc0707@localhost/baseball', echo = True)
Base.metadata.create_all(engine)



