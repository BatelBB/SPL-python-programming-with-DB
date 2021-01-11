import sys

import Repository
from singleObjects.Clinic import Clinic
from singleObjects.Vaccine import Vaccine
from singleObjects.Supplier import Supplier
from singleObjects.Logistic import Logistic

def add_information_to_tables(filePath, repo):
    with open(filePath, 'r') as file:

        splitFirstLine = file.readline(0).split(',')
        amountVaccines = splitFirstLine[0]
        amountSuppliers = splitFirstLine[1]
        amountClinics = splitFirstLine[2]
        amountLogistics = splitFirstLine[3]

        for index in range(1, amountVaccines+1):
            line = next(file)
            splitVaccines = line.split(',')
            vaccinesFromFile = Vaccine(splitVaccines[0], splitVaccines[1], splitVaccines[2], splitVaccines[3])
            repo.vaccines.insert(vaccinesFromFile)

        for index in range(amountVaccines+1, amountSuppliers + 1):
            line = next(file)
            splitSuppliers = line.split(',')
            supplierFromFile = Supplier(splitSuppliers[0], splitSuppliers[1], splitSuppliers[2])
            repo.supplier.insert(supplierFromFile)

        for index in range(amountSuppliers + 1, amountClinics + 1):
            line = next(file)
            splitClinic = line.split(',')
            clinicsFromFile = Clinic(splitClinic[0], splitClinic[1], splitClinic[2], splitClinic[3])
            repo.clinic.insert(clinicsFromFile)

        for index in range(amountClinics + 1, amountLogistics + 1):
            line = next(file)
            splitLogistics = line.split(',')
            logisticFromFile = Logistic(splitLogistics[0], splitLogistics[1], splitLogistics[2], splitLogistics[3])
            repo.logistic.insert(logisticFromFile)



def main(args):
    inputfilename = args[1]
    repo = Repository.repo
    repo.__init__()
    # add_activity_to_Activities(inputfilename, repo)
    # printdb(repo)


if __name__ == '__main__':
    main(sys.argv)
