class Solution:
    def partitionLabels(self, S: str) -> List[int]:

        finalPositions, answerArray = {}, []
        letter, letterPosition, count = '', -1, 0

        # create a hash map that maps letters to their final index position
        for i in range(len(S)):
            finalPositions[S[i]] = i

        # break string up into parts based on letter presence
        for i in range(len(S)):
            count = count + 1
            # check to see if position of letter in string is within final
            # position of first letter, if it isnt that indicates the begining of
            # a new part, that final positions of first letter in that new part
            # becomes the comparision index
            if letter != S[i] and finalPositions[S[i]] > letterPosition:
                letter = S[i]
                letterPosition = finalPositions[S[i]]
            # once we reach the position of comparision final letter that indicates
            # the ending of a part, the count indicates the number of letters so
            # it gets placed into the answer array and the letter, letterPosition
            # and cound variable get reset for the next part in the string
            if i == letterPosition:
                answerArray.append(count)
                letter, letterPosition, count = '', -1, 0
        return answerArray
