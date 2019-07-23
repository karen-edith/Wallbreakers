# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        if (not p and q) or (p and not q):
            return False
        if (not p and not q):
            return True

        tree1, tree2 = [], []
        nodeValueT1, nodeValueT2 = p.val, q.val

        # put nodes of Tree 1 in array
        def nodes1(p, nodeValueT1):
            tree1.append(nodeValueT1)
            # if node contains both left and right child nodes call function for both
            # seperately
            if p.left and p.right:
                nodes1(p.left, p.left.val)
                nodes1(p.right, p.right.val)
            # if node contains only right child node append null to node array and then
            # call have function call itself only for right child
            elif not p.left and p.right:
                tree1.append(None)
                nodes1(p.right, p.right.val)
            # if node contains only left child node then have function call itself for
            # left child node
            elif p.left and not p.right:
                nodes1(p.left, p.left.val)

        # put nodes of Tree 1 in array
        # same logic for nodes 1 function
        def nodes2(q, nodeValueT2):
            tree2.append(nodeValueT2)
            if q.left and q.right:
                nodes2(q.left, q.left.val)
                nodes2(q.right, q.right.val)
            elif not q.left and q.right:
                tree2.append(None)
                nodes2(q.right, q.right.val)
            elif q.left and not q.right:
                nodes2(q.left, q.left.val)

        nodes1(p, nodeValueT1)
        nodes2(q, nodeValueT2)

        if tree1 == tree2:
            return True
        else:
            return False
