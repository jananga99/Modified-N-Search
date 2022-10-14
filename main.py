# get the number square as a 2d array from given input filename
from functions.algorithm import n_search_set

# start_file = input("Start configuration file : ")
# goal_file = input("Goal configuration file : ")
from functions.fileHandling import getConfigurationFromFile, writeFile, getPath
from functions.pairedT import pairedT
from functions.runTests import runTests

while 1:
    start_file = input("Start configuration filename    :   ")
    try:
        start_configuration = getConfigurationFromFile(start_file)
        break
    except FileNotFoundError:
        print("Enter existing file name")

while 1:
    goal_file = input("Goal configuration filename     :   ")
    try:
        goal_configuration = getConfigurationFromFile(goal_file)
        break
    except FileNotFoundError:
        print("Enter existing file name")


output_file = "output.txt"

size = len(start_configuration)
heuMethod = "mis"

ans = n_search_set(start_configuration, goal_configuration, size, heuMethod)


writeFile(output_file, getPath(ans))


"""
runTests(100, 3, 4, "tests/starts/", "tests/goals/", "tests/outputs.txt")
pairedT("tests/outputs.txt", "tests/analysis.txt")
"""