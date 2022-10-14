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
    numTests = 0

    for line in dataFile:
        a, b = tuple(map(int, line.split()))
        misplacedArr.append(a)
        manhattanArr.append(b)
        diffArr.append(a - b)  # misplaced-manhattan
        numTests += 1
    analysisFile.write("Array of number of moves required for misplaced tiles heuristic\n")
    analysisFile.write(str(misplacedArr) + "\n")
    analysisFile.write("Array of number of moves required for manhattan distance heuristic\n")
    analysisFile.write(str(manhattanArr) + "\n")
    analysisFile.write("Sample of differences (Misplaced - Manhattan\n")
    analysisFile.write(str(diffArr) + "\n")

    diffMean = statistics.mean(diffArr)
    analysisFile.write("\nSample Mean : " + str(diffMean) + "\n")
    sampleDeviation = statistics.stdev(diffArr)
    analysisFile.write("Sample Derivation : " + str(sampleDeviation) + "\n")
    t = diffMean / (sampleDeviation / math.sqrt(len(misplacedArr)))

    # Test to check difference mean is greater than 0
    analysisFile.write("\nOne tailed t test(right) to check that difference mean > 0\n")
    analysisFile.write("H0 : Difference mean = 0.\n")
    analysisFile.write("H1 : Difference mean  > 0.\n")
    analysisFile.write("Assuming H0 is true,t statistic : " + str(t) + "\n")
    # p = stats.t.pdf(t, len(misplacedArr) - 1)
    # analysisFile.write("p value : " + str(p) + "\n")
    # if p<0.05 null hypothesis correct probability is low
    analysisFile.write("Suppose the level of significance is 5%, Degrees of freedom=99\n")
    criticalBoundary = stats.t.ppf(1 - 0.05 / 2, numTests - 1)
    analysisFile.write(
        "Therefore, for right tailed t test, Critical value for the boundary of critical region : %f\n" % criticalBoundary)
    analysisFile.write("If t statistic > %f, there is enough evidence to reject H0\n" % criticalBoundary)
    if t > criticalBoundary:
        analysisFile.write(
            "There is enough evidence to reject H0. Therefore the difference mean > 0.\nSo, misplaced tiles "
            "heuristics need more number of steps than manhattan distance heuristics. Therefore the manhattan distance "
            "heuristic is better.\n")
    else:
        analysisFile.write(
            "There is not enough evidence to reject H0. Therefore there is not enough evidence to state difference "
            "mean > 0. SO, there is not enough evidence to state manhattan distance heuristic is better than "
            "misplaced tiles heuristic.\n")

        # Test to check difference mean is less than 0
    analysisFile.write("\nOne tailed t test(left) to check that difference mean > 0\n")
    analysisFile.write("H0 : Difference mean = 0.\n")
    analysisFile.write("H1 : Difference mean  < 0.\n")
    analysisFile.write("Assuming H0 is true,t statistic : " + str(t) + "\n")
    # p = stats.t.pdf(t, len(misplacedArr) - 1)
    # analysisFile.write("p value : " + str(p) + "\n")
    # if p<0.05 null hypothesis correct probability is low
    analysisFile.write("Suppose the level of significance is 5%, Degrees of freedom=99\n")
    # criticalBoundary = -1.665  # From tables
    criticalBoundary = -stats.t.ppf(1 - 0.05 / 2, numTests - 1)
    analysisFile.write(
        "Therefore, for right tailed t test, Critical value for the boundary of critical region : %f\n" % criticalBoundary)
    analysisFile.write("If t statistic > %f, there is enough evidence to reject H0\n" % criticalBoundary)
    if t < criticalBoundary:
        analysisFile.write(
            "There is enough evidence to reject H0. Therefore the difference mean < 0.\nSo, misplaced tiles "
            "heuristics need less number of steps than manhattan distance heuristics. Therefore the misplaced tiles "
            "heuristic is better.\n")
    else:
        analysisFile.write(
            "There is not enough evidence to reject H0. Therefore there is not enough evidence to state difference "
            "mean < 0. SO, there is not enough evidence to state misplaced tiles heuristic is better than the "
            "manhattan distance heuristic.\n")

    dataFile.close()
    analysisFile.close()
    print("Analysis finished")

# pairedT("../outputs.txt","../analysis.txt")
