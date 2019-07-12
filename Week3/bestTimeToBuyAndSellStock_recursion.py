class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        def profit(j):
            if j == 0:
                return 0
            else:
                recursiveValue = profit(j-1)
                for k in range (0, j):
                    recursiveValue = max(recursiveValue, prices[j-1] - prices[k])
                return recursiveValue

        return profit(len(prices))
