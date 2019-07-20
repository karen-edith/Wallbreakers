class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = []
        for i in range(n):
            nums.append(i+1)

        def combinations(nums, k):
            if k == 0:
                return [[]]
            if len(nums) == k:
                return [list(nums)]
            result = [[nums[0]] + c for c in combinations(nums[1:], k - 1)]
            result += combinations(nums[1:], k)
            return result

        return combinations(nums, k)
