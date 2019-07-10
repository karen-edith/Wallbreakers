class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:

        minimum = 0
        maximum = len(A) -1

        while minimum < maximum:
            # find the middle index of Array between maximum and minimum values
            middleIndex = int((minimum + maximum)/2)
            # if value assigned to that index is less than the value after it,
            # then the value after it (and thus index) becomes the new minimum
            if A[middleIndex] < A[middleIndex + 1]:
                minimum = middleIndex + 1
            # if value assigned to that index is greater than the value after it,
            # then our current index becomes the new maximum value
            else:
                maximum = middleIndex
        return minimum
