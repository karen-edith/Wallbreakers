from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # set up letterIndexMap to have default lists as values, initialize j to -1
        letterIndexMap, j = defaultdict(list), -1

        # if s is empty there is no first non repeating letter
        if len(s) == 0:
            return -1

        # for each letter, map corresponding index by appending letters value array
        # while simultaneously preserving the order of letters
        for i in range(len(s)):
            letterIndexMap[s[i]].append(i)

        # first letter that has a an array value of lenght one will be first repeating letters
        for key, value in letterIndexMap.items():
            j = j + 1
            if len(value) == 1:
                return value[0]
            # if we get to the end of items in array and no letter has value array with length 1
            # all letters in string repeat themselves
            elif (j == len(letterIndexMap) - 1 ):
                return -1
