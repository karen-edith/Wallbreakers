class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}

        for i, x in enumerate(nums):
            if target - x in index:
                return [index[target - x], i]
            index[x] = i
