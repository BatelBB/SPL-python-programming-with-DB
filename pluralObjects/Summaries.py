# Data Access Objects:
# All of these are meant to be singletons


class Summaries:
    def __init__(self, total_inventory, total_demand, total_received, total_sent):
        self._total_inventory = total_inventory
        self._total_demand = total_demand
        self._total_received = total_received
        self._total_sent = total_sent

    def totalSent(self, sent):
        self._total_sent = self._total_sent + sent
        self._total_demand = self._total_demand - sent
        self._total_inventory = self._total_inventory - sent
        self.createOutput(input)

    def totalReceived(self, received):
        self._total_received = self._total_received + received
        self._total_inventory = self._total_inventory + received
        self.createOutput()

    def createOutput(self, input):
        with open(input, "w") as file:
            text = self._total_inventory + "," + self._total_demand + "," + self._total_received + "," + self._total_sent
            file.writelines(text)


def main(args):
    Summaries.__init__()
