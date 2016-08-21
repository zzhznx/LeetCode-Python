def deserialize(self, s):
    def nestedInteger():
        num = ''
        while s[-1] in '1234567890-':
            num += s.pop()
        if num:
            return NestedInteger(int(num))
        s.pop()
        lst = NestedInteger()
        while s[-1] != ']':
            lst.add(nestedInteger())
            if s[-1] == ',':
                s.pop()
        s.pop()
        return lst
    s = list(' ' + s[::-1])
    return nestedInteger()

def deserialize2(self, s):
    def nestedInteger(x):
        if isinstance(x, int):
            return NestedInteger(x)
        lst = NestedInteger()
        for y in x:
            lst.add(nestedInteger(y))
        return lst
    return nestedInteger(eval(s))