from db import *
# Filtering queries is done by appending filter() statements to a query

# A tipical filter clause has a Column, an Operator, and a Value or a Column.

# It is possible to chain multiple filter() clauses or a comma separated
# mutiple ClauseElement expresions in a single filter. They will act as ANDs
# in Traditional SQL

record = session.query(Cookie).filter(Cookie.cookie_name == 'chocolate '
                                                            'chip').first()
print(record)

# There is also a filter_by() method that works similarly to the filter()
# method except instead of explicity providing the class as part of the
# filter expression it uses attribute keyword expressions from the primary
# entity of the query or the last entity that was joined to the statement.
# It also uses a keyword assignment instead of a Boolean.

record = session.query(Cookie).filter_by(cookie_name='dark chocolate '
                                                     'chip').first()
print(record)

# Another way of filtering is using the like() method that is available on
# ClauseElements

query = session.query(Cookie).filter(Cookie.cookie_name.like('%chocolate%'))
for record in query:
    print(record.cookie_name)


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

# Use the filter() method with multiple ClauseElement expressions
# To preform an AND
query = session.query(Cookie).filter(
    Cookie.quantity > 23,
    Cookie.unit_cost < 0.40
)
for result in query:
    print(result.cookie_name)
    print(result.unit_cost)

# The or_() functio works opposite of and includes results that either one
# of the supplied clauses

from sqlalchemy import and_,or_, not_

query = session.query(Cookie).filter(
    or_(
        Cookie.quantity.between(10,50),
        Cookie.cookie_name.contains('chip')
    )
)

for result in query:
    print(result.cookie_name)