import sys

import Repository

def add_information_to_tables(filePath, repo):
    with open(filePath) as file:
        for line in file:
            line = line.strip()
            splitted_line = line.split(', ')
            if splitted_line[0] == 'C':
                if splitted_line.__len__() == 3:
                    coffee_stand = Coffee_stand(splitted_line[1], splitted_line[2], None)
                    repo.coffee_stands.insert(coffee_stand)
                elif splitted_line.__len__() == 4:
                    coffee_stand = Coffee_stand(splitted_line[1], splitted_line[2], splitted_line[3])
                    repo.coffee_stands.insert(coffee_stand)
            elif splitted_line[0] == 'S':
                if splitted_line.__len__() == 3:
                    supplier = Supplier(splitted_line[1], splitted_line[2], None)
                    repo.suppliers.insert(supplier)
                elif splitted_line.__len__() == 4:
                    supplier = Supplier(splitted_line[1], splitted_line[2], splitted_line[3])
                    repo.suppliers.insert(supplier)
            elif splitted_line[0] == 'E':
                employee = Employee(splitted_line[1], splitted_line[2], splitted_line[3], splitted_line[4])
                repo.employees.insert(employee)
            elif splitted_line[0] == 'P':
                product = Product(splitted_line[1], splitted_line[2], splitted_line[3], 0)
                repo.products.insert(product)

def main(args):
    inputfilename = args[1]
    repo = Repository.repo
    repo.__init__()
    #add_activity_to_Activities(inputfilename, repo)
    #printdb(repo)


if __name__ == '__main__':
    main(sys.argv)