class Solution:
    def titleToNumber(self, s: str) -> int:

        colNum = 0
        for i in s:
            if i in string.ascii_letters:
                colNum = colNum * 26 + (ord(i.upper()) - ord('A')) + 1
        return colNum
