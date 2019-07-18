class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        if len(s) % 2 != 0:
            return False

        # use stack to compare neighboring string values
        stack = []
        # first value of stack is the first value of string
        stack.append(s[0])

        # starting with second string value
        for i in range (1, len(s)):
            # if stack is empty append the current string value to the stack and
            # continue on to the next iteration
            if len(stack) == 0:
                stack.append(s[i])
                continue
            # pop off the stack value
            top = stack.pop()
            # grab the current string value
            val = s[i]
            # if stack value and curent string value fall into any of the following
            # combinations continue on the the next iteration and don't append stack
            if (top == "(" and val == ")") or (top == "[" and val == "]") or (top == "{" and val == "}"):
                continue
            # otherwise, append stack value back to stack and append the current string value
            # to the stack afterwards
            else:
                stack.append(top)
                stack.append(val)
        # if stack is empty parenthesis were all in correct order
        if len(stack) == 0:
            return True
        else:
            return False
