from Tree_zzh import tree
import queue

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        if not root:
            return []
        res = []
        self.dfs(root, "", res)
        return res

    def dfs(self, root, ls, res):
        if root:
            self.dfs(root.left, ls + str(root.val) + "->", res)
            self.dfs(root.right, ls + str(root.val) + "->", res)
            if root.left is None and root.right is None:
                res.append(ls + str(root.val))

    # dfs + stack
    def binaryTreePaths2(self, root):
        if not root:
            return []
        stack, res = [(root, str(root.val))], []
        while stack:
            node, ls = stack.pop()
            if node:
                if not node.left and not node.right:
                    res.append(ls)
                if node.right:
                    stack.append((node.right, ls + "->" + str(node.right.val)))
                if node.left:
                    stack.append((node.left, ls + "->" + str(node.left.val)))
        return res

    # bfs + queue
    def binaryTreePaths3(self, root):
        if not root:
            return []
        q, res = queue.Queue(), []
        q.put((root, str(root.val)))
        while not q.empty():
            node, ls = q.get()
            if node:
                if not node.left and not node.right:
                    res.append(ls)
                if node.left:
                    q.put((node.left, ls + "->" + str(node.left.val)))
                if node.right:
                    q.put((node.right, ls + "->" + str(node.right.val)))
        return res

root = tree.get_one()
solution = Solution()
print(solution.binaryTreePaths(root))
print(solution.binaryTreePaths2(root))
print(solution.binaryTreePaths3(root))