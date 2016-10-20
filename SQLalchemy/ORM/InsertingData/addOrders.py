from db import *

# To associate one object with another , just assign it to the relationship
# property.

# Create an empty Order instance
o1 = Order()

# Set user property to the cookiemon instance
o1.user = session.query(User).filter(User.username == 'cookiemon').one()

# Add it to the session
session.add(o1)

# Then we query for the chocolate chip cookie
cc = session.query(Cookie).filter(Cookie.cookie_name == "chocolate "
                                                        "chip").one()

# And set the cookie to be the chocolate chip one we just queried for
line1 = LineItems(cookie=cc, quantity=2,extended_cost=1.00)
# Repeat process for 2nd line item in the order
pb = session.query(Cookie).filter(Cookie.cookie_name == "penut butter").one()

line2 = LineItems(quantity=12, extended_cost=3.00)
line2.cookie = pb
line2.order = o1

o1.line_items.append(line1)
o1.line_items.append(line2)

session.commit()
o2 = Order()
session.add(o2)


o2.user = session.query(User).filter(User.username =='cakeeater').one()
cc = session.query(Cookie).filter(Cookie.cookie_name == "chocolate "
                                                        "chip").one()
line1 = LineItems(cookie=cc,quantity=24, extended_cost=12.00)

oat = session.query(Cookie).filter(Cookie.cookie_name == "oatmeal " \
                                                       "raisin").one()
line2 = LineItems(cookie=oat,quantity=6, extended_cost=6.00)

o2.line_items.append(line1)
o2.line_items.append(line2)


session.commit()
