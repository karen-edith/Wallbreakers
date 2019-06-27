class Solution:
    def isPalindrome(self, s: str) -> bool:
        letterString = ''

        for i in range(len(s)):
            if (s[i].isalpha() or s[i].isdigit()):
                letterString = letterString + s[i].lower()

        if (letterString == ''):
            return True
        if (letterString[::-1] == letterString):
            return True
        if (letterString[::-1] != letterString):
            return False
