class MinStack:
    def __init__(self):
        self.q = []

    # @param x, an integer
    # @return an integer
    def push(self, x):
        curMin = self.getMin()
        if curMin is None or x < curMin:
            curMin = x
        self.q.append((x, curMin))

    # @return nothing
    def pop(self):
        self.q.pop()

    # @return an integer
    def top(self):
        if len(self.q) == 0:
            return None
        return self.q[len(self.q) - 1][0]

    # @return an integer
    def getMin(self):
        if len(self.q) == 0:
            return None
        else:
            return self.q[len(self.q) - 1][1]

class MinStack2:
    def __init__(self):
        self.q = []
        self.minVal = 0

    # @param x, an integer
    # @return an integer
    def push(self, x):
        if len(self.q) == 0:
            self.q.append(0)
            self.minVal = x
        else:
            self.q.append(x - self.minVal)
            if x < self.minVal:
                self.minVal = x

    # @return nothing
    def pop(self):
        if len(self.q) == 0:
            return
        temp = self.q.pop()
        if temp < 0:
            self.minVal -= temp

    # @return an integer
    def top(self):
        if len(self.q) == 0:
            return None
        temp = self.q[len(self.q) - 1]
        if temp > 0:
            return self.minVal + temp
        else:
            return self.minVal

    # @return an integer
    def getMin(self):
        return self.minVal
