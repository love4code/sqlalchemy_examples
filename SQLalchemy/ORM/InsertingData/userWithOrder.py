from session_db import *

cookiemon = User('cookiemon','mon@cookie.com','111-111-1111','password')

session.add(cookiemon)

o1 = Order()
o1.user = cookiemon
session.add(o1)

cc = session.query(Cookie).filter(\
    Cookie.cookie_name == 'Change chocolate chip').one()
line1 = LineItem(order=o1, cookie=cc, quantity=2,extended_cost=1.00)

session.add(line1)
session.commit()