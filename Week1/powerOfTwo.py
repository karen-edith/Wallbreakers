class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        print ((bin(n))[2])
        if (bin(n).count('1') == 1 and str(bin(n))[2] == "1"):
            return True
        else:
            return False
