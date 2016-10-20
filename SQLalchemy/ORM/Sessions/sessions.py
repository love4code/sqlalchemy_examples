from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# Import sessionmaker class
engine = create_engine('sqlite:///ormTest.db',echo=True)
# Defines sessionmaker class with the bind configuration supplied by the
# sessionmaker
Session = sessionmaker(bind=engine)
# Creates a session from our generated Session class
session = Session()