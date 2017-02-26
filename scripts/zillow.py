from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float
import csv
import geocoder
import os

Base = declarative_base()

mysql_user = os.environ.get('MYSQL_USER')
mysql_password = os.environ.get('MYSQL_PASSWORD')
if not mysql_user:
    print 'No MYSQL_USER in env'
elif not mysql_password:
    print 'No MYSQL_PASSWORD in env'

conn_string = 'mysql://{user}:{password}@localhost:3306/ratemylandlord'.format(
    user=mysql_user,
    password=mysql_password
)

engine = create_engine(conn_string, echo=False)
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

Session = sessionmaker(bind=engine)
session = Session()

class Landlord(Base):
    __tablename__ = 'landlord'

    id = Column(primary_key = True)
    name = Column(String(100), primary_key=True, nullable=False)
    contact_name = Column(String(100))
    score = Column(Float, default=0)
    address = Column(String(100), nullable=False)
    phone_number = Column(String(20))
    email = Column(String(100))
    link = Column(String(100))
    latitude = Column(Float)
    longitude = Column(Float)

def geocode(row):
    api_key = os.environ.get('MAPQUEST_API_KEY')
    if not api_key:
        print 'MAPQUEST_API_KEY not set'
    else:
        address = "{} Boulder, Colorado".format(row[0])
        print address
        g = geocoder.mapquest(address, key=api_key)
        return (g.json['lat'], g.json['lng'])


with open('initial_data.csv') as csv_file:
    reader = csv.reader(csv_file)
    next(reader, None)
    for row in reader:

        # Landlord info
        name = row[1]
        contact_name = row[2]
        phone = row[3]
        email = row[4]
        address = row[0]


        coords = geocode(row)
        # construct a Model object
        landlord = Landlord(
            name=name,
            contact_name=contact_name,
            phone_number=phone,
            email=email,
            latitude=coords[0],
            longitude=coords[1],
            address=address
        )
        session.add(landlord)
    session.commit()
