class Solution:
    def hammingDistance(self, x: int, y: int) -> int:

        binx, biny = bin(x)[2:], bin(y)[2:]
        count = 0
        addedZeroString =''
        mainBinaryNumber = ''
        secondaryBinaryNumber = ''

        if (len(binx) != len(biny)):
            lengthDifference = len(binx) - len(biny)
            if (lengthDifference > 0):
                for i in range(abs(lengthDifference)):
                    addedZeroString = addedZeroString + '0'
                    mainBinaryNumber = addedZeroString + biny
                    secondaryBinaryNumber = binx
            else:
                 for i in range(abs(lengthDifference)):
                    addedZeroString = addedZeroString + '0'
                    mainBinaryNumber = addedZeroString + binx
                    secondaryBinaryNumber = biny
        else:
            mainBinaryNumber = binx
            secondaryBinaryNumber = biny

        for i in range(len(mainBinaryNumber)):
            if (mainBinaryNumber[i] != secondaryBinaryNumber[i]):
                count = count + 1
        return count
