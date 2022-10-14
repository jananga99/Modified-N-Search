# Calculate the heuristic between input configuration and goal configuration using the input method
def calculateHeuristic(configuration1, configuration2, method, size):
    if method == "man":
        return manhattanDistance(configuration1, configuration2, size)
    elif method == "mis":
        return numMisplacedTiles(configuration1, configuration2, size)


# Returns the number of misplaced tiles between configuration1 and configuration2
def numMisplacedTiles(configuration1, configuration2, size):
    h = 0
    for i in range(size):
        for j in range(size):
            if configuration1[i][j] != "-" and configuration1[i][j] != configuration2[i][j]:
                h += 1
    return h


# Returns the manhattan distance corresponding val (in x,y indexes) in configuration.
def cellManhattanDistance(val, x, y, configuration, size):
    for i in range(size):
        for j in range(size):
            if val == configuration[i][j]:
                return abs(x - i) + abs(y - j)


# Returns manhattan distance between configuration1 and configuration2
def manhattanDistance(configuration1, configuration2, size):
    h = 0
    total = 0
    for i in range(size):
        for j in range(size):
            if configuration1[i][j] != "-":
                total += cellManhattanDistance(configuration1[i][j], i, j, configuration2, size)
    return total
