class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        left, right, string = n, 0, ''
        combinations = []

        def parenthesis(left, right, string):
            # once left and right parenthesis count is equal to 0 then append that
            # combination to array
            if left == 0 and right == 0:
                combinations.append(string)

            # if left count is not 0 then add open parenthesis to string and iterate
            # until both left and right counters are at a value of 0
            if left > 0:
                parenthesis(left - 1, right + 1, string + '(')

            # if right count is not 0 then add closing parenthesis to string and iterate
            # until both left and right counters are at a value of 0
            if right > 0:
                parenthesis(left, right - 1, string + ')')

        parenthesis(left, right, string)
        return combinations
