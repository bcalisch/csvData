import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,Boolean, create_engine
from sqlalchemy.dialects.mysql import DATETIME
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
class News(Base):
    __tablename__='News'
    NewsID= Column(Integer, primary_key=True)
    Title = Column(String(50))
    Updated = Column(DATETIME)
    Url = Column(String(250))
    Content = Column(String(50))
    Source = Column(String(50))
    TermsOfUse = Column(String(50))
    PlayerID = Column(Integer)
    TeamID = Column(Integer)
    Team = Column(String(50))

    def __repr__(self):
        return '<Title: %r>'%(self.Title)

engine = create_engine('mysql+pymysql://root:uerbc0707@localhost/baseball', echo = True)
Base.metadata.create_all(engine)



