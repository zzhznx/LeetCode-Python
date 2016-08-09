from Tree_zzh import tree
import queue


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        q = queue.Queue()
        q.put(root)
        res = []
        flag = True
        while not q.empty():
            n = q.qsize()
            temp = []
            for i in range(n):
                node = q.get()
                temp.append(node.val)
                if node.left is not None:
                    q.put(node.left)
                if node.right is not None:
                    q.put(node.right)
            if flag:
                res.append(temp)
                flag = not flag
            else:
                res.append(temp[::-1])
                flag = not flag
        return res


root = tree.get_one()
solution = Solution()
print(solution.zigzagLevelOrder(root))