import queue
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    #recursive
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) if root else 0

    #iterative
    def maxDepth2(self, root):
        if root is None:
            return 0
        res = 0
        q = queue.Queue()
        q.put(root)
        while q.empty():
            res += 1
            n = q.qsize()
            for i in range(n):
                node = q.get()
                if node.left is not None:
                    q.put(node.left)
                if node.right is not None:
                    q.put(node.right)

        return res
