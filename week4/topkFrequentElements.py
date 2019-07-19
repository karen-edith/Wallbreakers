from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap, mostFrequent = [], []
        # map value to frequency of value
        count = Counter(nums)

        for key, value in count.items():
            # create tuple with value, key elements
            keyValuePair = (value, key)
            # pop out lowest value of heap when comparing three keyValuePair tuples
            # at a time
            if len(heap) >= k:
                heapq.heappushpop(heap, keyValuePair)
            else:
                heapq.heappush(heap, keyValuePair)

        for j in range(len(heap)):
            # pop out lowest keyValuePair item from heap and append it to the
            # mostFrequent value
            mostFrequent.append(heapq.heappop(heap)[1])
        return mostFrequent[::-1]
