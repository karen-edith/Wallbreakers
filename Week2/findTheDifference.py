from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        # create string count dictionaries
        sCounter, tCounter = Counter(s), Counter(t)

        # check to see if items in tCounter are in sCounter
        for key, value in tCounter.items():
            # if not in sCounter, then its a new letter
            if key not in sCounter:
                return key
            # if in sCounter, check to see that corresponding sCounter values match
            # if not a new letter has been added
            elif sCounter[key] != tCounter[key]:
                return key
