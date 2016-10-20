from db import *
from sqlalchemy import func
query = session.query(Order.order_id, User.username, User.phone,
                      Cookie.cookie_name, LineItems.quantity,
                      LineItems.extended_cost)

query = query.join(User).join(LineItems).join(Cookie)

results = query.filter(User.username == 'cookiemon').all()

print(results)

# OUTERJOINS
# Grouping

query = session.query(User.username, func.count(Order.order_id))
query = query.outerjoin(Order).group_by(User.username)
for row in query:
    print(row)

