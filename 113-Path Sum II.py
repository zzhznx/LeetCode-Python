from Tree_zzh import tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return []
        val, kids = root.val, (root.left, root.right)
        if any(kids):
            return [[val] + path
                    for kid in kids
                    for path in self.pathSum(kid, sum - val)]
        return [[val]] if val == sum else []

root = tree.get_one()
solution = Solution()
print(solution.pathSum(root, 15))