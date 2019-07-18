class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if len(nums) > 1:
            i = 1
            while i <= k:
                # pop the last element and insert it at the front
                nums.insert(0,nums.pop())
                i = i + 1
        
