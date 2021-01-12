import sys

import Repository
from pluralObjects.Summaries import Summaries


def executeOrders(filePath, repo):
    with open(filePath, 'r') as file:
        for line in file:
            split_line = line.split(', ')
            if len(split_line) == 2:  ### Send shipment
                repo.Clinics.remove_amount_from_demand(split_line[0], int(split_line[1]))

                locationLogi = repo.Logistics.get_logistics_id_from_clinics(split_line[0])
                repo.Logistics.update_count_sent(int(split_line[1]), locationLogi)

                vaccinesQuantity = repo.Vaccines.get_vaccine_quantity_by_clinic_location(split_line[0])
                if vaccinesQuantity > int(split_line[1]):
                    repo.Vaccines.update_amount_in_quantity(int(split_line[1]))
                elif vaccinesQuantity == int(split_line[1]):
                    repo.Vaccines.delete_row_from_vaccine_table(int(split_line[1]))
                else:  #### TODO add the logic for the sum
                    sum = sum + (int(split_line[1]) - vaccinesQuantity)
                    repo.Vaccines.delete_row_from_vaccine_table(vaccinesQuantity)
                Summaries.totalSent(int(split_line[1]))
            elif len(split_line) == 3:  ### Receive shipment
                logisticID = repo.Suppliers.get_logistic_from_supplier(split_line[0])
                repo.Logistics.update_count_received(split_line[1], logisticID)

                supplierID = repo.Suppliers.get_supplier_id_from_supplier_name(split_line[0])
                repo.vaccines.insert(supplierID, split_line[1], split_line[2])
                Summaries.totalReceived(int(split_line[1]))


def main(args):
    # inputfilename = args[2]
    repo = Repository.repo
    repo.__init__()
    # (inputfilename, repo)


if __name__ == '__main__':
    main(sys.argv)
