class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {} # will use to cache recursions
        length = len(nums)

        def house(i):
            if len(nums) == 3:
                return nums[1]
            if i >= length:
                return 0
            # if specific recursion value has already been calculated return that
            # value from memo dictionary
            if i in memo:
                return memo[i]
            # recursively compare amount values
            currentMax= max(nums[i] + house(i+2), house(i+1))
            # if value not already in memo dictionary, place it in
            memo[i] = currentMax
            return currentMax

        return house(0)
