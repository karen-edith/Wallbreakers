from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # set up empty array to put in indeces, find length of p and s strings
        # and initiate index value
        indeces, sLength, pLength, index = [], len(s), len(p), 0
        # s is a shorter string them return empty array
        if sLength < pLength:
            return indeces
        # count number of letters in string p
        pCounter = Counter(p)
        # count number of letters in string s (based on length of p, first letters)
        sCounter = Counter(s[:pLength-1])

        # loop through remaining letters, adjust sCounter, and compare adjusted
        # sCounter to pCounter
        for index in range (pLength - 1, sLength):
            # count next letter, update if already in sCounter, if not letter
            # will be counted
            sCounter[s[index]] = sCounter[s[index]] + 1
            # compare adjusted sCounter to pCounter, if equal add index to indeces array
            if sCounter == pCounter:
                indeces.append(index - (pLength - 1))
            # go back to first letter of grouped letter, and remove 1 count from it
            sCounter[s[index - (pLength - 1)]] = sCounter[s[index - (pLength - 1)]] - 1
            # if count is now zero for that first group letter, delete it
            if sCounter[s[index- (pLength - 1)]] == 0:
                del sCounter[s[index - (pLength - 1)]]
        return indeces
