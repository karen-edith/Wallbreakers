class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        allUpperCase = word.isupper()
        allLowerCase = word.islower()
        firstUpperCase = word[0].isupper()
        correct = False

        if (allUpperCase == True):
            correct = True
        elif(allLowerCase == True):
            correct = True
        elif(firstUpperCase == True):
            for i in range(1, len(word)):
                if( word[i].isupper()):
                    correct = False
                    break
                else:
                    if(i == len(word)-1):
                        correct = True
        else:
            correct = False

        return correct
