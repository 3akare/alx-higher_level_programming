#!/usr/bin/python3
"""changes the name of a State object from the database hbtn_0e_6_usa"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == '__main__':
    URL = 'mysql+mysqldb://{}:{}@localhost/{}'
    s1, s2, s3 = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(URL.format(s1, s2, s3), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    new_update = session.query(State).filter(State.id == 2)
    new_update.update({State.name: 'New Mexico'})
    session.commit()
