from db_schema import *
from sqlalchemy import insert,select, func
#print([res for res in connection.execute(select([line_items])).fetchall()])
def get_orders_by_customer_name(cust_name, shipped=None, details=False):
    """Return Orders Connected To Customer Name"""
    columns = [orders.c.order_id,
               users.c.username,
               users.c.phone]
    joins = users.join(orders)
    if details:
        columns.extend([cookies.c.cookie_name,
                        line_items.c.quantity,
                        line_items.c.extended_cost])
        joins = joins.join(line_items).join(cookies)
    cust_orders = select(columns)
    cust_orders = cust_orders.select_from(joins)
    cust_orders = cust_orders.where(users.c.username == cust_name)
    if shipped is not None:
        cust_orders = cust_orders.where(orders.c.shipped == shipped)
    result = connection.execute(cust_orders).fetchall()
    return result
print("get_orders_by_customer_name('cakeeater')")
print([res for res in get_orders_by_customer_name('cakeeater')])
#RESULTS:get_orders_by_customer_name('cakeeater')
# [(2, u'cakeeater', u'222-222-2222')]
print("get_orders_by_customer_name('cakeeater',details=True)")
print([res for res in get_orders_by_customer_name('cakeeater',
                                             details=True)])
#RESULTS: get_orders_by_customer_name('cakeeater',details=True)
# [(2, u'cakeeater', u'222-222-2222', u'peunt butter', 24,
# Decimal('24.00')),
# (2, u'cakeeater', u'222-222-2222', u'dark chocolate chip', 6,
# Decimal('3.00'))]
print("get_orders_by_customer_name('cakeeater',shipped=True)")
print([res for res in get_orders_by_customer_name('cakeeater',
shipped=True)])
#RESULTS:
# []
print("get_orders_by_customer_name('cakeeater',shipped=False)")
print([res for res in get_orders_by_customer_name('cakeeater',
                                                  shipped=False)])
# RESULTS:
# [(2, u'cakeeater', u'222-222-2222')]
print("get_orders_by_customer_name('cakeeater',shipped=False,details=True)")
print([res for res in get_orders_by_customer_name('cakeeater',
                                                  shipped=False,
                                                  details=True)])
# RESULTS:
# [
# (2, u'cakeeater', u'222-222-2222', u'peunt butter', 24, Decimal('24.00')),
# (2, u'cakeeater', u'222-222-2222', u'dark chocolate chip', 6,
# Decimal('3.00'))
# ]