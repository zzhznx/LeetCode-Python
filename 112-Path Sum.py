# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if root.left is None and root.right is None and root.val == sum:
            return True
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

    def hasPathSum2(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        stack, sumStack = [root], [sum]
        while stack:
            node = stack.pop()
            num = sumStack.pop()
            if node.left is None and node.right is None and node.val == num:
                return True
            if node.right is not None:
                stack.append(node.right)
                sumStack.append(num - node.val)
            if node.left is not None:
                stack.append(node.left)
                sumStack.append(num - node.val)
        return False