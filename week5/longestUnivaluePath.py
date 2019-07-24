# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:

        answer = [0]

        # recursive function that will call itself for all sum up their path
        # containing equal values
        def uniValuePath(root, answer):
            if not root:
                return 0

            # function calls itself passing in children node along with the current
            # longest path
            left = uniValuePath(root.left, answer)
            right = uniValuePath(root.right, answer)

            # variables used to determine longest current path
            leftMax, rightMax = 0, 0

            # if left child node is equal in value to parent node then add 1 to left counter
            if (root.left and root.left.val == root.val):
                leftMax = leftMax + left + 1

            # if right child node is equal in value to parent node then add 1 to right counter
            if (root.right and root.right.val == root.val):
                rightMax = rightMax + right + 1

            # record the sum of these two vales in answer array
            answer[0] = max(answer[0], leftMax + rightMax)
            # return the max value of the two max values calculated above
            return max(leftMax, rightMax)

        uniValuePath(root, answer)
        return answer[0]
