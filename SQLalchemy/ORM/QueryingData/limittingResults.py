from db import *
# To limit the fields that are returned from a query, we need to pass
# in the columns we want in the query() method constructor separated by
# columns.
print(session.query(Cookie.cookie_name,Cookie.quantity).first())

# The output from the query where we sullpy the column names is a tuple of
# those column values

# We can use an array slice notation to actally issue a limit statement as
# part of out query
query = session.query(Cookie).order_by(Cookie.quantity).limit(2)
print("LIMIT 2:")
print([result.cookie_name for result in query])