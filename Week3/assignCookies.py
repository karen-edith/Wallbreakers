from collections import Counter
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        # sort g and s arrays
        sSorted, gSorted  = sorted(s), sorted(g)

        #initiate i, j, and count values at 0
        i, j, count = 0, 0, 0

        # check g against s one by one
        while i < len(g) and j < len(s):
                # for each sorted g value, check to see if, one by one, s values are
                # greater than or equal to sorted s values, if it move up one
                # in the g sorted array and up one in the s sorted array, and repeat
                # comparison
                if sSorted[j] >= gSorted[i]:
                    count = count + 1
                    j = j + 1
                    i = i + 1
                # otherwise, keep moving through sorted s array until you find a value
                # that meets the above criteria
                else:
                    j = j + 1
        return count
