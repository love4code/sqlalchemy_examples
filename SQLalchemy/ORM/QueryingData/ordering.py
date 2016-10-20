from db import *
from sqlalchemy import desc
# If we want our results to be in order, we can chain an order_by()
# statement to our select.

# Order by quantity ascending

for cookie in session.query(Cookie).order_by(Cookie.quantity):
    print('{:3} - {}'.format(cookie.quantity, cookie.cookie_name))

# Order by quantity Descending

for cookie in session.query(Cookie).order_by(desc(Cookie.quantity)):
    print('{:3} - {}'.format(cookie.quantity, cookie.cookie_name))

# The descending function can also be used as a method on a column object
# Such as Cookie.quantity.desc(). However that can be confusing in long
# statements

