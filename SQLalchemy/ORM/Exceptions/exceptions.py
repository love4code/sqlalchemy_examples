from session_db import *

# MultipleResultsSFound Exception

# This exception occurs when we use the .one() query method,
# but get more than one result back.
dcc = Cookie('dark chocolate chip',
             'http://some.awesome.me/cookie/recipe/dcc_recipe.html',
             'CC02',
             1,
             0.75)

# session.add(dcc)
# session.commit()

results = session.query(Cookie).one()

# ERROR MESSAGE:
# MultipleResultsFound: Multiple rows were found for one()

# Another exception related to this is the NoResultFound exception,
# which would occur if we used the .one() method and
# the query returned no results.

from sqlalchemy.orm.exc import MultipleResultsFound

try:
    results = session.query(Cookie).one()
except MultipleResultsFound as error:
    print('We found too many cookies... is that even possible?')

# +------------------------------------------------------------------------+
# DetachedInstanceError
# -------------------------------------------------------------------------+

# This exception occurs when we attempt to access an attribute on
# an instance that needs to be loaded from the database,
# but the instance we are using is not currently attached to the database.

order = session.query(Order).first()
session.expunge(order)
print(order.line_items)

