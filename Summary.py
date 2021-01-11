# Data Transfer Objects:
class Summary:
    def __init__(self, total_inventory, total_demand, total_received, total_sent):
        self.total_inventory = total_inventory
        self.total_demand = total_demand
        self.total_received = total_received
        self.total_sent = total_sent


