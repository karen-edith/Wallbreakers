class Solution:
    def findComplement(self, num: int) -> int:
        binaryNumberString = bin(num)[2:]
        complementBinaryString = ''

        for i in binaryNumberString:
            binaryInteger = int(i)
            if (binaryInteger == 1):
                complementBinaryString = complementBinaryString + '0'
            else:
                complementBinaryString = complementBinaryString + '1'
        return (int(complementBinaryString, 2))
        
