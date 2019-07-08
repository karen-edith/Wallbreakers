class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        # Check that all letters in shorter string s are in t
        # if not return False
        for k in s:
            if k not in t:
                return False

        # if either s or t are empty strings return True
        if s == '' or t == '':
            return True

        # initialize i, j, and count variables to 0
        i, j, count = 0, 0, 0


        while i < len(s) and j < len(t):
            # check letters in s one by one, if letter is equal to value in t
            # move on to next letter in both s string and t string and add 1 to count
            # this will keep track of the order of the as you move through both
            # arrays
            if s[i] == t[j]:
                i = i + 1
                j = j + 1
                count = count + 1
                # if count equals length of s that means we've already found all
                # three letters in the appropriate order
                if count == len(s):
                    return True
            # if above is not true, move to next letter in t string
            else:
                j = j + 1
        # if true hasn't been returned by the time we reach the end of j, then 
        # s is not a substring of t
        return False
