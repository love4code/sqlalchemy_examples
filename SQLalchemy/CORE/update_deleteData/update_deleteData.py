from db_schema import *
from sqlalchemy import update, select

# +-----------------------------------------------------------------------+
# | Update statements can be created either by the update() function      |
# | or by the update() method of the Table being updated                  |
# |                                                                       |
# | You can update all row of a Table by leaving off the where() clause   |
# +-----------------------------------------------------------------------+

u = update(cookies).where(cookies.c.cookie_name == "chocolate chip")
u = u.values(
    quantity=(cookies.c.quantity + 120)
)
result = connection.execute(u)
print(result.rowcount)

#RESULTS: 1

# Rowcount returns the number of rows updated

# To retrieve the updated row

s = select([cookies]).where(cookies.c.cookie_name == "chocolate chip")

result = connection.execute(s).first()

for key in result.keys():
    print('{:>20}:{}'.format(key, result[key]))

#RESULTS:
#            cookie_id:1
#          cookie_name:chocolate chip
#    cookie_recipe_url:http://some.awesome.me/cookie/recipe.html
#           cookie_sku:CC01
#             quantity:132
#            unit_cost:0.50

from sqlalchemy import delete
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

u = delete(cookies).where(cookies.c.cookie_name == 'dark chocolate chip')
result = connection.execute(u)

print(result.rowcount)
#1
s = select([cookies]).where(cookies.c.cookie_name == 'dark chocolate chip')
results = connection.execute(s).fetchall()

print(len(results))
#0

s = select([cookies])
print([res for res in connection.execute(s)])

#RESULTS:
#  [
#   (1, u'peunt butter',
#    u'http://some.awesome.me/cookie/pb_recipe.html',
#    u'PB01',
#    15,
#    Decimal('1.00')),
#   (2, u'oatmeal rasin',
#    u'http://some.awesome.me/cookie/or_recipe.html',
#    u'OR01',
#    15,
#    Decimal('0.50')),
#   (3, u'chocolate chip',
#    u'http://some.awesome.me/cookie/cc_recipe.html',
#    u'CC01',
#    145,
#    Decimal('1.25'))
#  ]