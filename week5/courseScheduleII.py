from collections import defaultdict
from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        indegree = defaultdict(int) # indegree of each vertex
        neighbor = defaultdict(set) # outgoing edges for each vertex

        for to, frm in prerequisites:
            neighbor[frm] |= {to}
            indegree[to] += 1

        #print('indegree', indegree)
        #print('oudgoing Edges', neighbor)

        visited = set() # vertices that have been visited
        visitedArr = [] # added array to keep order of how vertices are visited
        # double ended queue, vertices to be visited, if there are any
        # vertices with no incoming edges add them to queue
        toVisit = deque( i for i in range(numCourses) if not indegree[i])
        count = 0 # visited count

        #print('to visit', toVisit)

        # while there are still vertices to visit, pop off vertices from the front of the queue list
        while toVisit:
            cur = toVisit.popleft()

            # add popped vertex to visited array and add 1 to visited count
            visited.add(cur)
            visitedArr.append(cur)
            count += 1
            # if no cycle found and count equals number of courses then it is possible to finish
            # all courses
            #print('visited', visited)
            if count == numCourses:
                return(visitedArr)
                #return True

            # check neighboring vertices for current vertex, update indegree dictionary accordingly and
            # to visit array
            for v in neighbor[cur]:
                indegree[v] -= 1
                if not indegree[v]: toVisit += [v]
