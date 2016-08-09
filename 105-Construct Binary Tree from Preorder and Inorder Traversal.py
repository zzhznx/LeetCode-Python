from Tree_zzh import tree


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            index = inorder.index(preorder.pop(0))
            root = tree.TreeNode(inorder[index])
            root.left = self.buildTree(preorder, inorder[0:index])
            root.right = self.buildTree(preorder, inorder[index + 1:])
            return root

    def buildTree2(self, preorder, inorder):
        if len(preorder) == 0:
            return None

        stack, stackTree = [], []
        f, i, j = 0, 0, 0
        stack.append(preorder[0])
        root = tree.TreeNode(preorder[0])
        stackTree.append(root)
        t = root
        i += 1

        while i < len(preorder):
            if stackTree and stackTree[-1].val == inorder[j]:
                t = stackTree.pop()
                stack.pop()
                f = 1
                j += 1
            else:
                if not f:
                    stack.append(preorder[i])
                    t.left = tree.TreeNode(preorder[i])
                    t = t.left
                    stackTree.append(t)
                    i += 1
                if f:
                    f = 0
                    stack.append(preorder[i])
                    t.right = tree.TreeNode(preorder[i])
                    t = t.right
                    stackTree.append(t)
                    i += 1
            print(stack)
        return root


solution = Solution()
newRoot = solution.buildTree2([1, 2, 4, 5, 7, 8, 3, 6], [4, 2, 7, 5, 8, 1, 3, 6])
tree.pretty_print(newRoot)