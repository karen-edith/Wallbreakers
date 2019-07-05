from collections import Counter
class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        #setup counter dictionary for candies array, set up sisters candy list
        candiesCounter, sisterCandies = Counter(candies), []

        for key, value in candiesCounter.items():
            # if value for key is 1 add to sister candy list
            if (value == 1 and len(sisterCandies) < len(candies)/2):
                sisterCandies.append(key)

        for key in sisterCandies:
            # remove all the values from the candy counter dictionary
            candiesCounter.pop(key)

        # length of updated candies counter will determine the types of candy sister gets
        if (len(candies)/2) - len(sisterCandies) < len(candiesCounter):
            return (int(len(candies)/2))
        else:
            return len(candiesCounter) + len(sisterCandies)
