from collections import deque
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        # append queue on the left when adding elements so that the last element
        # is on top
        self.queue.appendleft(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return (self.queue.popleft())

    def top(self) -> int:
        """
        Get the top element.
        """
        # pop item off to get value then append to it to list at same place
        item = self.queue.popleft()
        self.queue.appendleft(item)
        return (item)

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if len(self.queue) == 0:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
