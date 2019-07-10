class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sSorted, tSorted = sorted(s), sorted(t)
        # if sorted letter strings don't contain the same letter then they aren't
        # neither is an anagram
        if sSorted == tSorted:
            return True
        else:
            return False
