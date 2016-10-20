from sqlalchemy import MetaData, create_engine, Table
metadata = MetaData()
engine = create_engine('sqlite:///Chinook_Sqlite.sqlite')

artist = Table('Artist', metadata, autoload=True, autoload_with=engine)

album = Table('Album', metadata, autoload=True,autoload_with=engine)
