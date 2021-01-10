# Data Transfer Objects:
class Vaccine:
    def __init__(self, vaccine_bulk_id, date, amount):
        self.vaccine_bulk_id = vaccine_bulk_id
        self.date = date
        self.amount = amount
