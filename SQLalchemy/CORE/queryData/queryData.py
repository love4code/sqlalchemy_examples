# To start building a query we need to use the 'select' method
# The 'Select Method' ecpects a list of Columns to Select but
# For Convenience Accepts Table Objects

# 'rp' stands for ResultProxy
# ResultProxy is a wrapper around DBAPI cursor object
# ResultProxy allows acces using Index, Name, or Column Object
#   -> (cookies.c.cookie_name)

from sqlalchemy.sql import select

from CORE.db_schema import *

s = select([cookies])

rp = connection.execute(s)

results = rp.fetchall()


# There is also a select method of the Table Object
s = cookies.select()
rp = connection.execute(s)
results = rp.fetchall()

first_row = results[0]
first_row[1]
first_row.cookie_name
first_row[cookies.c.cookie_name]

# +-----------------------------------------------------------------------+
# |  RESULT:                                                              |
# |                                                                       |
# |   u 'chocolate chip'                                                  |
# +-----------------------------------------------------------------------+

# +-----------------------------------------------------------------------+
# |  ResultProxy can be used as an iterable                               |
# |                                                                       |
# |   for result in rp:                                                   |
# |       print(result)                                                   |
# +-----------------------------------------------------------------------+

# +-----------------------------------------------------------------------+
# |  Other methods of the resultProxy are:                                |
# |-----------------------------------------------------------------------|
# |                                                                       |
# |   first() : Returns the first record if exists then closes connection |
# |                                                                       |
# |   fetchone() : Returns one row and leaves cursor open for you to make |
# |                additional fetch calls.                                |
# |                                                                       |
# |   scalar() : Returns a single value is a query results in a single    |
# |              record with one Column.                                  |
# |                                                                       |
# |   keys() : Returns the keys of the object                             |
# |                                                                       |
# |   items() : Returns a list of colums and values                       |
# +-----------------------------------------------------------------------+


# +-----------------------------------------------------------------------+
# |  Limit the Columns Returned                                           |
# |                                                                       |
# |   !this will help with memory consumption!                            |
# |                                                                       |
# | To limit the fields that are returned from a query we need to pass    |
# |   the columns we want into the 'select() method constructor as a list.|
# |                                                                       |
# +-----------------------------------------------------------------------+
# |  SELECT cookie_name, quantity                                         |
# |  FROM cookies                                                         |
# |_______________________________________________________________________|
# |                                                                       |
# |   s = select([cookies.c.cookie_name, cookies.c.quantity])             |
# |   rp = connection.execute(s)                                          |
# |                                                                       |
# |   print(rp.keys())                                                    |
# |   RETURNS: ['cookie_name', 'quantity']                                |
# |                                                                       |
# |   result = rp.first()                                                 |
# |                                                                       |
# |   print(result)                                                       |
# |   RETURNS:(u'chocolate chip', 12)                                     |
# +-----------------------------------------------------------------------+

s = select([cookies.c.cookie_name, cookies.c.quantity])

rp = connection.execute(s)

print(rp.keys())
#RETURNS: ['cookie_name', 'quantity']

result = rp.first()

print(result)
#RETURNS: (u'chocolate chip', 12)

# +-----------------------------------------------------------------------+
# |  order_by()                                                           |
# +-----------------------------------------------------------------------+
s = select([cookies.c.cookie_name, cookies.c.quantity])
s = s.order_by(cookies.c.quantity)
rp = connection.execute(s)

for cookie in rp:
    print('{} - {}'.format(cookie.quantity,cookie.cookie_name))

#RETURNS:
#
# 1 - dark chocolate chip
# 12 - chocolate chip
# 24 - penut butter
# 100 - oatmeal raisin

# +-----------------------------------------------------------------------+
# |  order_by() desc()                                                    |
# +-----------------------------------------------------------------------+

from sqlalchemy import desc
s = select([cookies.c.cookie_name, cookies.c.quantity])
s = s.order_by(desc(cookies.c.quantity))

# Notice we are wrapping the 'cookies.c.quantity' column in the desc()
#   -> function.

# The desc() function can also be used as a method on a Column
# ie. cookies.c.quantity.desc()
# This approach is less readable and a bit more confusing to read in long
#  -> statements.

# +-----------------------------------------------------------------------+
# |  limit()                                                              |
# +-----------------------------------------------------------------------+

s = select([cookies.c.cookie_name, cookies.c.quantity])
s = s.order_by(cookies.c.quantity)
s = s.limit(2)

rp = connection.execute(s)

print([result.cookie_name for result in rp])

#RETURNS: [u 'dark chocolate chip', u 'chocolate chip']