# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.helper(root, None)

    def helper(self, root, pre):
        if not root:
            return pre
        pre = self.helper(root.right, pre)
        pre = self.helper(root.left, pre)
        root.right = pre
        root.left = None
        pre = root
        return pre