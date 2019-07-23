# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:

        leafSequence1, leafSequence2 = [], []

        # recursion for tree 1
        def leaves1(root):
            # if node has both a right and left child, call function again for both
            # children (left first then right node )
            if root.left and root.right:
                leaves1(root.left)
                leaves1(root.right)
            # if node has only left child node then call itself again only for left node
            elif root.left and not root.right:
                leaves1(root.left)
            # if node has only right child node then call itself again only for right node
            elif not root.left and root.right:
                leaves1(root.right)
            # if node has neither left or right children, its a leaf value so append it
            # to leafSequence1 array
            else:
                leafSequence1.append(root.val)

        # recursion for tree 2, logic is the same as for tree 1
        def leaves2(root):
            if root.left and root.right:
                leaves2(root.left)
                leaves2(root.right)
            elif root.left and not root.right:
                leaves2(root.left)
            elif not root.left and root.right:
                leaves2(root.right)
            else:
                leafSequence2.append(root.val)

        leaves1(root1)
        leaves2(root2)

        # if leaf array for tree 1 and tree 2 match then return true
        if leafSequence1 == leafSequence2:
            return True
        else:
            return False
