from sqlalchemy import insert, select

from CORE.db_schema import *

ins = insert(orders).values(user_id=1, order_id=1)
result = connection.execute(ins)

ins = insert(line_items)
order_items = [
    {
        'order_id':'1',
        'cookie_id':'1',
        'quantity':'2',
        'extended_cost':'2.00'
    },
    {
        'order_id':'1',
        'cookie_id':'3',
        'quantity':'12',
        'extended_cost':'16.00'
    }
]
result = connection.execute(ins, order_items)

ins = insert(orders).values(user_id=2, order_id=2)
result = connection.execute(ins)

ins = insert(line_items)

order_items = [
    {
        'order_id':'2',
        'cookie_id':'1',
        'quantity':'24',
        'extended_cost':'24.00'
    },
    {
        'order_id':'2',
        'cookie_id':'4',
        'quantity':'6',
        'extended_cost':'3.00'
    }
]

result = connection.execute(ins, order_items)

sc = select([cookies])
su = select([users])
so = select([orders])
print([res for res in connection.execute(sc)])
print([res for res in connection.execute(su)])
print([res for res in connection.execute(so)])


ins = insert(orders).values(user_id=3, order_id=4)
result = connection.execute(ins)
print(result.inserted_primary_key)

ins = insert(line_items)

order_items = [
    {
        'order_id':'3',
        'cookie_id':'3',
        'quantity':'12',
        'extended_cost':'16.00'
    },
    {
        'order_id':'3',
        'cookie_id':'4',
        'quantity':'40',
        'extended_cost':'20.00'
    }

]
result = connection.execute("SELECT * FROM line_items").fetchall()
print([res for res in result])

order_items = [
    {
        'order_id':'4',
        'cookie_id':'2',
        'quantity':'6',
        'extended_cost':'3.00'
    },
    {
        'order_id':'4',
        'cookie_id':'3',
        'quantity':'12',
        'extended_cost':'15.00'
    }
]

order_items = [
    {
        'order_id':'5',
        'cookie_id':'4',
        'quantity':'24',
        'extended_cost':'12.00'
    },
    {
        'order_id':'5',
        'cookie_id':'1',
        'quantity':'100',
        'extended_cost':'100.00'
    }
]