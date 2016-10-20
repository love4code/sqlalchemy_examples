from sqlalchemy import select, update
from sqlalchemy.exc import IntegrityError

from CORE.db_schema import *


def ship_it_1(order_id):

    s = select([line_items.c.cookie_id, line_items.c.quantity])
    s = s.where(line_items.c.order_id == order_id)
    cookies_to_ship = connection.execute(s)
    for cookie in cookies_to_ship:
        u = update(cookies).where(cookies.c.cookie_id == cookie.cookie_id)
        u = u.values(quantity=cookies.c.quantity - cookie.quantity)
        result = connection.execute(u)
    u = update(orders).where(orders.c.order_id == order_id)
    u = u.values(shipped=True)
    result = connection.execute(u)
    print("Shipped order ID: {}".format(order_id))

def ship_it(order_id):

    s = select([line_items.c.cookie_id, line_items.c.quantity])
    s = s.where(line_items.c.order_id == order_id)

    # START TRANSACTION

    transaction = connection.begin()

    cookies_to_ship = connection.execute(s).fetchall()

    try:
        for cookie in cookies_to_ship:
            u = update(cookies).where(cookies.c.cookie_id ==
                                      cookie.cookie_id)
            u = u.values(quantity=cookies.c.quantity-cookie.quantity)

            result = connection.execute(u)
        u = update(orders).where(orders.c.order_id == order_id)
        u = u.values(shipped=True)
        result = connection.execute(u)
        print("Shipped order ID: {}".format(order_id))
        transaction.commit()
    except IntegrityError as error:
        transaction.rollback()
        print("custom:",error)
ship_it(2)