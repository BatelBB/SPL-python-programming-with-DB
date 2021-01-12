import sys
import Repository
from Orders import executeOrders

from pluralObjects.Summaries import Summaries
from pluralObjects.Suppliers import Suppliers
from singleObjects.Clinic import Clinic
from singleObjects.Vaccine import Vaccine
from singleObjects.Supplier import Supplier
from singleObjects.Logistic import Logistic


def add_information_to_tables(filePath, repo, sumVaccineAmount, sumClinicsDemand):
    with open(filePath, 'r', encoding='utf-8') as file:
        #splitFirstLine = file.readline(0).replace(' ', '')
        #splitFirstLine = file.readline(0).split(',')
        #test = list(map(int, splitFirstLine))

        for index in range(0, 1):
            line = next(file)
            splitFirstLine = line.split(',')
            amountVaccines = int(splitFirstLine[0])
            amountSuppliers = int(splitFirstLine[1])
            amountClinics = int(splitFirstLine[2])
            amountLogistics = int(splitFirstLine[3])

        for index in range(1, amountVaccines + 1):
            line = next(file)
            splitVaccines = line.split(',')
            vaccinesFromFile = Vaccine(splitVaccines[1], int(splitVaccines[2]), splitVaccines[3])
            sumVaccineAmount = sumVaccineAmount + int(splitVaccines[2])
            repo.Vaccines.insert(vaccinesFromFile)

        for index in range(amountVaccines + 1, amountSuppliers + 1):
            line = next(file)
            splitSuppliers = line.split(',')
            supplierFromFile = Supplier(splitSuppliers[0], splitSuppliers[1], splitSuppliers[2])
            repo.Suppliers.insert(supplierFromFile)

        for index in range(amountSuppliers + 1, amountClinics + 1):
            line = next(file)
            splitClinic = line.split(',')
            clinicsFromFile = Clinic(splitClinic[0], splitClinic[1], int(splitClinic[2]), splitClinic[3])
            sumClinicsDemand = sumClinicsDemand + int(splitClinic[2])
            repo.Clinics.insert(clinicsFromFile)

        for index in range(amountClinics + 1, amountLogistics + 1):
            line = next(file)
            splitLogistics = line.split(',')
            logisticFromFile = Logistic(splitLogistics[0], splitLogistics[1], splitLogistics[2], splitLogistics[3])
            repo.Logistics.insert(logisticFromFile)
        Summaries.__init__(sumVaccineAmount, sumClinicsDemand, 0, 0)


def main(args):
    configFile = args[1]
    orderFile = args[2]
    outputFile = args[3]
    repo = Repository.repo
    repo.__init__()
    repo.create_tables()
    add_information_to_tables(configFile, repo, 0, 0)
    executeOrders(orderFile, repo)
    Summaries.createOutput(outputFile)


if __name__ == '__main__':
    main(sys.argv)
