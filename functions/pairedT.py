import math
import statistics
from scipy import stats


# Analysing using paired t test on sample of differences.
def pairedT(dataFileName, analysisFileName):
    print("Analysing")
    dataFile = open(dataFileName, "r")
    analysisFile = open(analysisFileName, "w")

    misplacedArr = []
    manhattanArr = []
    diffArr = []

    for line in dataFile:
        a, b = tuple(map(int, line.split()))
        misplacedArr.append(a)
        manhattanArr.append(b)
        diffArr.append(a - b)  # misplaced-manhattan
    analysisFile.write("Array of number of moves required for misplaced tiles heuristic\n")
    analysisFile.write(str(misplacedArr) + "\n")
    analysisFile.write("Array of number of moves required for manhattan distance heuristic\n")
    analysisFile.write(str(manhattanArr) + "\n")
    analysisFile.write("Sample of differences (Misplaced - Manhattan\n")
    analysisFile.write(str(diffArr) + "\n")

    diffMean = statistics.mean(diffArr)
    analysisFile.write("Sample Mean : " + str(diffMean) + "\n")
    sampleDeviation = statistics.stdev(diffArr)
    analysisFile.write("Sample Derivation : " + str(sampleDeviation) + "\n")
    t = diffMean / (sampleDeviation / math.sqrt(len(misplacedArr)))
    analysisFile.write("t statistic : " + str(t) + "\n")
    p = stats.t.pdf(t, len(misplacedArr) - 1)
    analysisFile.write("p value : " + str(p) + "\n")
    # if p<0.05 null hypothesis correct probability is low
    dataFile.close()
    analysisFile.close()
    print("Analysis finished")

# pairedT("../outputs.txt","../analysis.txt")
