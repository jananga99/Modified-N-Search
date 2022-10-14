from copy import deepcopy


# Swap i,j and x,y indexed cells im configuration and return configuration
def swapCells(configuration, i, j, x, y):
    configuration[i][j], configuration[x][y] = configuration[x][y], configuration[i][j]
    return configuration


# Return the list of successors configuration of given configuration
def getSuccessors(configuration, size):
    successors = []
    emptyCount = 0
    for i in range(size):
        for j in range(size):

            if configuration[i][j] == "-":

                emptyCount += 1

                if j > 0 and configuration[i][j - 1] != "-":
                    successors.append((swapCells(deepcopy(configuration), i, j, i, j - 1), "("+configuration[i][j-1]+",right)"))

                if i > 0 and configuration[i - 1][j] != "-":
                    successors.append((swapCells(deepcopy(configuration), i, j, i - 1, j),"("+configuration[i-1][j]+",down)"))

                if j < size - 1 and configuration[i][j + 1] != "-":
                    successors.append((swapCells(deepcopy(configuration), i, j, i, j + 1),"("+configuration[i][j+1]+",left)"))

                if i < size - 1 and configuration[i + 1][j] != "-":
                    successors.append((swapCells(deepcopy(configuration), i, j, i + 1, j), "("+configuration[i+1][j]+",up)"))

            if emptyCount >= 2:
                return successors

    # If there are no empty cells, it is not a reachable successor, and it raises an exception
    raise Exception("Invalid Node, Does not contain two -")
