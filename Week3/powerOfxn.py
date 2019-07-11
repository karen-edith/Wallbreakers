class Solution:
    def myPow(self, x: float, n: int) -> float:
        # once n reaches base, return 1
        if n == 0:
            return 1
        # if power is negative calculate the inverse, where denominator is calculated
        # with normally by converting negative n to positive n
        if n < 0:
            return 1 / self.myPow(x, -n)
        # if n is not even then we have to take into account the extra base value
        # that gets multiplied when calculating power
        if n % 2 != 0:
            return x * self.myPow(x, n-1)
        # if n is even then n is divided by two square calculate x^(n/2) and square
        # that value
        else:
            return self.myPow(x*x, n/2)
