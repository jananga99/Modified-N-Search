import random


def ConfigurationGenerator(n):
    numSeq = random.sample(range(1, n ** 2 - 1), n ** 2 - 2)
    emptyIndex = random.sample(range(n ** 2 - 2), 2)
    numSeq.insert(emptyIndex[0], "-")
    numSeq.insert(emptyIndex[1], "-")
    configuration = [[None for j in range(n)] for i in range(n)]
    c = 0
    for i in range(n):
        for j in range(n):
            configuration[i][j] = str(numSeq[c])
            c += 1
    return configuration
