from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///products.sqlite')
Session = sessionmaker(bind=engine)
Session()

Base = declarative_base()