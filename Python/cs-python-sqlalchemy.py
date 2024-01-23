#based on Copeland, Rick_Myers, Jason - Essential SQLAlchemy_ mapping Python to databases-O'Reilly Media (2016)


#tablas que almacenan metadata
from sqlalchemy import MetaData
metadata = MetaData()

#Inicializar tablas y columnas
from sqlalchemy import Table, Column, Integer, Numeric, String, ForeignKey
cookies = Table('cookies', metadata,
        Column('cookie_id', Integer(), primary_key=True),
        Column('cookie_name', String(50), index=True),
        Column('cookie_recipe_url', String(255)),
        Column('cookie_sku', String(55)),
        Column('quantity', Integer()),
        Column('unit_cost', Numeric(12, 2))
)

from datetime import datetime
from sqlalchemy import DateTime
users = Table('users', metadata,
    Column('user_id', Integer(), primary_key=True),
    Column('username', String(15), nullable=False, unique=True),
    Column('email_address', String(255), nullable=False),
    Column('phone', String(20), nullable=False),
    Column('password', String(25), nullable=False),
    Column('created_on', DateTime(), default=datetime.now),
    Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)
)


#Keys and constraints
from sqlalchemy import PrimaryKeyConstraint, UniqueConstraint, CheckConstraint
PrimaryKeyConstraint('user_id', name='user_pk')

UniqueConstraint('username', name='uix_username')

CheckConstraint('unit_cost >= 0.00', name='unit_cost_positive')

ForeignKeyConstraint(['order_id'], ['orders.order_id'])

#Indexes
from sqlalchemy import Index
Index('ix_cookies_cookie_name', 'cookie_name')


#Relationships
from sqlalchemy import ForeignKey
orders = Table('orders', metadata,
    Column('order_id', Integer(), primary_key=True),
    Column('user_id', ForeignKey('users.user_id')),     #relacion con la tabla users
    Column('shipped', Boolean(), default=False)
)

line_items = Table('line_items', metadata,
    Column('line_items_id', Integer(), primary_key=True),
    Column('order_id', ForeignKey('orders.order_id')),   #relacion con la tabla orders
    Column('cookie_id', ForeignKey('cookies.cookie_id')), #relacion con la tabla cookies
    Column('quantity', Integer()),
    Column('extended_cost', Numeric(12, 2))
)


#persisting
metadata.create_all(engine)


#SQL Achemy Core------------------------------------------------------------------------------------------
#Insert
ins = cookies.insert().values(
cookie_name="chocolate chip",
cookie_recipe_url="http://some.aweso.me/cookie/recipe.html",
cookie_sku="CC01",
quantity="12",
unit_cost="0.50"
)

print(str(ins)) # muestra el string con el sql


ins.compile().params #parameters that effectively are going to be sent

result = connection.execute(ins) #executing the insert statement

result.inserted_primary_key # id of the inserted data

#querying data
from sqlalchemy.sql import select
s = select([cookies])
rp = connection.execute(s) #ResultProxy, an iterable
results = rp.fetchall() #contains a list with the rows

first_row = results[0] # firs row of data
first_row[1] #access column by index
first_row.cookie_name #access column by name
first_row[cookies.c.cookie_name] #access column by column object


#iterating over a return proxy
for record in rp:
    print(record.cookie_name)   


s = select([cookies.c.cookie_name, cookies.c.quantity]) #select specific columns
s = s.order_by(cookies.c.quantity) # order asc
s = s.order_by(desc(cookies.c.quantity)) #ordes desc, desc must be imported
s = s.limit(2) #limit the number of rows
s = select([func.sum(cookies.c.quantity)]) # summing , func must be imported
s = select([cookies]).where(cookies.c.cookie_name == 'chocolate chip') #filtering
s = select([cookies]).where(cookies.c.cookie_name.like('%chocolate%')) #filtering regular expr

# Clause Elements when filtering---------------------
# between(cleft, cright) Find where the column is between cleft and cright
# concat(column_two) Concatenate column with column_two
# distinct() Find only unique values for the column
# in_([list]) Find where the column is in the list
# is_(None) Find where the column is None (commonly used for Null checks with None)
# contains(string) Find where the column has string in it (case-sensitive)
# endswith(string) Find where the column ends with string (case-sensitive)
# like(string) Find where the column is like string (case-sensitive)
# startswith(string) Find where the column begins with string (case-sensitive)
# ilike(string) Find where the column is like string (this is not case-sensitive)


s = select([cookies.c.cookie_name, 'SKU-' + cookies.c.cookie_sku]) #operation on columns
s = select([cookies.c.cookie_name,
    cast((cookies.c.quantity * cookies.c.unit_cost), #operation on columns
        Numeric(12,2)).label('inv_cost')])

#using and
from sqlalchemy import and_, or_, not_
s = select([cookies]).where(
    and_(
        cookies.c.quantity > 23,
        cookies.c.unit_cost < 0.40
    )
)

#updating data
from sqlalchemy import update
u = update(cookies).where(cookies.c.cookie_name == "chocolate chip")
u = u.values(quantity=(cookies.c.quantity + 120))
result = connection.execute(u)
print(result.rowcount) #how many rows where updated
s = select([cookies]).where(cookies.c.cookie_name == "chocolate chip")
result = connection.execute(s).first()

#deleting data
u = delete(cookies).where(cookies.c.cookie_name == "dark chocolate chip")

#joins, outerjoin

columns = [orders.c.order_id, users.c.username, users.c.phone,
        cookies.c.cookie_name, line_items.c.quantity,
        line_items.c.extended_cost]
cookiemon_orders = select(columns)
cookiemon_orders = cookiemon_orders.select_from(orders.join(users).join(
                line_items).join(cookies)).where(users.c.username ==
                    'cookiemon')
result = connection.execute(cookiemon_orders).fetchall()

#Aliases , when a table must be queried more than once
manager = employee_table.alias('mgr')

#group by
columns = [users.c.username, func.count(orders.c.order_id)]
all_orders = select(columns)
all_orders = all_orders.select_from(users.outerjoin(orders))
all_orders = all_orders.group_by(users.c.username)
result = connection.execute(all_orders).fetchall()


#raw queries
result = connection.execute("select * from orders").fetchall()



#SQL Alchemy ORM----------------------------------------------------

#persisting the schema

from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:')
Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine) #at the end of the code


from sqlalchemy import Table, Column, Integer, Numeric, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Cookie(Base):
    __tablename__ = 'cookies'
    cookie_id = Column(Integer(), primary_key=True)
    cookie_name = Column(String(50), index=True)
    cookie_recipe_url = Column(String(255))
    cookie_sku = Column(String(55))
    quantity = Column(Integer())
    unit_cost = Column(Numeric(12, 2))

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer(), primary_key=True)
    username = Column(String(15), nullable=False, unique=True)
    email_address = Column(String(255), nullable=False)
    phone = Column(String(20), nullable=False)
    password = Column(String(25), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

#relationships
from sqlalchemy import ForeignKey, Boolean
from sqlalchemy.orm import relationship, backref

class Order(Base):
    __tablename__ = 'orders'
    order_id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey('users.user_id')) #foreign key from other table
    shipped = Column(Boolean(), default=False)
    user = relationship("User", backref=backref('orders', order_by=order_id)) #relationship 1 to many
    cookie = relationship("Cookie", uselist=False) #one to one relationship


#inserting a single object
cc_cookie = Cookie(cookie_name='chocolate chip',
                    cookie_recipe_url='http://some.aweso.me/cookie/recipe.html',
                    cookie_sku='CC01',
                    quantity=12,
                    unit_cost=0.50)
session.add(cc_cookie)
session.commit()

print(cc_cookie.cookie_id) # see the primary key

#inserting multiple records method 1
c1=Cookie(...)
c2=Cookie(...)
session.flush() #like a commit but doesnt end the transaction and dosnt commit

#inserting multiple records method 2
session.bulk_save_objects([c1,c2])
session.commit()

#querying data
cookies = session.query(Cookie).all()
print(cookies)

#using the session as an iterable
for cookie in session.query(Cookie):
    print(cookie)


print(session.query(Cookie.cookie_name, Cookie.quantity).first()) #querying by columns

#ordering
for cookie in session.query(Cookie).order_by(Cookie.quantity): #.order_by(desc(Cookie.quantity)) must import desc
    print('{:3} - {}'.format(cookie.quantity, cookie.cookie_name))

#limiting
query = session.query(Cookie).order_by(Cookie.quantity)[:2]

#summing
from sqlalchemy import func
inv_count = session.query(func.sum(Cookie.quantity)).scalar()
print(inv_count)


#filtering
record = session.query(Cookie).filter(Cookie.cookie_name == 'chocolate chip').first()
print(record)

query = session.query(Cookie).filter(Cookie.cookie_name.like('%chocolate%')) #regular expression

#operations
results = session.query(Cookie.cookie_name, 'SKU-' + Cookie.cookie_sku).all()

#conjunctions
query = session.query(Cookie).filter(
    Cookie.quantity > 23,
    Cookie.unit_cost < 0.40
)

# using and or not
from sqlalchemy import and_, or_, not_
query = session.query(Cookie).filter(
    or_(
    Cookie.quantity.between(10, 50),
    Cookie.cookie_name.contains('chip')
    )
)

#updating 

query = session.query(Cookie)
cc_cookie = query.filter(Cookie.cookie_name == "chocolate chip").first()
cc_cookie.quantity = cc_cookie.quantity + 120
session.commit()

#deleting
query = session.query(Cookie)
query = query.filter(Cookie.cookie_name == "dark chocolate chip")
dcc_cookie = query.one()
session.delete(dcc_cookie)
session.commit()
dcc_cookie = query.first()
print(dcc_cookie)
























