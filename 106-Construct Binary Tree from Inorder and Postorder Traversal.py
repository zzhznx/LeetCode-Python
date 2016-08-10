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
        parents = []
        working = None
        i, post = 0, 0
        while post < len(postorder):
            if len(parents) > 0 and postorder[post] == parents[-1].val:
                parents[-1].right = working
                working = parents[-1]
                parents.pop()
                post += 1
            else:
                newNode = tree.TreeNode(inorder[i])
                newNode.left = working
                working = None
                parents.append(newNode)
                i += 1
        return working


solution = Solution()
newRoot = solution.buildTree2([4, 2, 7, 5, 8, 1, 3, 6], [4, 7, 8, 5, 2, 6, 3, 1])
tree.pretty_print(newRoot)