class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) <= 3 and len(nums) != 0:
            return max(nums)
        if len(nums) == 0:
            return 0

        memoFirst, memoSecond, length  = {}, {}, len(nums)

        # recursive relation to solve for the max looking at all houses except the last
        def startFirstHouse(i):
            # base case for indeces corresponding to the last house or larger
            if i >= length - 1:
                return 0
            # if we've already calculated the value for this iteration (if its already)
            # stored in our cache dictionary, we return that value for that iteration
            if i in memoFirst:
                return memoFirst[i]
            # because we are omitting the last house once we reach the second to last house
            # we return the nums value for that house at that iteration
            if i == length - 2:
                return nums[i]
            # calculate the currentMax by comparing the max amount of loot at each iteration with
            # the previous and the previous previous max values
            currentMax = max(nums[i] + startFirstHouse(i+2), startFirstHouse(i+1))
            # if not already in the cache dictionary, store iteration value
            memoFirst[i] = currentMax
            return currentMax

        # recursie relation to solve for the max looking at all houses except the first one
        def omitFirstHouse(j):
            # base case for indeces corresponding to any house index larger then the
            # last house
            if j >= length:
                return 0
            if j in memoSecond:
                return memoSecond[j]
            # because we are omitting the last first once we reach the last house
            # we return the nums value for that house at that iteration
            if j == length - 1:
                return nums[j]
            currentMax = max(nums[j] + omitFirstHouse(j+2), omitFirstHouse(j+1))
            memoSecond[j] = currentMax
            return currentMax

        # 0 indicates that we include the first house, 1 indicates that we omit the first house
        return max(startFirstHouse(0), omitFirstHouse(1))
