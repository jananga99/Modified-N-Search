
# Get configuration as a 2d array of strings from the file
def getConfigurationFromFile(fileName):
    file = open(fileName, "r")
    numberSquare = []
    for line in file:
        numberSquare.append(line.split())
    file.close()
    return numberSquare


# prints the path to given file
def getPath(current):
    if current.parent is not None:
        if current.parent.parent is not None:
            return getPath(current.parent) + ", " + current.parentMethod
        else:
            return current.parentMethod


# writes given string the file
def writeFile(fileName, string):
    file = open(fileName, "w")
    file.write(string)
    file.close()


# Writes configuration (2d array) to file
def writeConfiguration(filename, configuration):
    out = ""
    for row in configuration:
        for cell in row:
            out += str(cell) + " "
        out += "\n"
    writeFile(filename, out)


# appends given string to the file
def appendFile(fileName, string):
    file = open(fileName, "a")
    file.write(string)
    file.close()


