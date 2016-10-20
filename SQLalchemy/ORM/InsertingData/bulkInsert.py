from db import *

c1 = Cookie(cookie_name='penut butter',
            cookie_recipe_url='http://some.awesome.me/cookie/recipe'
                              '/pb_recipe.html',
            cookie_sku='PB01',
            quantity=24,
            unit_cost=0.25)
c2 = Cookie(cookie_name='oatmeal raisin',
            cookie_recipe_url='http://some.awesome.me/cookie/recipe'
                              '/or_recipe.html',
            cookie_sku='OR01',
            quantity=100,
            unit_cost=1.00)
session.bulk_save_objects([c1,c2])
session.commit()

# This method is quite faster then performing multiple individual adds and
# inserts. This speed does come at an expense. We lose some features we get
# in the normal add and commit such as.

# Relationship settings and actions are not respected or triggered
#
# The objects are not connected to the session
#
# Fetching primary keys is not done by default
#
# No events will be triggered

# In addition to bulk_save_objects there are additional methods to create
# and update objects via a dictionary.
# Check out the sqlalchemy documentation

# If your inserting multiple records and dont need access to relationships
# or inserted primary keys, use bulk_save_object or its related methods