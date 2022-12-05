#!/usr/bin/python3

"""
script that prints the State object with
the name passed as argument from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    """
    make engine
    """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(user, passwd, db), pool_pre_ping=True)
    # make a session
    Session = sessionmaker(bind=engine)
    # create an instance of the Session
    session = Session()

    # query the database to add new state
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()
    print('{}'.format(new_state.id))

    session.close()
