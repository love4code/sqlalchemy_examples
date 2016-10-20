from db import *
cc_cookie = Cookie(cookie_name='chocolate chip',
                   cookie_recipe_url='http://some.awesome.me/cookie'
                                     '/recipe/cc_recipe.html',
                   cookie_sku='CC01',
                   quantity=12,
                   unit_cost=0.50)
session.add(cc_cookie)
session.commit()

print(cc_cookie.cookie_id)
