class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # create a a num1 set and num2 set, and setup and empty Array to fill with
        # numbers that intersect two arrays
        nums1Set, nums2set, intersectionArray = set(nums1), set(nums2), []

        # find the set of intersecting numbers
        numsIntersection = nums1Set.intersection(nums2set)

        # place intersecting set values in array
        for i in numsIntersection:
            intersectionArray.append(i)

        return intersectionArray
