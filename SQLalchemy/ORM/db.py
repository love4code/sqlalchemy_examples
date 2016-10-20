from Sessions.sessions import *
from sqlalchemy import Table, Column, Integer, Numeric, String, DateTime,\
    ForeignKey, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from datetime import datetime

# Create an instance of the declarative_base
Base = declarative_base()
# inherit from the Base
class Cookie(Base):
    """Define a Cookies Table"""
    # Define a table name
    __tablename__ = 'cookies'
    # Define a Attribute and set it to be a primary_key
    cookie_id = Column(Integer(), primary_key=True)
    cookie_name = Column(String(50), index=True)
    cookie_recipe_url = Column(String(255))
    cookie_sku = Column(String(55))
    quantity = Column(Integer())
    unit_cost = Column(Numeric(12, 2))

    def __repr__(self):
        return "Cookie(cookie_name='{self.cookie_name}',"\
                        "cookie_recipe_url='{self.cookie_recipe_url}',"\
                        "cookie_sku='{self.cookie_sku}',"\
                        "quantity='{self.quantity}',"\
                        "unit_cost='{self.unit_cost}')".format(self=self)

# to varify type Cookies.__table__ into the prompt


# Table('cookies', MetaData(bind=None),

# Column('cookie_id', Integer(),
# table=<cookies>, primary_key=True, nullable=False),

# Column('cookie_name', String(length=50),
# table=<cookies>),

# Column('cookie_recipe_url', String(length=255),
# table=<cookies>),

# Column('cookie_sku', String(length=55),
# table=<cookies>),

# Column('quantity', Integer(),
# table=<cookies>),

# Column('unit_cost', Numeric(precision=12, scale=2),
# table=<cookies>), schema=None)

class User(Base):
    """Create a User table"""
    __tablename__ = 'users'
    # Defining Keys and Constraints using __table_args__
    #__table_arge_ = (ForeignKeyConstraint(['user_id'],
    #                                     ['other_table.other_id']),
    #                 CheckConstraint(unit_cost >= '0.00',
    #                                 name='unit_cost_positive'))
    user_id = Column(Integer(), primary_key=True)
    username = Column(String(15), nullable=False, unique=True)
    email_address = Column(String(255), nullable=False)
    phone = Column(String(20), nullable=False)
    password = Column(String(25), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now,
                        onupdate=datetime.now)

    def __repr__(self):
        return "User(username='{self.username}',"\
                        "email_address='{self.email_address}',"\
                        "phone='{self.phone}',"\
                        "password='{self.password}')".format(self=self)

class Order(Base):
    __tablename__ = 'orders'

    order_id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(),ForeignKey('users.user_id'))
    shipped = Column(Boolean(),default=False)
    # Establish a One to Many Relationship with the User class
    # SQLalchemy knows to use our ForeignKey we defined
    user = relationship("User", backref=backref('orders',
                                                order_by=order_id))

    def __repr__(self):
        return "Order(user_id='{self.user_id}',"\
                        "shipped='{self.shipped}')".format(self=self)

class LineItems(Base):
    __tablename__ = 'line_items'

    line_item_id = Column(Integer(), primary_key=True)
    order_id = Column(Integer(), ForeignKey('orders.order_id'))
    cookie_id = Column(Integer(), ForeignKey('cookies.cookie_id'))
    quantity = Column(Integer())
    extended_cost = Column(Numeric(12, 2))

    order = relationship("Order", backref=backref('line_items',
                                                  order_by=line_item_id))
    # ESTABLISH a One to One relationship
    cookie = relationship("Cookie", uselist=False, order_by=cookie_id)

    def __repr__(self):
        return "LineItems(order_id='{self.order_id}',"\
                            "cookie_id='{self.cookie_id}',"\
                            "quantity='{self.quantity}',"\
                            "extended_cost='{ \
               self.extended_cost}')".format(self=self)


Base.metadata.create_all(engine)