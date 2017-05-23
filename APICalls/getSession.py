import requests
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import json
from news import Base, News

engine = create_engine('mysql+pymysql://root:uerbc0707@localhost/baseball', echo = True)
Session = sessionmaker(bind=engine)
session = Session()
