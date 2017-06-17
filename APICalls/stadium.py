import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,Boolean, create_engine
from sqlalchemy.dialects.mysql.base import DECIMAL
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
class Stadium(Base):
    __tablename__='Stadium'

    StadiumID= Column(Integer, primary_key=True)
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
        return "<Stadium(Stadium = '{0}', Active = '{1}', Name = '{2}', City\
    ='{3}', State = '{4}', Country = '{5}', Capacity = '{6}', Surface\
    = '{7}'>".format(self.StadiumID, self.Active,self.Name, self.City,
            self.State, self.Country, self.Capacity, self.Surface)

engine = create_engine('mysql+pymysql://root:uerbc0707@localhost/baseball', echo = True)
Base.metadata.create_all(engine)



