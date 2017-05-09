import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,Boolean, create_engine
from sqlalchemy.dialects.mysql.base import DECIMAL
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
class Stadium(Base):
    __tablename__='Stadium'

    Stadium= Column(Integer, primary_key=True)
    Active = Column(Boolean)
    Name = Column(String(50))
    City = Column(String(50))
    State = Column(String(10))
    Country = Column(String(10))
    Capacity = Column(Integer)
    Surface = Column(String(50))
    LeftField = Column(Integer)
    MidLeftField = Column(Integer)
    CenterField = Column(Integer)
    MidRightCenterField= Column(Integer)
    RightCenterField= Column(Integer)
    RightField= Column(Integer)
    GeoLat = Column(DECIMAL(11,8))
    GeoLong = Column(DECIMAL(11,8))
    Altitude = Column(Integer)
    HomePlateDirection = Column(Integer)

    def __repr__(self):
        return '<Team: %r>'%(self.Name)

engine = create_engine('mysql+pymysql://root:uerbc0707@localhost/baseball', echo = True)
Base.metadata.create_all(engine)



