from sqlalchemy import Table, Column, Integer, Numeric, String, DateTime,\
    ForeignKey, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from datetime import datetime
# We imported the 'relationship' and 'backref' methods from sqlalchemy.orm
Base = declarative_base()

class Order(Base):
    __tablename__ = 'orders'
# We are defining a ForeignKey
    order_id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey('users.user_id'))
    shipped = Column(Boolean(),default=False)
# This establishes a One To Many relationship
    user = relationship("User", backref=backref('orders',
                                                order_by=order_id))