from db import *
# +-----------------------------------------------------------------------+
# | Update statements can be created either by the update() function      |
# | or by the update() method of the Table being updated                  |
# |                                                                       |
# | You can update all row of a Table by leaving off the where() clause   |
# +-----------------------------------------------------------------------+
query = session.query(Cookie)
cc_cookie = query.filter(Cookie.cookie_name == "chocolate chip").first()
cc_cookie.quantity = cc_cookie.quantity + 120
session.commit()
print('{} - {:3}'.format(cc_cookie.cookie_name,cc_cookie.quantity))
# Its also possible to update data without having the object originally

query = session.query(Cookie)
query = query.filter(Cookie.cookie_name == "chocolate chip")
# The update methos causes the record to be updated outside of the session
# and return the number of rows updated
query.update({Cookie.quantity:Cookie.quantity - 20})
# We are reusing 'query' here because it has the same selection criteria
# we need
cc_cookie = query.first()

print('{} - {:3}'.format(cc_cookie.cookie_name,cc_cookie.quantity))