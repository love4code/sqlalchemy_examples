from db import *
cookiemon = User(username='cookiemon',
                 email_address='mon@cookie.com',
                 phone='111-111-1111',
                 password='password')
cakeeater = User(username='cakeeater',
                 email_address='cake@cookie.com',
                 phone='222-222-2222',
                 password='password')
pieperson = User(username='pieperson',
                 email_address='pie@cookie.com',
                 phone='333-333-3333',
                 password='password')

session.add(cookiemon)
session.add(cakeeater)
session.add(pieperson)
session.commit()