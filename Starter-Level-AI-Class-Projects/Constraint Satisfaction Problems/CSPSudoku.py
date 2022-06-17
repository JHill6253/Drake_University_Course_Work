from CSP import *

class CSPSudoku(CSP):

    def __init__ (self, variables, domains):
        # a list of variables
        # a dictionary of domains: a mapping of variables to a list of possible values
        super().__init__(variables,domains)



    def printBoard(self):
        for row in range(9):
            for col in range(9):
                val = "n"
                num = len(self.domains[self.variables[row * 9 + col]])
                if num == 1:
                    val = str(self.domains[self.variables[row * 9 + col]][0])
                elif num > 1:
                    val = "."
                print(val, end="")

                if (col == 2 or col == 5):
                    print ("|", end = "")
            print()

            if (row == 2 or row == 5):
                for col in range(11):
                    print("-", end="")
                print()
