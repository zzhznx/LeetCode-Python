from Tree_zzh import tree
import queue


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        q = queue.Queue()
        q.put(root)
        res = []
        while not q.empty():
            n = q.qsize()
            node = None
            for i in range(n):
                node = q.get()
                if node.left is not None:
                    q.put(node.left)
                if node.right is not None:
                    q.put(node.right)
            res.append(node.val)
        return res

root = tree.get_one()
solution = Solution()
print(solution.rightSideView(root))
