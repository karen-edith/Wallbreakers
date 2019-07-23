# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:

        if not root:
            return 0

        leftLeavesSum = []

        def leftSum(root) :
            # check to see if left child node of current node has a left child node
            # if it does function calls itself again
            if root.left and root.left.left:
                leftSum(root.left)
            # check to see if current node has right child node
            # if it does function calls itself again
            if root.right:
                leftSum(root.right)
            # check to see if left child node of current node has children
            # if none, then its a left left and we append it to leftLeavesSum array
            if root.left and not root.left.left and not root.left.right:
                leftLeavesSum.append(root.left.val)
            # check to see if left child of current node has only a right child node
            # if so, then function calls itself passing in that right child node 
            if root.left and not root.left.left and root.left.right:
                leftSum(root.left.right)

        leftSum(root)
        return sum(leftLeavesSum)
