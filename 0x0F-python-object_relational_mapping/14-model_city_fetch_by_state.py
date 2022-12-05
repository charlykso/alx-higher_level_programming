#!/usr/bin/python3

"""
print all City objects from the
database hbtn_0e_14_usa
"""

from sys import argv
from model_city import City
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    """
    make engine
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(user, passwd, db), pool_pre_ping=True)
    # make Session
    Session = sessionmaker(bind=engine)

    # make an instance of the session
    session = Session()

    query_row = session.query(City, State)\
        .filter(City.state_id == State.id).all()

    for city, state in query_row:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
