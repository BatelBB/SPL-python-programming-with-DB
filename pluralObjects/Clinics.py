# Data Access Objects:
# All of these are meant to be singletons
class Clinics:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, clinic):
        self._conn.execute("INSERT INTO Clinics VALUES (?, ?, ?, ?))", [clinic.id, clinic.location,
                                                                        clinic.demand, clinic.logistic])

    def remove_amount_from_demand(self, clinic, amount):
        self._conn.execute("UPDATE Clinics SET demand = demand - " + amount + " WHERE location = " + clinic)

