from collections import Counter
class Solution:
    def longestWord(self, words: List[str]) -> str:
        #create a root dict and end word signal
        trie, _end = dict(), '*'

        # put all words in a dictionary in a Trie
        for word in words:
            helper = trie
            for letter in word:
                helper = helper.setdefault(letter,{})
            # marks the end of the word
            helper[_end] = _end

        # setup wordcopy arrays to help find the longest word in the Array
        wordsCopy, failedTest, j = words[:], [], -1
        print(wordsCopy)

        # true until the appropriate word is found
        while j == -1:
            #set up a subtrie equal trie I create above, and set longest Word Variable
            subTrie, longestWord = trie, ''
            # if longest word cannot be put together letter by letter, it is removed
            # from wordsCopy
            if len(failedTest) == 1:
                wordsCopy.remove(failedTest[0])

            # Find the longest Word in array
            multipleWords, currentMax = [], 0
            for w in wordsCopy:
                if len(w) > currentMax :
                    currentMax = len(w)
                    longest = w
            multipleWords.append(longest)

            # Pull out an other words that share the same length as the longest
            # word found above
            for i in wordsCopy:
                if len(i) == len(multipleWords[0]) and i != multipleWords[0]:
                    multipleWords.append(i)

            # select the words lexologically smaller
            longestWord = min(multipleWords)

            # search Trie to see if word can be put together letter by letter
            for letter in longestWord:
                if letter in subTrie:
                    subTrie = subTrie[letter]
                # if letter does not have an end marker associated with it, that word
                # that letter belongs to cannot be put together letter by letters
                if _end not in subTrie:
                    failedTest = []
                    # place that word in the failed Test array (it will be removed from wordsCopy)
                    failedTest.append(longestWord)
                    break
            # if long word is in the trie it will have an end marker, and it will
            # be returned
            else:
                if _end in subTrie:
                    j = 0
                    return longestWord
                else:
                    return False
