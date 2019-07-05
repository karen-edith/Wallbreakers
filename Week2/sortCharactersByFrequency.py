from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        # setup a string counter map, and initialize string
        sCounter, string = Counter(s), ''

        # sort the counter by value and returns array of corresponding values
        sCounterSorted = sorted(sCounter, key = sCounter.get, reverse=True)

        # if character in string appears in sorted counter (in order of descending)
        # frequency, it gets attached to string variable 
        for i in sCounterSorted:
            for j in s:
                if i == j:
                    string = string + j
        return string
