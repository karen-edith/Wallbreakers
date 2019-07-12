class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) == 0:
            return 0

        # set up array array to store profits
        buySellDifference = [0] * len(prices)
        # initiate the current minimum with the first element of the array
        currentMin = prices[0]

        for i in range(1, len(prices)):
            # find the minimum between the current minimum and current price
            currentMin = min(currentMin, prices[i])
            # find difference between current price and current minimum
            # then find the maximum between what the previous maximum difference value
            # and store it in the buySellDifference array
            # if the difference is less than previous difference, difference carries through
            buySellDifference[i] = max(buySellDifference[i-1], prices[i] - currentMin)
        return buySellDifference[len(prices)-1]
