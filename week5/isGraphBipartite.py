class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = [0]*len(graph) # visited array equal in length to input graph

        for node in range(len(graph)):
            # if node not visited then place value in stack and assign it a value of
            # 1 to indicate its now been visited
            if not visited[node]:
                stack = [node]
                visited[node] = 1
            # while there are still nodes to visit, pop the element off the bottom of the stack
            while stack:
                node = stack.pop()
                # check to see if neighboring node values have same value, if they do,
                # neighboring nodes cannot share the same value(color) so the graph is not
                # bitpartite
                for neighbor in graph[node]:
                    if visited[neighbor] == visited[node]:
                        return False
                    # if neighbor has not been visited, place that in the stack (nodes to visit)
                    # assign it the opposite value of current node
                    if not visited[neighbor]:
                        stack.append(neighbor)
                        visited[neighbor] = visited[node]*-1
        return True
                    
