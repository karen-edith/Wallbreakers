import collections
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        # initialize jewelstone count and set for Jewels
        count, jewelSet = 0, set()

        for j in J:
            jewelSet.add(j) # put character in set

        for s in S:
            if (s in jewelSet):
                count = count + 1 #count all stone characters in jewel set
