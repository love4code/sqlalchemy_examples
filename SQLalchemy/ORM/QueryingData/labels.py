from db import *
# Two common databasef unctions re SUM() and COUNT()
from sqlalchemy import func

inv_count = session.query(func.sum(Cookie.quantity)).scalar()
# Notice the use of scalar() which will return only the left most column in
# the first record
print(inv_count,' cookies')

rec_count = session.query(func.count(Cookie.cookie_name)).first()
print(rec_count, 'Different Types')

# Unlike the first example we return a tuple for us to use. As we used the
#     first() method instead of scalar()

# Using functions such as count and sum will end up returning tuples or
# results with column names line column_1, ex. the 4th count function
# would be count_4
# SqlAlchemy fixes this by use of the label() function

rec_count = session.query(func.count(Cookie.cookie_name).label(
    'inventory_count')).first()
print(rec_count.keys())
print(rec_count.inventory_count)