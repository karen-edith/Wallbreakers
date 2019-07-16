# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:

        if head == [] or head == None:
            return head

        # setup current, odd and even headers
        current, nextNode, evenHeader = head, current.next, current.next

        # initiate counter that help keep track of even and odd nodes
        i = 1
        while current.next != None:
            # links current node with next odd/even node
            current.next = nextNode.next
            # if node is odd break out of the while loop before current and nextNode
            # are calculated, this will allow the even length node list to link
            # even numbers to the last odd number
            if current.next == None and i % 2 != 0:
                break
            # next node becomes the current node
            current = nextNode
            nextNode = current.next
            i = i + 1
        # corresponding even header gets attached to corresponding last odd node
        current.next = evenHeader
        return head
