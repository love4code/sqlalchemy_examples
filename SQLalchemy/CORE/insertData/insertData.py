# REMEMBER TO IMPORT MODULES THAT PERTAIN TP YOU BD ENGINE / CONNECTION
#    ->BEFORE ATTEMPTING TO USE THESE STATEMENTS.

# YOU CAN USE THE ' db_schema.py ' FILE FROM THIS ROOT DIR

# ENTER THESE CODE SAMPLES INTO YOUR
#   -> PYTHON SHELL WITH db_schema import * at Top

from CORE.db_schema import *

# +------------------------------------------------------------------------+
# |                                                                        |
# |  First we will built a simple insert statement to insert a             |
# |  cookie flavor into the database                                       |
# |  We will be using the insert method of the Table Object                |
# |                                                                        |
# +------------------------------------------------------------------------+


ins = cookies.insert().values(
    cookie_name="chocolate chip",
    cookie_recipe_url="http://some.awesome.me/cookie/recipe.html",
    cookie_sku="CC01",
    quantity="100",
    unit_cost="0.50"
)

# +------------------------------------------------------------------------+
# |                                                                        |
# |  Another way to achieve the same results is to use the                 |
# |  Insert command as a standalone function                               |
# |  This is a more generative approach                                    |
# |                                                                        |
# +------------------------------------------------------------------------+

ins = cookies.insert()

result = connection.execute(
    ins,
    cookie_name='dark chocolate chip',
    cookie_recipe_url='http://some.awesome.me/cookie/dc_recipe.html',
    cookie_sku='CC02',
    quantity='25',
    unit_cost='1.00'
)
result.inserted_primary_key

# +-----------------------------------------------------------------------+
# |                                                                       |
# |         To get a preview of our INSERT use the print(str(ins))        |
# |                                                                       |
# +-----------------------------------------------------------------------+

print(str(ins))

# +-----------------------------------------------------------------------+
# | INPUT:                                                                |
# |_______________________________________________________________________|
# |                                                                       |
# |  print(str(ins))                                                      |
# |_______________________________________________________________________|
# |                                                                       |
# | OUTPUT:                                                               |
# |_______________________________________________________________________|
# |                                                                       |
# | INSERT INTO cookies (cookie_name, cookie_recipe_url, cookie_sku,      |
# |  quantity, unit_cost)                                                 |
# | VALUES (:cookie_name, :cookie_recipe_url, :cookie_sku, :quantity,     |
# |  :unit_cost)                                                          |
# |                                                                       |
# +-----------------------------------------------------------------------+

# +-----------------------------------------------------------------------+
# |                                                                       |
# |  Our parameters are replaced with :column_name                        |
# |  To view the parameters through th SQLCompiler Object                 |
# |  Which gives us acces to the actual parameters to be sent             |
# |                                                                       |
# +-----------------------------------------------------------------------+

ins.compile().params

# +-----------------------------------------------------------------------+
# | INPUT:                                                                |
# |_______________________________________________________________________|
# |                                                                       |
# |  ins.compile().params                                                 |
# |_______________________________________________________________________|
# |                                                                       |
# | OUTPUT:                                                               |
# |_______________________________________________________________________|
# |                                                                       |
# |  {                                                                    |
# |   'cookie_name': 'chocolate chip',                                    |
# |   'cookie_recipe_url': 'http://some.awesome.me/cookie/recipe.html',   |
# |   'cookie_sku': 'CC01',                                               |
# |   'quantity': '100',                                                  |
# |   'unit_cost': '0.50'                                                 |
# |  }                                                                    |
# |                                                                       |
# +-----------------------------------------------------------------------+

# +-----------------------------------------------------------------------+
# |                                                                       |
# |  Now that we have a complete picture of the INSERT statement          |
# |  We can use the EXECUTE method on our CONNECTION to send the          |
# |  Data to the DataBase WHich will insert the record into the Table     |
# |                                                                       |
# +-----------------------------------------------------------------------+

rp = connection.execute(ins)


# +-----------------------------------------------------------------------+
# |                                                                       |
# |  We can also get the ID of the record we just Inserted by accessing   |
# |  The inserted_primary_key attribute                                   |
# |                                                                       |
# +-----------------------------------------------------------------------+

rp.inserted_primary_key

# +-----------------------------------------------------------------------+
# | INPUT:                                                                |
# |_______________________________________________________________________|
# |                                                                       |
# |  rp.inserted_primary_key                                              |
# |_______________________________________________________________________|
# |                                                                       |
# | OUTPUT:                                                               |
# |_______________________________________________________________________|
# |                                                                       |
# |  [0]                                                                  |
# |                                                                       |
# +-----------------------------------------------------------------------+

# +-----------------------------------------------------------------------+
# |                                                                       |
# |  We can insert multiple records at once by using a list               |
# |  Of Dictionaries                                                      |
# |                                                                       |
# |  Its important to note that your dictionary keys must match           |
# |  Because the insert statement is created from the first Dictionary    |
# |                                                                       |
# +-----------------------------------------------------------------------+

inventory_list = [
    {
        'cookie_name': 'penut butter',
        'cookie_recipe_url': 'http://some.awesome.me/cookie/pb_recipe.html',
        'cookie_sku': 'PB01',
        'quantity': '25',
        'unit_cost': '1.25'
    },
    {
        'cookie_name': 'oatmeal rasin',
        'cookie_recipe_url': 'http://some.awesome.me/cookie/or_recipe.html',
        'cookie_sku': 'OR01',
        'quantity': '125',
        'unit_cost': '0.75'
    },
    {
        'cookie_name': 'chocolate chip',
        'cookie_recipe_url': 'http://some.awesome.me/cookie/cc_recipe.html',
        'cookie_sku': 'CC01',
        'quantity': '12',
        'unit_cost': '0.50'
    },
    {
        'cookie_name': 'dark chocolate chip',
        'cookie_recipe_url': 'http://some.awesome.me/cookie/dc_recipe.html',
        'cookie_sku': 'CC02',
        'quantity': '1',
        'unit_cost': '0.75'
    }
]

result = connection.execute(ins, inventory_list)