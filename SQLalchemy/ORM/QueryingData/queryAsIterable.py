from db import *
# We dont append an all() when using an iterable
for cookie in session.query(Cookie):
    print(cookie)

# Using the iterable approach allows us to interact with each record
# object individually, release it, and get the next object