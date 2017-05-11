import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,Boolean, create_engine
from sqlalchemy.dialects.mysql import DATETIME
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
class Pitch(Base):
    __tablename__='Pitch'
    PitchID= Column(Integer, primary_key=True)
    PlayID= Column(Integer, primary_key=True)
    PitchNumberThisAtBat = Column(Integer)
    PitcherID = Column(Integer)
    HitterID = Column(Integer)
    Outs = Column(Integer)
    BallsBeforePitch = Column(Integer)
    StrikesBeforePitch = Column(Integer)
    Strike = Column(Boolean)
    Ball = Column(Boolean)
    Foul = Column(Boolean)
    Swinging = Column(Boolean)
    Looking = Column(Boolean)

    def __repr__(self):
        return '<PitchID:: %r>'%(self.PitchID)

engine = create_engine('mysql+pymysql://root:uerbc0707@localhost/baseball', echo = True)
Base.metadata.create_all(engine)



