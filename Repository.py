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
        c = self._conn.cursor()
        c.executescript("""
        CREATE TABLE vaccines(
                id integer primary key autoincrement,
                date TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                supplier INTEGER NOT NULL,
                FOREIGN KEY(supplier) REFERENCES suppliers(id));
        CREATE TABLE suppliers(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                logistic INTEGER NOT NULL,
                FOREIGN KEY(logistic)  REFERENCES logistics(id));    
        CREATE TABLE clinics(
                id INTEGER PRIMARY KEY,
                location TEXT NOT NULL,
                demand INTEGER NOT NULL,
                logistic INTEGER NOT NULL,
                FOREIGN KEY(logistic)  REFERENCES logistics(id));
        CREATE TABLE logistics(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                count_sent INTEGER NOT NULL,
                count_received INTEGER NOT NULL);""")


# the repository singleton
repo = Repository()
atexit.register(repo._close)