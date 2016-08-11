from Tree_zzh import tree
import queue


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        return left + right + 1 if left == 0 or right == 0 else min(left, right) + 1

    def minDepth2(self, root):
        if not root:
            return 0
        minDep = 1
        q = queue.Queue()
        q.put(root)
        while not q.empty():
            n = q.qsize()
            for i in range(n):
                node = q.get()
                if not node.left and not node.right:
                    return minDep
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            minDep += 1
        return minDep


root = tree.get_one()
solution = Solution()
print(solution.minDepth(root))
print(solution.minDepth2(root))