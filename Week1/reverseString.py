class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        for i in range (len(s)//2):
            a,b = s[len(s) - (i + 1)], s[i]
            s[i],s[len(s) -( 1 + i)] = a, b
