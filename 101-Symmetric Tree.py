from Tree_zzh import tree


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return root is None or self.isSymmetricHelp(root.left, root.right)

    def isSymmetricHelp(self, left, right):
        if left is None or right is None:
            return left == right
        if left.val != right.val:
            return False
        return self.isSymmetricHelp(left.left, right.right) and self.isSymmetricHelp(left.right, right.left)

    def isSymmetric2(self, root):
        if root is None:
            return True
        stack = []
        if root.left is not None:
            if root.right is None:
                return False
            stack.append(root.left)
            stack.append(root.right)
        elif root.right is not None:
            return False

        while stack:
            if len(stack) % 2 != 0:
                return False
            right = stack.pop()
            left = stack.pop()

            if right.val != left.val:
                return False

            if left.left is not None:
                if right.right is None:
                    return False
                stack.append(left.left)
                stack.append(right.right)
            elif right.right is not None:
                return False

            if left.right is not None:
                if right.left is None:
                    return False
                stack.append(left.right)
                stack.append(right.left)
            elif right.left is not None:
                return False

        return True