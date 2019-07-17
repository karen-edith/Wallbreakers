class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        if len(nums1) == 0 or len(nums2) == 0:
            return []

        helperStack = []
        nextGreaterMap = {}
        # setting first element of helper stack to be first element in nums2 array
        helperStack.append(nums2[0])
        nextGreaterArray = []

        for i in range(1, len(nums2)):
            # compare elements in nums2 array with neighbor element
            # if an elements neighbor element is larger than itself
            # pop the element in the stack pair the element (key) with the
            # neighboring value (value) in the map
            while helperStack and helperStack[-1] < nums2[i]:
                nextGreaterMap[helperStack.pop()] = nums2[i]
            # append next element to helper stack and repeat comparison
            helperStack.append(nums2[i])

        for j in range(len(nums1)):
            # use map to find num1 elements and if they are in map, find their
            # corresponding next greater value
            if nums1[j] in nextGreaterMap:
                nextGreaterArray.append(nextGreaterMap[nums1[j]])
            else:
                nextGreaterArray.append(-1)

        return nextGreaterArray
