from Tree_zzh import tree


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            index = inorder.index(postorder.pop())
            root = tree.TreeNode(inorder[index])
            root.right = self.buildTree(inorder[index+1:], postorder)
            root.left = self.buildTree(inorder[0:index], postorder)
            return root

    def buildTree2(self, inorder, postorder):


solution = Solution()
newRoot = solution.buildTree([4, 2, 7, 5, 8, 1, 3, 6], [4, 7, 8, 5, 2, 6, 3, 1])
tree.pretty_print(newRoot)