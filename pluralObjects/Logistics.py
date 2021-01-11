# Data Access Objects:
# All of these are meant to be singletons
class Logistics:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, logistic):
        self._conn.execute("INSERT INTO Logistics VALUES (?, ?, ?, ?)",
                           [logistic.id, logistic.name, logistic.count_sent, logistic.count_received])

    def get_logistics_id_from_clinics(self, location):
        c = self._conn.cursor()
        c.execute("""SELECT logistic
                                FROM clinics
                                JOIN logistics ON clinics.logistic = logistics.id 
                                WHERE clinics.location = """ + location)
        return c.fetchone()

    def update_count_sent(self, amount, id):
        self._conn.execute("UPDATE Logistics SET count_sent = count_sent + " + amount + " WHERE id = " + id)

    def update_count_received(self, amount, id):
        self._conn.execute("UPDATE Logistics SET count_received = count_received + " + amount + " WHERE id = " + id)
