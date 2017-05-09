import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,Boolean, create_engine, MetaData
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
class Team(Base):
    __tablename__='Inning'

    InningID= Column(Integer, primary_key=True)
    GameID = Column(Integer)
    InningNumber = Column(Integer)
    AwayTeamRuns = Column(Integer)
    HomeTeamRuns = Column(Integer)


engine = create_engine('mysql+pymysql://root:uerbc0707@localhost/baseball', echo = True)
Base.metadata.create_all(engine)



