# The Repository
import atexit
import os
import _sqlite3

#from pluralObjects.Activities import Activities
#from pluralObjects.Coffee_stands import Coffee_stands
#from pluralObjects.Employees import Employees
#from pluralObjects.Products import Products
#from pluralObjects.Suppliers import Suppliers


class Repository:
    def __init__(self):
        self._conn = _sqlite3.connect('database.db')
        #self.employees = Employees(self._conn)
        #self.coffee_stands = Coffee_stands(self._conn)
        #self.products = Products(self._conn)
        #self.suppliers = Suppliers(self._conn)
        #self.activities = Activities(self._conn)

    def _close(self):
        self._conn.commit()
        self._conn.close()

    def create_tables(self):
        self._conn.executescript("""
        CREATE TABLE vaccines(
                id INTEGER PRIMARY KEY,
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