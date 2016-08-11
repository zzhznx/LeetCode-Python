from Tree_zzh import tree
import queue

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        self.dfs(root, 0)
        return self.res

    def dfs(self, root, val):
        if root:
            self.dfs(root.left, val * 10 + root.val)
            self.dfs(root.right, val * 10 + root.val)
            if root.left is None and root.right is None:
                self.res += val * 10 + root.val

    # dfs + stack
    def sumNumbers2(self, root):
        if not root:
            return 0
        stack, res = [(root, root.val)], 0
        while stack:
            node, value = stack.pop()
            if node:
                if not node.left and not node.right:
                    res += value
                if node.right:
                    stack.append((node.right, value * 10 + node.right.val))
                if node.left:
                    stack.append((node.left, value * 10 + node.left.val))
        return res

    # bfs + queue
    def sumNumbers3(self, root):
        if not root:
            return 0
        q, res = queue.Queue(), 0
        q.put((root, root.val))
        while not q.empty():
            node, value = q.get()
            if node:
                if not node.left and not node.right:
                    res += value
                if node.left:
                    q.put((node.left, value * 10 + node.left.val))
                if node.right:
                    q.put((node.right, value * 10 + node.right.val))
        return res

root = tree.get_one()
solution = Solution()
print(solution.sumNumbers(root))
print(solution.sumNumbers2(root))
print(solution.sumNumbers3(root))