class Solution:
    def calPoints(self, ops: List[str]) -> int:

        if len(ops) == 1:
            return int(ops.pop())

        # reverse the order of ops to have first inning at top (bottom) of stack
        reversedOps, ops2, pointSum = ops[::-1], [], 0
        i = 0

        while i < len(ops):
            # remove top value from stack
            top = reversedOps.pop()
            # if its a number then add it to the points sum and add removed value to
            # helper stack
            if top.isalpha() == False and top != '+' :
                pointSum = pointSum + int(top)
                ops2.append(top)
            # if removed value is C then remove previously summed points from sum and remove
            # value from helper stack
            elif top == 'C':
                top2 = ops2.pop()
                pointSum = pointSum - int(top2)
            # if removed value is D take top value from helper stack and double it
            # append that doubled value to helper stack and add it to the overall point sum
            elif top == 'D':
                top2 = ops2.pop()
                pointSum = pointSum + 2*int(top2)
                ops2.append(top2)
                ops2.append(str(2*int(top2)))
            # if removed value is + take top two values from helper stack and add them
            # append that sum to the helper stack and add it to the sum
            elif top == '+':
                # remove values
                t2 = ops2.pop()
                t1 = ops2.pop()
                tadd = int(t2) + int(t1)
                pointSum = pointSum + tadd
                # append values in correct order back to helper stack
                ops2.append(t1)
                ops2.append(t2)
                ops2.append(str(tadd))
            i = i + 1
        return pointSum
