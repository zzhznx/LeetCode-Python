# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        left = self.depth(root.left)
        right = self.depth(root.right)

        return abs(left - right) and self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, root):
        if root is None:
            return 0
        return max(self.depth(root.left), self.depth(root.right))


    def isBalanced2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfsHeight(root) != -1

    def dfsHeight(self, root):
        if root is None:
            return 0

        leftHeight = self.dfsHeight(root.left)
        if leftHeight == -1:
            return -1

        rightHeight = self.dfsHeight(root.right)
        if rightHeight == -1:
            return -1

        if abs(leftHeight - rightHeight) > 1:
            return -1
        return max(leftHeight, rightHeight) + 1