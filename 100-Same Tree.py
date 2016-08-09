# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is not None and q is not None:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q

    def isSameTree2(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        stack = [(p, q)]
        while stack:
            x, y = stack.pop()
            if x is None and y is None:
                continue
            if x is None or y is None:
                return False
            if x.val == y.val:
                stack.append((x.left, y.left))
                stack.append((x.right, y.right))
            else:
                return False
        return True

