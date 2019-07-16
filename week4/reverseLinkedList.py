# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        if head == [] or head == None:
            return head

        # initializing markers that will allow for while loop to re-link nodes
        previous, current, nextNode = None, head, current.next

        # if nextNode is none, that means we've reached the second to last
        # node in the linked list
        while nextNode != None:
            # link current node to previous node
            current.next = previous
            # the current node now becomes the previous node
            previous = current
            # next node becomes the current node
            current = nextNode
            # next node become the node after current(above) node
            nextNode = nextNode.next
        # loop ends with second to last node of original linked list, so
        # link the second the last node to parameter previous
        current.next = previous
        # head becomes the current node (last)
        head = current
        return head
