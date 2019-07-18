class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.helperStack = []
        self.length = 0

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)
        self.length += 1

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        # pops off top of stack and places it in a new stack
        # top of the new stack is now the bottom of the previous stack
        while self.stack:
            self.helperStack.append(self.stack.pop())
        # pop off last element of new stack and subtract 1 from the counter that
        # keeps track of length
        item = self.helperStack.pop()
        self.length += - 1

        # take elements in stack, pop them off one by one and place them back in the
        # stack (this will remove the front element and preserve the order of the
        # original stack) 
        while self.helperStack:
            self.stack.append(self.helperStack.pop())

        return item


    def peek(self) -> int:
        """
        Get the front element.
        """
        while self.stack:
            self.helperStack.append(self.stack.pop())

        item = self.helperStack.pop()
        self.helperStack.append(item)

        while self.helperStack:
            self.stack.append(self.helperStack.pop())

        return item


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.

        """
        if self.length == 0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
