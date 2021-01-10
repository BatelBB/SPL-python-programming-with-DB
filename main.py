import sys

import Repository

def main(args):
    inputfilename = args[1]
    repo = Repository.repo
    repo.__init__()
    #add_activity_to_Activities(inputfilename, repo)
    #printdb(repo)


if __name__ == '__main__':
    main(sys.argv)