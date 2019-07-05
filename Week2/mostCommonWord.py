from collections import defaultdict
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # create a words counter initiated with 0 as values
        # create a punctuation array
        wordsCounter, punctuation = defaultdict(int), ['?', '!', ',', ';', "'", '.']

        #remove punctuation from paragraph
        for j in punctuation:
            #replace , with a space and other punctuation with ''
            if j in punctuation and j == ',':
                  paragraph = paragraph.replace(j, ' ')
            elif j in paragraph:
                paragraph = paragraph.replace(j, '')

        # after punctuation removed, split the words in the paragraph into an array
        words = paragraph.split(' ')

        # place words (except and spaces and banned words) in the wordsMap
        for i in range(len(words)):
            word = words[i].lower()
            if word not in banned and word!='':
                # count the number of times each word is used
                wordsCounter[word] = wordsCounter[word] + 1

        #find the maximum value in words map
        highestFrequency = max(wordsCounter.values())

        # print the key(word) that coressponds to that max value
        for key, value in wordsCounter.items():
            if value == highestFrequency:
                return key
