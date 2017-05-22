import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,Boolean, create_engine
from sqlalchemy.dialects.mysql.base import DECIMAL
from sqlalchemy.dialects.mysql import DATETIME
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
class DfsSlate(Base):
    __tablename__='DfsSlate'
    SlateID = Column(Integer, primary_key = True)
    Operator = Column(String(20))
    OperatorSlateID = Column(Integer)
    OperatorName = Column(String(50))
    OperatorDay = Column(DATETIME)
    OperatorStartTime = Column(DATETIME)
    NumberOfGames = Column(Integer)

    def __repr__(self):
        return '<OperatorName: %r>'%(self.OperatorName)

engine = create_engine('mysql+pymysql://root:uerbc0707@localhost/baseball', echo = True)
Base.metadata.create_all(engine)



