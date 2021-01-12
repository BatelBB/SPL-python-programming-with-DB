# Data Access Objects:
# All of these are meant to be singletons
class Vaccines:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, vaccine):
        self._conn.execute("INSERT INTO Vaccinces VALUES (?, ?, ?)", [vaccine.date,
                                                                      vaccine.supplier, vaccine.quantity])

    def update_amount_in_quantity(self, supplier, amount):
        self._conn.execute("UPDATE Vaccines SET quantity = quantity - " + amount + " WHERE supplier = " + supplier)

    def delete_row_from_vaccine_table(self, quantity):
        self._conn.execute("DELETE FROM vaccines WHERE quantity = " + quantity)

    def get_vaccine_quantity_by_clinic_location(self, location):
        c = self._conn.cursor()
        c.execute("""SELECT quantity
                    FROM vaccines, clinics
                    JOIN suppliers ON vaccines.supplier = suppliers.id AND suppliers.logistic = clinics.logistic
                    WHERE clinics.location = """ + location)
        return c.fetchone()
