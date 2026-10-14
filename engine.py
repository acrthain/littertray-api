from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from cat import Cat

DATABASE_URL = "postgresql+psycopg2://alexandrathain@localhost:5432/postgres"

class Engine():
    def __init__(self):
        self.engine = create_engine(DATABASE_URL)
        self.session = Session(self.engine)

    def print_cats(self):
        stmt = select(Cat)
        cats = []
        for cat in self.session.scalars(stmt):
            cats.append(cat)
        return cats
