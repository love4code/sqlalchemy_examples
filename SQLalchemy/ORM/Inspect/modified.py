from session_db import *
from inspect import cc_cookie
from sqlalchemy import inspect


session.add(cc_cookie)

cc_cookie.cookie_name = 'Change chocolate chip'
insp = inspect(cc_cookie)
print(insp.modified)

# We can use the inspectors attr collection to find out what has changed

for attr, attr_state in insp.attrs.items():
    # checks the attribute state to see if there has been changes
    if attr_state.history.has_changes():
        print('{}: {}'.format(attr,attr_state.value))
        # Prints the history object of the changed attribute
        print('History: {}\n'.format(attr_state.history))