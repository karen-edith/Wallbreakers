class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # first subset element for any nums array is an empty array so, initiate
        # subsets array with empty array
        subsets = [[]]
        for element in nums:
            for i in range(len(subsets)):
                # as subsets array keeps on growing, element from nums array
                # get added to prior subset array
                subsets.append(subsets[i] + [element])
        return subsets
