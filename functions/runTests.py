import random
import time

from functions.algorithm import n_search_set
from functions.fileHandling import writeConfiguration, appendFile, writeFile
from functions.generators import ConfigurationGenerator


def runTests(numTests, lowSize, highSize, startDirPath, goalDirPath, output):

    #writeFile(output, "Mis  Man")
    writeFile(output, "")

    for i in range(1, numTests + 1):

        size = random.randint(lowSize, highSize)

        start_configuration = ConfigurationGenerator(size)
        writeConfiguration(startDirPath+ str(i) + ".txt", start_configuration)
        goal_configuration = ConfigurationGenerator(size)
        writeConfiguration(goalDirPath + str(i) + ".txt", goal_configuration)
        startTime = time.time()
        ansMisplaced = n_search_set(start_configuration, goal_configuration, size, "mis").f
        print("Step " + str(i) + " Time Misplaced : ", time.time()-startTime )
        startTime = time.time()
        ansManhattan = n_search_set(start_configuration, goal_configuration, size, "man").f
        print("Step " + str(i) + " Time Manhattan : ", time.time() - startTime)
        print()
        appendFile(output , str(ansMisplaced) + "  " + str(ansManhattan) + "\n")