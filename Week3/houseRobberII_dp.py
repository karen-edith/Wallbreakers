class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        if sum(nums) == 0:
            return nums[0]

        if len(nums) <= 3:
            return max(nums)

        # set up two arrays, one to store max values that take into account the
        # first house but not the last, and the other one to store the max values
        # that take into account the last house but not the first
        maxRobbedFirst = [0]*(len(nums) - 1)
        maxRobbedSecond = [0]*(len(nums) - 1)
        # first value is in this array is the amount of money in the first house
        maxRobbedFirst[0] = nums[0]
        # first value in this array is the amount of money in the second house
        maxRobbedSecond[0] = nums[1]

        # the second value in the maxRobbedFirst array will be the max between the first
        # second value of the nums array
        if nums[0] >= nums[1]:
            maxRobbedFirst[1] = nums[0]
        if nums[0] < nums[1]:
            maxRobbedFirst[1] = nums[1]
        # the second value in the maxRobbedSecond array will be the max between the
        # second and third value of the nums array
        if nums[1] >= nums[2]:
            maxRobbedSecond[1] = nums[1]
        if nums[1] < nums[2]:
            maxRobbedSecond[1] = nums[2]

        # store max values calculated in each comparison
        # array including first house but excluding last
        for i in range(2, len(maxRobbedFirst)):
            # compare the previously stored max value, with the sum of the max value two
            # places behind and the current value
            # maximum between these two gets stored as the maximum at that position
            maxRobbedFirst[i] = max(maxRobbedFirst[i-1], maxRobbedFirst[i-2] + nums[i])
        # array including last house but excluding first house
        for j in range(3, len(maxRobbedSecond) + 1):
            # compare the previously stored max value, with the sum of the max value two
            # places behind and the current value
            # maximum between these two gets stored as the maximum at that position
            maxRobbedSecond[j-1] = max(maxRobbedSecond[j-2], maxRobbedSecond[j-3] + nums[j])
        #compare the last values (which contain the max values of each array) to find the max
        return max(maxRobbedFirst[len(maxRobbedFirst) - 1], maxRobbedSecond[len(maxRobbedSecond) -1])
