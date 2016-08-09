from Tree_zzh import tree


class Solution(object):

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack, res = [(root, False)], []
        while stack:
            node, visited = stack.pop()
            if node is not None:
                if visited:
                    res.append(node.val)
                else:
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        return res

    def postorderTraversal2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack, res = [root], []
        while stack:
            node = stack.pop()
            if node is not None:
                res.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return res[::-1]

root = tree.get_one()
solution = Solution()
print(solution.postorderTraversal(root))
print(solution.postorderTraversal2(root))