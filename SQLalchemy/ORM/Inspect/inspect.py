from session_db import *

cc_cookie = Cookie('chocolate chip',
                   'http://some.awesome.me/cookie/recipe/cc_recipe.html',
                   'CC01',
                   12,
                   0.50)
# +------------------------------------------------------------------------+
# There are four possible states for data object instances:
# +------------------------------------------------------------------------+
# Transient
# ...The instance is not in session, and is not in the database.
#
# Pending
# ...The instance has been added to the session with add(), but hasnt been
#  flushed or committed.
#
# Persistent
# ...The object in session has a corresponding record in the database.
#
# Detached
# ...The instance is no longer connected to the session, but has a record
# in the database. session.expunge(cc_cookie)

from sqlalchemy import inspect

insp = inspect(cc_cookie)

states = ['transient','pending','persistent','detached']

for state in states:
    print('{:>10}: {}'.format(state, getattr(insp, state)))

# also
print(insp.transient)
print(insp.pending)
print(insp.persistent)
print(insp.detached)
print(insp.modified)
