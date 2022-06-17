from CSP import *


class CSPCryptarithmetic(CSP):

    def __init__ (self, variables, domains):
        # a list of variables
        # a dictionary of domains: a mapping of variables to a list of possible values
        super().__init__(variables,domains)


    def consistent(self, variable, val, assignment):
        for variable2 in self.constraints[variable]:
            if variable2 in assignment and assignment[variable2] == val:
                return False

        # check if all letters are assigned
        assign = copy.deepcopy(assignment)
        assign[variable] = val

        if len(assign) == len(self.variables):
            S = int(assign["S"])
            E = int(assign["E"])
            N = int(assign["N"])
            D = int(assign["D"])
            M = int(assign["M"])
            o = int(assign["O"])
            R = int(assign["R"])
            E = int(assign["E"])
            M = int(assign["M"])
            o = int(assign["O"])
            N = int(assign["N"])
            E = int(assign["E"])
            Y = int(assign["Y"])

            send = S * 1000 + E * 100 + N * 10 + D
            more =  M * 1000 + o * 100 + R * 10 + E
            money = M * 10000 + o * 1000 + N * 100+ E * 10 + Y

            return send + more == money
        return True
    print('done')