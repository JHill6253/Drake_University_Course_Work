from nqueenscsp import *

number_q = 20

def main():
    variables = []
    domains = {}

    for i in range(1,number_q):
        variables.append(str(i))

    d = [str(x) for x in range(1,number_q)]
    for variable in variables:
        domains[variable] =d
    myCSP = nqueesnscsp(variables,domains)

    for i in range(1,number_q):
        for l in range(i+1, number_q):
            myCSP.addConstraint(str(i),str(l))

    myCSP.ac3()
    myCSP.print()
    myCSP.search()
    myCSP.print()
main()
