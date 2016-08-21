class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        stack = []
        index = -1
        preorder = preorder.split(",")
        for s in preorder:
            stack.append(s)
            index += 1
            while self.endsWithTwoPoundSign(stack, index):
                stack.pop()
                index -= 1
                stack.pop()
                index -= 1
                if index < 0:
                    return False
                stack.pop()
                stack.append("#")
        if len(stack) == 1 and stack[0] == "#":
            return True
        return False


    def endsWithTwoPoundSign(self, stack, index):
        if index < 1:
            return False
        if stack[index] == "#" and stack[index - 1] == "#":
            return True
        return False

    """
    Some used stack. Some used the depth of a stack. Here I use a different perspective. In a binary tree, if we consider null as leaves, then

    all non-null node provides 2 outdegree and 1 indegree (2 children and 1 parent), except root
    all null node provides 0 outdegree and 1 indegree (0 child and 1 parent).
    Suppose we try to build this tree. During building, we record the difference between out degree and in degree diff = outdegree - indegree.
    When the next node comes, we then decrease diff by 1, because the node provides an in degree. If the node is not null, we increase diff by 2, because it provides two out degrees.
    If a serialization is correct, diff should never be negative and diff will be zero when finished
    """
    def isValidSerialization2(self, preorder):
        nodes = preorder.split(",")
        diff = -1
        for node in nodes:
            diff -= 1
            if diff < 0:
                return False
            if node == "#":
                diff += 2
        return diff == 0




solution = Solution()
print(solution.isValidSerialization("9,#,#,1"))