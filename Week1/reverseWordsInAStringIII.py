class Solution:
    def reverseWords(self, s: str) -> str:
        phrase = ''
        word =''
        reverseWord = ''
        spaces = []

        for j in range(len(s)):
            if (s[j] == ' '):
                spaces.append(j)

        if (len(spaces) == 0):
            return s[::-1]

        for i in range(len(s)):
            if (s[i] != ' ' and i < spaces[len(spaces)-1]):
                word = word + s[i]
            if (s[i] == ' '):
                reverseWord = word[::-1]
                phrase = phrase + reverseWord + ' '
                word = ''
            if (i > spaces[len(spaces)-1]):
                word = word + s[i]
            if (i == len(s) - 1):
                reverseWord = word[::-1]
                phrase = phrase + reverseWord
                word = ''

        return phrase
                
