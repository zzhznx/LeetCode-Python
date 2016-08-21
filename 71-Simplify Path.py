class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        oper = path.strip("\/").split("/")
        print(oper)
        for o in oper:
            if o == "..":
                if len(stack):
                    stack.pop()
            elif o in (".", "/", ""):
                continue
            else:
                stack.append(o)
        return "/" + "/".join(stack)

solution = Solution()
print(solution.simplifyPath("/home//foo/"))