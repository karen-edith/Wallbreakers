# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:

        def bottomLeftValue(root, bottomLeft, height):
            if root == None:
                return

            # store current left most bottom value
            # if height is greater than previous height, replace previous
            # height and bottom left value with current values
            if height > bottomLeft[1]:
                bottomLeft[0] = root.val
                bottomLeft[1] = height

            # function calls itself for left values of first branch
            bottomLeftValue(root.left, bottomLeft, height + 1)
            # once left values are calculated other branch values left values
            # are compared agains the level and leftmost value of the first branch
            # if there is a higher level and thus different leftmost value it will get
            # updated
            bottomLeftValue(root.right, bottomLeft, height + 1)


        bottomLeft = [root.val, 0]
        bottomLeftValue(root, bottomLeft, 0)

        return bottomLeft[0]
