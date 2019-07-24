# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        if not root:
            return 0

        # to find the diameter of the binary tree we need to find the height
        # of left left and right subtrees

        # recursive function that will find the height of each subtree
        def height(root):
            if not root:

                return 0
            # adds 1 to find the height of the tree that includes the root node
            return 1 + max(height(root.left), height(root.right))

        # recurseive function that finds the diameter of the binary tree.
        # As we move down nodes, we pass in subtrees and its left and right
        # children are used to find the subtree height and thus its diameter
        def btDiameter(root):
            if not root:
                return 0

            leftHeight = height(root.left)
            rightHeight = height(root.right)

            leftDiameter = btDiameter(root.left)
            rightDiameter = btDiameter(root.right)

            return max(leftHeight + rightHeight + 1, max(leftDiameter, rightDiameter))

        return btDiameter(root) - 1
