import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,Boolean, create_engine, MetaData
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
class team(Base):
    __tablename__='team'

    TeamID = Column(Integer, primary_key=True)
    Key = Column(String(10))
    Active = Column(Boolean)
    City = Column(String(50))
    Name = Column(String(50))
    StadiumID = Column(Integer)
    League = Column(String(10))
    Division = Column(String(10))
    PrimaryColor = Column(String(6))
    SecondaryColor= Column(String(6))
    TertiaryColor = Column(String(6))
    QuarternaryColor = Column(String(6))
    WikipediaLogoUrl = Column(String(250))
    GlobalTeamID = Column(Integer)

    def __repr__(self):
        return '<Team: %r>'%(self.Name)

engine = create_engine('mysql+pymysql://root:uerbc0707@localhost/baseball', echo = True)
Base.metadata.create_all(engine)



