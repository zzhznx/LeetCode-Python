from Tree_zzh import tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
Let

f1(node) be the value of maximum money we can rob from the subtree with node as root ( we can rob node if necessary).

f2(node) be the value of maximum money we can rob from the subtree with node as root but without robbing node.

Then we have

f2(node) = f1(node.left) + f1(node.right) and

f1(node) = max( f2(node.left)+f2(node.right)+node.value, f2(node) ).
"""

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.robDFS(root)[1]

    def robDFS(self, root):
        if not root:
            return (0, 0)
        l = self.robDFS(root.left)
        r = self.robDFS(root.right)
        return (l[1] + r[1], max(l[1] + r[1], l[0] + r[0] + root.val))

root = tree.get_one()
solution = Solution()
print(solution.rob(root))