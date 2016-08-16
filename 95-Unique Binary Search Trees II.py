"""
I start by noting that 1..n is the in-order traversal for any BST with nodes 1 to n. So if I pick i-th node as my root,
the left subtree will contain elements 1 to (i-1), and the right subtree will contain elements (i+1) to n.
I use recursive calls to get back all possible trees for left and right subtrees
and combine them in all possible ways with the root.
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 1:
            return []
        return self.genTrees(1, n)

    def genTrees(self, start, end):
        treeList = []

        if start > end:
            treeList.append(None)
            return treeList

        if start == end:
            treeList.append(TreeNode(start))
            return treeList

        for i in range(start, end + 1):
            left = self.genTrees(start, i - 1)
            right = self.genTrees(i + 1, end)

            for lNode in left:
                for rNode in right:
                    root = TreeNode(i)
                    root.left = lNode
                    root.right = rNode
                    treeList.append(root)
        return treeList

solution = Solution()
print(solution.generateTrees(1))