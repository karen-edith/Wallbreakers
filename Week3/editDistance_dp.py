class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # solved using replace, remove, insert matrix

        # creating a 2d array the contains length of word 2 columns + 1 and length of word1 + 1
        # rows because word1 is what we are trying to mutate to word2. The 1 comes
        # from a row and a culmn that represent null string
        operationsCache = [[0]*(len(word2) + 1) for i in range(len(word1) + 1)]

        # fill the table in, the last col and row element will be the minimum number
        # of operations required to mutate word1 to word2
        for i in range(len(word1) + 1):
            for j in range(len(word2) + 1):
                # set first element of the 2d array equal to zero, representing null strings
                if i == 0 and j == 0:
                    operationsCache[i][j] = 0
                # set elements of row equal to the number of insertions that it would take to
                # complete word2 from empty string
                elif i == 0:
                    operationsCache[i][j] = operationsCache[i][j-1] + 1
                # set elements of column equal to the number of insertions that it would take to
                # complete word1 from empty string
                elif j == 0:
                    operationsCache[i][j] = operationsCache[i-1][j] + 1
                # fill the reminaing table
                else:
                    # if a letter in string 1 and string two match copy the value from the diagonal
                    # element above it
                    if word1[i-1] == word2[j-1]:
                        operationsCache[i][j] = operationsCache[i-1][j-1]
                    # otherwise find the minimum value between first element above (deletion),
                    # first element to the left (insertion), and first above digonal(replacement)
                    else:
                        operationsCache[i][j] = 1 + min(operationsCache[i-1][j], operationsCache[i][j-1], operationsCache[i-1][j-1])
        # return last value of the 2d array
        return operationsCache[len(word1)][len(word2)]
