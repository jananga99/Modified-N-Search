# get the number square as a 2d array from given input filename
from functions.algorithm import n_search_set

# start_file = input("Start configuration file : ")
# goal_file = input("Goal configuration file : ")
from functions.fileHandling import getConfigurationFromFile, writeFile, getPath
from functions.pairedT import pairedT
from functions.runTests import runTests


start_file = "Sample_Start_Configuration.txt"
goal_file = "Sample_Goal_Configuration.txt"
output_file = "output.txt"

start_configuration = getConfigurationFromFile(start_file)
goal_configuration = getConfigurationFromFile(goal_file)
size = len(start_configuration)
heuMethod = "mis"

ans = n_search_set(start_configuration, goal_configuration, size, heuMethod)


writeFile(output_file, getPath(ans))


"""
runTests(100,3,4, "tests/starts/", "tests/goals/", "tests/outputs.txt")
pairedT("tests/outputs.txt", "tests/analysis.txt")
"""