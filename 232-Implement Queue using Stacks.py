class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.inStack = []
        self.outStack = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.inStack.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        self.peek()
        self.outStack.pop()

    def peek(self):
        """
        :rtype: int
        """
        if len(self.outStack) == 0:
            for _ in range(len(self.inStack)):
                self.outStack.append(self.inStack.pop())
        return self.outStack[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not (len(self.inStack) or len(self.outStack))