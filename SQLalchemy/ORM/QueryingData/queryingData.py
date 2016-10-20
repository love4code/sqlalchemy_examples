#! /usr/bin/python2.7
from db import *

# Return a list of cookie instances that represent all the records in the
#  cookies table
cookies = session.query(Cookie).all()
print(cookies)