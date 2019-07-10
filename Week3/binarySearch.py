class Solution:
    def search(self, nums: List[int], target: int) -> int:
        minimum, maximum = 0, len(nums) - 1
        guess = 0

        # if array only has one element, if it matches the target return 0
        # otherwise return -1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        # binary search will run as long as maximum is greater than or equal to
        # minimum (when maximum < minimum value is not in array)
        while maximum >= minimum:
            # find middle of array
            guess = int((maximum + minimum)/2)
            # if middle value is equal to target return index
            if nums[guess] == target:
                return guess
            # if middle value is not equal to target value and less than target
            elif nums[guess] < target:
                # increase minimum by 1 to find new middle point
                minimum = guess + 1
            # if middle value greater than
            else:
                # decrease minimum by 1 to find new middle point
                maximum = guess -1
        return -1
