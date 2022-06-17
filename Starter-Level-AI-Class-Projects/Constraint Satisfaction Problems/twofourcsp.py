from Cryptarithmetic_P import *

def main():
    variables = ["S","E","N","D","M","O",'R','Y',]
    domains = {}

    d = [x for x in range(0,10)]

    for variable in variables:
        domains[variable] = d

    myCSP = CSPCryptarithmetic(variables,domains)

    for i in range(len(variables)):
        for j in range (i+1,len(variables)):
            myCSP.addConstraint(variables[i],variables[j])

    myCSP.ac3()
    myCSP.print()

    myCSP.search()
    myCSP.print()


main()