from collections import defaultdict
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        # setup count dictionary, split words in string A and B into arrays, setup uniqueWords list
        totalWordCount, wordsA, wordsB, uniqueWords = defaultdict(int), A.split(' '), B.split(' '), []

        for i in wordsB:
            wordsA.append(i) # place all words in a single Array

        for i in wordsA:
            # countwords and assign count value to corresponding key
            totalWordCount[i] = totalWordCount[i] + 1

        # search totalWordCount map to find words with count equal to 1
        for key, value in totalWordCount.items():
            if value == 1:
                uniqueWords.append(key)

        return uniqueWords
