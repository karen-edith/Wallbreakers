class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:

        count = 0
        selfDividing = []

        for i in range(left, right + 1):
                numberString = str(i)
                for j in range(len(numberString)):
                    if (int(numberString[j]) == 0):
                        break
                    if (int(numberString[j]) != 0):
                        divisible = i % int(numberString[j])
                    if(divisible == 0):
                        count = count + 1
                    if(j == len(numberString) - 1 and count == len(numberString)):
                        selfDividing.append(i)
                count = 0
        return selfDividing
