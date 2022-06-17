from CSP import *

class nqueesnscsp(CSP):

    def __init__(self, variables, domains):
        super().__init__(variables, domains)


    def consistent(self, variable, val, assignment):
        for variable2 in self.constraints[variable]:
            if variable2 in assignment:
                if assignment[variable2] == val:
                    return False
                else:
                    row_difference = abs(int(variable2) - int(variable))
                    col_difference = abs(int(val) - int(assignment[variable2]))
                    if row_difference == col_difference:
                        return False
        return True