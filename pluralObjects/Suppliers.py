# Data Access Objects:
# All of these are meant to be singletons
class Suppliers:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, supplier):
        self._conn.execute("INSERT INTO Suppliers VALUES (?, ?, ?)", [supplier.id, supplier.name, supplier.logistic])

    def get_logistic_from_supplier(self, name):
        c = self._conn.cursor()
        c.execute("""SELECT logistic
                    FROM suppliers
                    WHERE suppliers.name = """ + name)
        return c.fetchone()

    def get_supplier_id_from_supplier_name(self, name):
        c = self._conn.cursor()
        c.execute("""SELECT id
                            FROM suppliers
                            WHERE suppliers.name = """ + name)
        return c.fetchone()