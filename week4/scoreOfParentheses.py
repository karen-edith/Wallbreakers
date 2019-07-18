class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = []

        for i in S:
            # when string value is equal to ( push it on to stack
            if i == '(':
                stack.append(i)
                score = 0
            # when string value is equal to ) check to see what its closing
            elif i == ')':
                top = stack.pop()
                # if closing neigbor then push the value of 1 onto stack
                if top == '(':
                    stack.append(1)
                # if popped value is a value find the value inside of parenthesis
                # its closing
                else:
                    while top != '(':
                        # whatever is inside the parentheses gets multiplied by two
                        score = score + 2*top
                        # pop off the next stack value before appending score
                        top = stack.pop()
                    stack.append(score)
                    score = 0
        return sum(stack)
