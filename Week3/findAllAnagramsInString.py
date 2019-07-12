from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        # does not work, i get an error of Time exceeds limit

        p = sorted(p)
        indeces = []
        words = []
        sortedWords = []
        ordSum = 0
        pSum = 0

        # create array with all possible anagrams (based on length of string)
        for i in range (len(s) - (len(p) - 1)):
            words.append(s[i:i+len(p)])

        # sort each word in the array and place sorted words in new array
        for k in words:
            k = sorted(k)
            sortedWords.append(k)

        # compare sorted word sorted p string, if the same append the index to
        # the indeces array
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
