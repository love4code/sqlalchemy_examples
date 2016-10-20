from db_schema import *
from sqlalchemy import insert

customer_list = [
    {
        'username':'cookiemon',
        'email_address':'mon@cookie.com',
        'phone':'111-111-1111',
        'password':'password'
    },
    {
        'username':'cakeeater',
        'email_address':'cake@cookie.com',
        'phone':'222-222-2222',
        'password':'password'
    },
    {
        'username':'pieguy',
        'email_address':'pieguy@cookie.com',
        'phone':'333-333-3333',
        'password':'password'
    },
    {
        'username':'codeWarrior',
        'eamil_address':'codeWarrior@cookie.com',
        'phone':'444-444-4444',
        'password':'password'
    }
]

ins = users.insert()
result = connection.execute(ins, customer_list)

print(result.rowcount)