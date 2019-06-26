class Solution:
    def binaryGap(self, N: int) -> int:
        n = bin(N)[2:]
        print(n)
        indexForOne = []
        difference = []

        for i in range(len(n)):
            if (n[i] == '1'):
                indexForOne.append(i)

        for j in range(len(indexForOne)):
            if (j != len(indexForOne) - 1):
                print(indexForOne[j+1])
                diff = int(indexForOne[j + 1]) - int(indexForOne[j])
                difference.append(diff)

        return max(difference, default = 0)
