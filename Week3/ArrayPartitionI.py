class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        count, i = 0, 0

        # to get min, once array is sorted, take every other number
        # (this will be the minimum of the pairs) and sum them
        #
        while i < len(nums):
            count = count + nums[i]
            i = i + 2
        return count
