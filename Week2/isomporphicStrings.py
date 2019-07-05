from collections import Counter
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # setup empty letter dictionary to create s[i]-t[i] pair letter map
        letterMap = {}

        # if both s and t are empty strings they are isomorphic
        if len(s) == 0 and len(t) == 0:
            return True

        # place new s[i]-t[i] pair in letterMap
        for i in range(len(s)):
            # check to see if key s[i] part of letter Map
            if s[i] not in letterMap:
                 # if no check to see if corresponding t[i] value is mapped to a different key
                if t[i] in letterMap.values():
                    return False # if mapped to a different key then word is not isomorphic
                letterMap[s[i]] = t[i]
            # if key does exist check to see if key has been mapped to a different
            # value then the corresponding t[i] value
            else:
                if letterMap[s[i]] != t[i]:
                    return False
                    # if it has been mapped to a different value then
                    #words are not isomorphic

        return True
