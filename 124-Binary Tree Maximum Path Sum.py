import sys
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            l = r = 0
            ls = rs = None
            if node.left:
                l, ls = dfs(node.left)
                l = max(0, l)
            if node.right:
                r, rs = dfs(node.right)
                r = max(0, r)
            return node.val + max(l, r), max(ls, rs, l + r + node.val)

        if root:
            return dfs(root)[1]
        return 0
