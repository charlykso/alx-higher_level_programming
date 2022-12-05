#!/usr/bin/python3

"""
script that lists all City
objects from the database hbtn_0e_101_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

user = argv[1]
passwd = argv[2]
db = argv[3]

if __name__ == '__main__':
    # connect to database
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(user, passwd, db), pool_pre_ping=True)
    # make session
    Session = sessionmaker(bind=engine)
    # create instance of session
    session = Session()

    # query the db
    for city in session.query(City).order_by(City.id):
        print('{}: {} -> {}'.format(city.id, city.name, city.state.name))

    session.close()
