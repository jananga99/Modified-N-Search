from functions.heuristics import calculateHeuristic


# configuration = current configuration : str[size][size]
# goalConfiguration = goal configuration : str[size][size]
# parent = Predecessor node from which this node created : Node
# heuMethod = "mis" for misplaced tile, "man" for manhattan distance
# Cost from start state to this state : int
# size = Size(Length) of the configuration : int
# parentMethod = Operation used to get this node from parent node (only use if backtracking is needed) : str
class Node:

    def __init__(self, configuration, goalConfiguration, parent, heuMethod, g, size, parentMethod=''):
        self.configuration = configuration
        self.h = calculateHeuristic(configuration, goalConfiguration, heuMethod, size)
        self.g = None
        self.f = None
        self.setCostFromState(g)
        self.parent = parent
        self.parentMethod = parentMethod

    # set the cost from start state to this state
    def setCostFromState(self, g):
        self.g = g
        self.f = self.h + g

    # Less than
    def __lt__(self, other):
        return self.h < other.h

    # Less than or equal
    def __le__(self, other):
        return self.h <= other.h

    # Less than
    def __gt__(self, other):
        return self.h > other.h

    # Less than or equal
    def __ge__(self, other):
        return self.h >= other.h

# print the configuration 2d array
def printConfiguration(configuration):
    printStr = ""
    for i in configuration:
        for j in i:
            printStr += str(j) + " "
        printStr += "\n"
    print(printStr)


# Prints the information of the node
def printNode(node):
    printStr = "---------------------------------------\n"
    print("Current configuration")
    printConfiguration(node.configuration)
    printStr += "Heuristic value: " + str(node.h) + "\n"
    printStr += "Cost from start: "
    if node.g == -1:
        printStr += "Not calculated yet. \n"
    else:
        printStr += str(node.g) + "\n"
    printStr += "Estimated total cost to goal through this state: "
    if node.f == -1:
        printStr += "Not calculated yet. \n"
    else:
        printStr += str(node.f) + "\n"
    printStr += "---------------------------------------\n"
    return printStr
