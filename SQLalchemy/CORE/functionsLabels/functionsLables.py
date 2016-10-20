from sqlalchemy.sql import func, select

from CORE.db_schema import *

# importing 'func' helps prevent any naming collisions that could occur
#    with pythons built in sum method
# +-----------------------------------------------------------------------+
# |  sum()                                                                |
# +-----------------------------------------------------------------------+

s = select([func.sum(cookies.c.quantity)])
rp = connection.execute(s)
print(rp.scalar())

#RETURNS:  137

# Remember scalar will return only the left most column in the first record

# +-----------------------------------------------------------------------+
# |  count()                                                              |
# +-----------------------------------------------------------------------+

s = select([func.count(cookies.c.cookie_name)])
rp = connection.execute(s)
record = rp.first()
print(record.keys())
#RETURNS: [u'count_1']

print(record.count_1)
#RETURNS:  4

# +-----------------------------------------------------------------------+
# | The problem here is the naming convention for the key that we need to |
# |  reference the column from.                                           |
# | Luckily There is a Solution.                                          |
# |                                                                       |
# |  Its called Labels!!!                                                 |
# +-----------------------------------------------------------------------+
# +-----------------------------------------------------------------------+
# |  label()                                                              |
# +-----------------------------------------------------------------------+

s = select([func.count(cookies.c.cookie_name).label('inventory_count')])
rp = connection.execute(s)
record = rp.first()
print(record.keys())

#RETURNS: [u'inventory_count']

print(record.inventory_count)

#RETURNS: 4

# +-----------------------------------------------------------------------+
# |  Notice we just use the label() function on the Column object we want |
# |  to change.                                                           |
# +-----------------------------------------------------------------------+

# +-----------------------------------------------------------------------+
# |  FILTERING    where()                                                 |
# +-----------------------------------------------------------------------+

s = select([cookies]).where(cookies.c.cookie_name == 'chocolate chip')
rp = connection.execute(s)
record = rp.first()
print(record.items())

#RETURNS:  [
#               ('cookie_id', 1),
#               ('cookie_name', u'chocolate chip'),
#               ('cookie_recipe_url',
#                   u'http://some.awesome.me/cookie/recipe.html'),
#               ('cookie_sku', u'CC01'),
#               ('quantity', 12),
#               ('unit_cost', Decimal('0.50'))
#           ]

# +-----------------------------------------------------------------------+
# |  FILTERING Contains Word   where()  like()                            |
# +-----------------------------------------------------------------------+

s = select([cookies]).where(cookies.c.cookie_name.like('%chocolate%'))
rp = connection.execute(s)
for record in rp.fetchall():
    print(record.cookie_name)

#RETURNS:  chocolate chip
#          dark chocolate chip

# +-----------------------------------------------------------------------+
# |  ClauseElements                                                       |
# |  To Be Used Inside Where() Statement                                  |
# +------------------+----------------------------------------------------+
# |                  |                                                    |
# |  METHOD          |      PURPOSE                                       |
# |------------------+----------------------------------------------------+
# |                  |                                                    |
# | between('cleft', |   Find where the column is between 'cleft' and     |
# |         'cright')|   'cright'                                         |
# |..................+....................................................|
# |                  |                                                    |
# | concat(          |   Concatenate column with column_two               |
# |     column_two)  |                                                    |
# |..................+....................................................|
# |                  |                                                    |
# | distinct()       |   Find only Unique values for the column           |
# |..................+....................................................|
# |                  |                                                    |
# | in_([list])      |   Find where the column is in the list             |
# |..................+....................................................|
# |                  |                                                    |
# | is_(None)        |   Find where the column is None (commonly used for |
# |                  |   Null checks with None                            |
# |..................+....................................................|
# |                  |                                                    |
# | contains(string) | Find where the column has STRING in it             |
# |                  | (Case Sensitive)                                   |
# |..................+....................................................|
# |                  |                                                    |
# | endswith(string) | Find where the column end with STRING              |
# |                  | (Case Sensitive)                                   |
# |..................+....................................................|
# |                  |                                                    |
# | like(string)     | Find where column is like STRING                   |
# |                  | (Case Sensitive)                                   |
# |..................+....................................................|
# |                  |                                                    |
# | startswith(      | Find where the column begins with STRING           |
# |         string)  | (Case Sensitive)                                   |
# |..................+....................................................|
# |                  |                                                    |
# | ilike(string)    | Find where the column is like STRING               |
# |                  | (Not Case Sensitive)                               |
# |..................+....................................................|
# |                                                                       |
# +-----------------------------------------------------------------------+
# |  There is also negative versions of these methods                     |
# |                                                                       |
# |  notlike_()                                                           |
# |  notin_()                                                             |
# |  isnot() 'breaks the not<method> naming convention'                   |
# +-----------------------------------------------------------------------+

# +-----------------------------------------------------------------------+
# | CONJUCTIONS it is more readable and functional then chaining together |
# |  where() clauses                                                      |
# |                                                                       |
# | and_()                                                                |
# | or_()                                                                 |
# | not_()
# +-----------------------------------------------------------------------+

from sqlalchemy import and_, or_

#--------------- or_() -------------------------------
s = select([cookies]).where(

    or_(

        cookies.c.quantity.between(10,50),
        cookies.c.cookie_name.contains('chip')
    )
)

for row in connection.execute(s):
    print(row.cookie_name)

#--------------- and_() -----------------------------
s = select([cookies]).where(
    and_(
        cookies.c.quantity > 23,
        cookies.c.unit_cost < 0.40
    )
)

for row in connection.execute(s):
    print(row.cookie_name)

#RESULTS IN:

# chocolate chip
# dark chocolate chip
# penut butter

