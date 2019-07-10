class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # if input intervals array is empty return empty
        if len(intervals) == 0:
            return []

        # if input intervals array contains only one element return the input
        if len(intervals) == 1:
            return intervals

        intervals = sorted(intervals)
        beginningValue, endValue = intervals[0][0], intervals[0][1]
        merged, helper, i = [], [], 1

        while i < len(intervals):
            # check to see that end point of current start-end pair is less than
            # or equal to next start value, if it is new interval begins so
            # put those values in an array and then put that array in the merged
            # array
            if intervals[i][0] > endValue:
                helper.append(beginningValue)
                helper.append(endValue)
                merged.append(helper)
                helper = []
                beginningValue, endValue = intervals[i][0], intervals[i][1]
                # if last start-end pair in input array met above criteria,
                # place those values in helper array then place that
                # array in merged array
                if i == len(intervals) - 1:
                    helper.append(beginningValue)
                    helper.append(endValue)
                    merged.append(helper)
            elif intervals[i][1] > endValue:
                # if above criteria not met that indicates that start-end points
                # overlap and we check the end points to choose the largest of the
                # two to become the new endpoint
                endValue = intervals[i][1]
                # if met above criteria and last start-end point pair in input
                # array the append current start and end point to helper array
                # then place that array in merged array.
                if i == len(intervals) - 1:
                    helper.append(beginningValue)
                    helper.append(endValue)
                    merged.append(helper)
            # if neither of the criteria above is met and we're on the last start
            # -end pair then place those values in merged value
            elif i == len(intervals) - 1:
                helper.append(beginningValue)
                helper.append(endValue)
                merged.append(helper)
            i = i + 1
        return merged
