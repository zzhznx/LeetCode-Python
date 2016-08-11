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


root = tree.get_one()
solution = Solution()
print(solution.binaryTreePaths(root))