#!/usr/bin/python3
"""
Script that adds the State object “Louisiana” to the database
Using module SQLAlchemy
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()
    Base.metadata.create_all(engine)

    new_state = State(name="Louisiana")
    session.add(new_state)
    # commit and close session
    session.commit()
    print(new_state.id)
    session.close()
