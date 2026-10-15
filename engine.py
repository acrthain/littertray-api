from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from cat import Cat, Base
from tray_visit import TrayVisit
import os

DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    "postgresql+psycopg2://postgres:password@localhost:5432/postgres",
)


class Engine():
    def __init__(self):
        self.engine = create_engine(DATABASE_URL)
        Base.metadata.create_all(self.engine)
        self.session = Session(self.engine)

    def print_cats(self):
        stmt = select(Cat)
        cats = []
        for cat in self.session.scalars(stmt):
            cats.append(cat)
        return cats

    def print_tray_visits(self):  # fetches all tray visits from the database
        stmt = select(TrayVisit)  # build a query to select all tray visits
        tray_visits = []  # empty list to store the results
        for tray_visit in self.session.scalars(stmt):  # loop through each visit returned
            tray_visits.append(tray_visit)  # add it to the list
        return tray_visits  # send the list back to the endpoint

    def add_cat(self, name: str, age: int):  # takes a name and age, saves a new cat to the database
        cat = Cat(name=name, age=age)  # create a new cat object in memory
        self.session.add(cat)  # queue it up to be saved
        self.session.commit()  # actually write it to the database
        self.session.refresh(cat)  # re-read the row so we get the id the database assigned
        return cat  # send the cat back to the endpoint

    def add_tray_visit(self, visit_type: str, cat_weight: float,
                       cat_id: int):  # takes visit details, saves a new tray visit to the database
        tray_visit = TrayVisit(visit_type=visit_type, cat_weight=cat_weight,
                               cat_id=cat_id)  # create a new visit object in memory
        self.session.add(tray_visit)  # queue it up to be saved
        self.session.commit()  # actually write it to the database
        self.session.refresh(tray_visit)  # re-read the row so we get the id the database assigned
        return tray_visit  # send the visit back to the endpoint

    def delete_cat(self, cat_id: int):  # takes a cat id and removes that cat from the database
        cat = self.session.get(Cat, cat_id)  # find the cat with that id
        if cat is None:  # if no cat was found with that id
            return False  # signal that nothing was deleted
        self.session.delete(cat)  # queue it up to be deleted
        self.session.commit()  # actually delete it from the database
        return True  # signal that the deletion was successful

    def delete_tray_visit(self, tray_visit_id: int):  # takes a visit id and removes that visit from the database
        tray_visit = self.session.get(TrayVisit, tray_visit_id)  # find the visit with that id
        if tray_visit is None:  # if no visit was found with that id
            return False  # signal that nothing was deleted
        self.session.delete(tray_visit)  # queue it up to be deleted
        self.session.commit()  # actually delete it from the database
        return True  # signal that the deletion was successful
