import heapq

from functions.Node import Node
from functions.successors import getSuccessors


# Modified version of basic algorithm using sets.
# Two pair of sets used for OPEN, and CLOSED to optimize check element in operations
def n_search_set(start, goal, size, heuMethod):
    OPEN = [Node(start, goal, None, heuMethod, 0, size)]
    openSet = {str(start)}
    CLOSED = []
    closeSet = set()
    itr = 0
    while True:
        if len(OPEN) == 0:
            return False
        n = heapq.heappop(OPEN)
        openSet.remove(str(n.configuration))
        CLOSED.append(n)
        closeSet.add(str(n.configuration))
        if n.configuration == goal:
            return n
        for tup in getSuccessors(n.configuration, size):
            m = Node(tup[0], goal, n, heuMethod, n.g + 1, size, tup[1])
            prevmf = m.f
            conf = str(tup[0])
            inOpen = conf in openSet
            inClosed = False
            # conf can be in inClosed only if it is not in inOpen
            if not inOpen:
                inClosed = conf in closeSet
            if not inOpen and not inClosed:
                heapq.heappush(OPEN, m)
                openSet.add(conf)
            m.setCostFromState(min(m.g, n.g + 1))
            if prevmf > m.f and inClosed:
                CLOSED.remove(m)
                closeSet.remove(conf)
                heapq.heappush(OPEN, m)
                openSet.add(conf)
        itr += 1