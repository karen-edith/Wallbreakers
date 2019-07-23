"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        # array to append the postorder node values to
        postOrderTraversal = []

        def porder(root):
            # loop through children nodes and for each child node have the
            # function call itself again
            for child in root.children:
                porder(child)
            # append the root node value to the postOrderTraversal Array
            postOrderTraversal.append(root.val)

        porder(root)
        return postOrderTraversal
