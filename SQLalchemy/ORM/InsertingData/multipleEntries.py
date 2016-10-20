from db import *

dcc = Cookie(cookie_name='dark chocolate chip',
             cookie_recipe_url='http://some.awesome.me/cookie/recipe'
                               '/dcc_recipe.html',
             cookie_sku='CC02',
             quantity=1,
             unit_cost=0.75)

mol = Cookie(cookie_name='molasses',
             cookie_recipe_url='http://some.awesome.me/cookie/recipe'
                               '/mol_recipe.html',
             cookie_sku='MOL01',
             quantity=1,
             unit_cost=0.80)

session.add(dcc)
session.add(mol)
# flush() method doesnt do a database commit and end the transaction
# the ojects are still attached to the session for further use without
# extra queries
session.flush()
print(dcc.cookie_id)
print(mol.cookie_id)