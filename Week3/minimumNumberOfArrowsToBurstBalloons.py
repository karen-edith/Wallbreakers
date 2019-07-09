class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        # if array is empty no ballons exist so 0 arrows are needed
        if len(points) == 0:
            return 0

        # sort array by ending positions
        points=sorted(points,key=lambda x:x[1])
        # first end point that will be used to compare start points
        end = points[0][1]
        i, count = 1, 1

        while i < len(points):
            # if the start point of the second ballon is greater than the endpoint
            # of the first ballon then there is no overlap and another arrow is needed
            # to pop the second, otherwise this section will repeat until it is met
            # if not met only 1 arrow will be used
            if points[i][0] > end:
                # new endpoint
                end = points[i][1]
                count = count + 1
            i = i + 1
        return count
