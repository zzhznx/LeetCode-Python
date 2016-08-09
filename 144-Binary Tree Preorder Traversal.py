# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if root is not None:
            res.append(root.val)
            self.helper(root.left, res)
            self.helper(root.right, res)

    def preorderTraversal2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack, res = [root], []
        while stack:
            node = stack.pop()
            if node is not None:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res
