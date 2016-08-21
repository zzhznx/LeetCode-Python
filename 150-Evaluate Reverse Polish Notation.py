class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for t in tokens:
            if t in ("+", "-", "*", "/"):
                r, l = stack.pop(), stack.pop()
                if t == "+":
                    stack.append(l + r)
                elif t == "-":
                    stack.append(l - r)
                elif t == "*":
                    stack.append(l * r)
                else:
                    # here take care of the case like "1/-22",
                    # in Python 2.x, it returns -1, while in
                    # Leetcode it should return 0
                    if l * r < 0 and l % r != 0:
                        stack.append(l / r + 1)
                    else:
                        stack.append(l / r)
            else:
                stack.append(int(t))
        return stack[0]