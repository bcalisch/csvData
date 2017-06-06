from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import calendar
def translateDate(theDate):
    year = str(theDate.year)
    theMonth = calendar.month_name[theDate.month].upper()[:3]
    theDay = str(theDate.day)
    return year+'-'+theMonth+'-'+theDay

def getSession():
    engine = create_engine('mysql+pymysql://root:uerbc0707@localhost/baseball?charset=utf8',echo = False)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
