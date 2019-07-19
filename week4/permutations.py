class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # using recursion

        if len(nums) == 0:
            return [[]]
        else:
            # every time a function is called permutations array is emptied
        
            permutations = []
            # use length of nums and the previous permutation subset to calculate
            # next subset
            for subset in self.permute(nums[1:]):
                for j in range(len(nums)):
                    # places element each element of A and uses other two elements
                    # to calculate permutations
                    permutation = subset[:j] + [nums[0]] + subset[j:]
                    permutations.append(permutation)
            return permutations
