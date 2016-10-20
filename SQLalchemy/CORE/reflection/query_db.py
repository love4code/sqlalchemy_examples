from reflections_db import *
from sqlalchemy import select
print(artist.columns.keys())
print(album.columns.keys())
# Reflect Single Table
s = select([artist]).limit(10)
print([res for res in engine.execute(s).fetchall()])
s = select([album]).limit(10)
print([res for res in engine.execute(s).fetchall()])

# Reflecting an entire DataBase
metadata.reflect(bind=engine)
print(metadata.tables.keys())
# Assign the Table of a dbto a varriable for Reference
playlist = metadata.tables['Playlist']
s = select([playlist]).limit(10)
print([res for res in engine.execute(s).fetchall()])

