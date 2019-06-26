class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digitsCopy = digits.copy()
        lastDigitPlusOne = digitsCopy[len(digits)-1] + 1
        counts = 0
        notNine = 0

        for i in reversed(range(len(digits))):
            if(digits[i] != 9):
                notNine = i
                break
            else:
                counts = counts + 1

        if counts == len(digits):
            digitsCopy = [1,0]
            for k in range(1, len(digits)):
                digitsCopy.append(0)
        else:
            for j in range(notNine,len(digits)):
                if (j == notNine):
                    digitsCopy[j] = digits[j] + 1
                else:
                    digitsCopy[j] = 0

        return digitsCopy
