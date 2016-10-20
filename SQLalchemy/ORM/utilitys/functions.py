from db import *

def get_orders_by_customer(cust_name):
    query = session.query(Order.order_id, User.username, User.phone,
                          Cookie.cookie_name,LineItems.quantity,
                          LineItems.extended_cost)

    query = query.join(User).join(LineItems).join(Cookie)
    results = query.filter(User.username == cust_name).all()
    return results

print([order for order in get_orders_by_customer('cakeeater')])

def retrieve_orders_by_customer(cust_name, shipped=None, details=False):
    query = session.query(Order.order_id, User.username, User.phone)
    query = query.join(User)
    if details:
        query = query.add_columns(Cookie.cookie_name, LineItems.quantity,
                                  LineItems.extended_cost)
        query = query.join(LineItems).join(Cookie)
    if shipped is not None:
        query = query.filter(Order.shipped == shipped)
    results = query.filter(User.username == cust_name).all()

    return results
print([order for order in retrieve_orders_by_customer('cookiemon',
                                                      shipped=True,
                                                      details=True)])