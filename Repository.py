# The Repository
import atexit
import os
import _sqlite3

from pluralObjects.Clinics import Clinics
from pluralObjects.Logistics import Logistics
from pluralObjects.Suppliers import Suppliers
from pluralObjects.Vaccines import Vaccines


class Repository:
    def __init__(self):
        self._conn = _sqlite3.connect('database.db')
        self.clinics = Clinics(self._conn)
        self.logistics = Logistics(self._conn)
        self.suppliers = Suppliers(self._conn)
        self.vaccines = Vaccines(self._conn)

    def _close(self):
        self._conn.commit()
        self._conn.close()

    def create_tables(self):
        self._conn.executescript("""
        CREATE TABLE vaccines(
                id integer primary key autoincrement
                date DATE NOT NULL,
                supplier INTEGER REFERENCES Supplier(id),
                quantity INTEGER NOT NULL);
        CREATE TABLE suppliers(
                id INTEGER PRIMARY KEY,
                name STRING NOT NULL,
                logistic INTEGER REFERENCES Logistic(id));    
        CREATE TABLE clinics(
                id INTEGER PRIMARY KEY,
                location STRING NOT NULL,
                demand INTEGER NOT NULL,
                logistic INTEGER REFERENCES Logistic(id));
        CREATE TABLE logistics(
                id INTEGER PRIMARY KEY,
                name STRING NOT NULL,
                count sent INTEGER NOT NULL,
                count received INTEGER NOT NULL );
    """)


# the repository singleton
repo = Repository()
atexit.register(repo._close)