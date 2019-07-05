import collections
class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        # create empty set to store special equivalent numSpecialEquivGroups
        specialEquivalentGroups = set()
        for string in A: # loop through strings in list A
            # even index switch for string W, sort alphabetically
            evenIndeces = ''.join(sorted(string[0::2]))
            # even index switch for string W, sort alphabetically
            oddIndeces = ''.join(sorted(string[1::2]))
            # add tuple evenIndeces,oddIndeces to set
            specialEquivalentGroups.add((evenIndeces,oddIndeces))
            # set values are unique, so len of SpecialEquivalentGroups is to used
            # to determine number of groups
        return len(specialEquivalentGroups)
