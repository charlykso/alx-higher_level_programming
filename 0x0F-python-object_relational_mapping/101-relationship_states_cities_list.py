#!/usr/bin/python3

"""
script that lists all State objects,
and corresponding City objects, contained
in the database hbtn_0e_101_usa
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
    #create instance of session
    session = Session()

    # query the db
    states = session.query(State).order_by(State.id)
    for state in states:
        print('{}: {}'.format(state.id, state.name))
        for city in state.cities:
            print('\t{}: {}'.format(city.id, city.name))

    session.close()
