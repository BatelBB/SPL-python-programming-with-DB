# Data Transfer Objects:
class Logistic:
    def __init__(self, logistic_id, name, count_received, count_sent):
        self.logistic_id = logistic_id
        self.name = name
        self.count_received = count_received
        self.count_sent = count_sent
