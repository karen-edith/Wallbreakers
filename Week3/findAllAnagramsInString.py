from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        p = sorted(p)
        indeces = []
        words = []
        sortedWords = []
        ordSum = 0
        pSum = 0

        for i in range (len(s) - (len(p) - 1)):
            words.append(s[i:i+len(p)])

        for k in words:
            k = sorted(k)
            sortedWords.append(k)

        for j in range(len(sortedWords)):
            if sortedWords[j] == p:
                indeces.append(j)

        return indeces


        '''i = 0
        while i < len(s) - (len(p) - 1):
            if (sorted(s[i:i+len(p)])) == p:
                indeces.append(i)
            i = i + 1
        return indeces'''
                
