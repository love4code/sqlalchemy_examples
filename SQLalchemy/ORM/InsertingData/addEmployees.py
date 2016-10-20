from db import *
from addTable import Employee

marsha = Employee(name='Marsha')
fred = Employee(name='Fred')

marsha.reports.append(fred)

session.add(marsha)
session.commit()