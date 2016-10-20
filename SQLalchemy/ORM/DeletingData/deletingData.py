from db import *
# +-----------------------------------------------------------------------+
# | Delete statements can be created either by the delete() function      |
# | or by the delete() method of the Table being updated                  |
# |                                                                       |
# | You can delete all row of a Table by leaving off the where() clause   |
# |
# | Unlike Insert and Update, Delete() takes No Params
# |       Only an Optional Where Clause
# |
# +-----------------------------------------------------------------------+
query = session.query(Cookie)
query = query.filter(Cookie.cookie_name == "dark chocolate chip")

dcc_cookie = query.one()
session.delete(dcc_cookie)
session.commit()

dcc_cookie = query.first()
print(dcc_cookie)
# Its also possible to delete data in place without having the object
query = session.query(Cookie)
query = query.filter(Cookie.cookie_name == "molasses")
query.delete()
mol_cookie = query.first()

print(mol_cookie)