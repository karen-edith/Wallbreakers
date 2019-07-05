from collections import Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        #sort nums array
        nums = sorted(nums)
        #create a counter for nums and an empty array to put final values in
        numsCounter, duplicateMissing = Counter(nums), []

        # find the number with the highest frequency
        maximum = max(numsCounter, key=numsCounter.get)
        duplicateMissing.append(maximum)

        # all numbers between 1 and n should be in the array nums
        # check the number for which this fails, return that number as its the
        # missing value
        for i in range(len(nums)):
            if i + 1 not in nums:
                duplicateMissing.append(i+1)
                return duplicateMissing
