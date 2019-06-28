class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        checker = {}

        if len(s) != len(t):
            return False

        for char in s:
            if char not in checker:
                checker[char] = 1
            else:
                checker[char] += 1


        for char in t:
            if char in checker:
                checker[char] -= 1
            else:
                return False

        print(checker)

        for val in checker.values():
            if val != 0:
                return False

        return True
