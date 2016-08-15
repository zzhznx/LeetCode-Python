from Tree_zzh import tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = []
        prev = None
        while root or len(stack) != 0:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            if prev and node.val <= prev.val:
                return False
            prev = node
            root = node.right
        return True

    def isValidBST1(self, root):
        return self.isValid(root, None, None)

    def isValid(self, root, min, max):
        if not root:
            return True
        elif min and root.val <= min:
            return False
        elif max and root.val >= max:
            return False
        return self.isValid(root.left, min, root.val) and self.isValid(root.right, root.val, max)

root = tree.get_one()
solution = Solution()
print(solution.isValidBST1(root))