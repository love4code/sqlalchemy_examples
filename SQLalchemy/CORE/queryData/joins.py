from db_schema import *
from sqlalchemy import select, func
# |
# | Joins
# |
# | join()
# |
columns = [orders.c.order_id, users.c.username, users.c.phone,
           cookies.c.cookie_name, line_items.c.quantity,
           line_items.c.extended_cost]

cookiemon_orders = select(columns)

cookiemon_orders = cookiemon_orders.select_from(orders.join(users).join(
    line_items).join(cookies)).where(users.c.username == 'cookiemon')

result = connection.execute(cookiemon_orders).fetchall()

print([row for row in result])

# |
# | outerjoin()
# |
# | The table we use the outerjoin method on will be the one from which
# | all results are returned
# |

columns = [users.c.username, func.count(orders.c.order_id)]
all_orders = select(columns)
all_orders = all_orders.select_from(users.outerjoin(orders))
all_orders = all_orders.group_by(users.c.username)
result = connection.execute(all_orders).fetchall()

print(str(all_orders))
# | SELECT users.username, count(orders.order_id) AS count_1
# | FROM users LEFT OUTER JOIN orders ON users.user_id = orders.user_id
# | GROUP BY users.username


print('RESULT:')
print([res for res in result])

# | RESULT:
# | [(u'cakeeater', 1), (u'codeWarrior', 0), (u'cookiemon', 1), (u'pieguy',
# |  0)]

# SQLalchemy allows the use of Aliasing Selectables through the use of
# alias() function or method
# One great fetaur to not is sqlalchemy can pick the alias name for you
# preventing naming collisions

#
#  CHAINING EXERCISE
#
#
def get_orders_by_customer(cust_name):
    """Retrieve a RP object populated with all the orders
       Connected to the customer """
    columns = [orders.c.order_id,
               users.c.username,
               users.c.phone,
               cookies.c.cookie_name,
               line_items.c.quantity,
               line_items.c.extended_cost]

    cust_orders = select(columns)

    cust_orders = cust_orders.select_from(users.join(orders).join(
        line_items).join(cookies))

    cust_orders = cust_orders.where(users.c.username == cust_name)

    return connection.execute(cust_orders).fetchall()

print([res for res in get_orders_by_customer('cookiemon')])

#RESULTS:
#
#[
#(1, u'cookiemon', u'111-111-1111', u'peunt butter', 2, Decimal('2.00')),
#(1, u'cookiemon', u'111-111-1111', u'chocolate chip', 12, Decimal('16.00'))
#]
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
print("get_orders_by_customer_name('cakeeater',shipped=False)")
print([res for res in get_orders_by_customer_name('cakeeater',
                                                  shipped=False)])
print("get_orders_by_customer_name('cakeeater',shipped=False,details=True)")
print([res for res in get_orders_by_customer_name('cakeeater',
                                                  shipped=False,
                                                  details=True)])

# +-----------------------------------------------------+
# |                                                     |
# |    Stepping Through The Joins                       |
# |                                                     |
# |    Order of joins matters                           |
# |                                                     |

columns = [orders.c.order_id,
           users.c.username,
           users.c.phone,
           cookies.c.cookie_name,
           line_items.c.quantity,
           line_items.c.extended_cost]

all_orders = select(columns)
# SELECT FROM
# users (user_id)
# orders where (orders.user_id) == (users.user_id)
# line_items where (line_items.order_id) == (orders.order_id)
# cookies where (cookies.cookie_id) == (line_items.cookie_id)

all_orders = all_orders.select_from(users.join(orders).join(
    line_items).join(cookies))
# WHERE
# users (users.username) == 'codeWarrior'
all_orders = all_orders.where(users.c.username ==
                              'codeWarrior')

print([res for res in connection.execute(all_orders).fetchall()])