import queue

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def Link(parent, leftVal, rightVal):
    if leftVal is not None:
        nodeList[parent].left = nodeList[leftVal]
    if rightVal is not None:
        nodeList[parent].right = nodeList[rightVal]


nodeList = []

def get_one():
    for i in range(9):
        nodeList.append(TreeNode(i))
    Link(1, 2, 3)
    Link(2, 4, 5)
    Link(3, None, 6)
    Link(5, 7, 8)
    return nodeList[1]


def pretty_print(root):
    if root is None:
        return []
    q = queue.Queue()
    q.put(root)
    res = []
    while not q.empty():
        n = q.qsize()
        temp = []
        for i in range(n):
            node = q.get()
            temp.append(node.val)
            if node.left is not None:
                q.put(node.left)
            if node.right is not None:
                q.put(node.right)
        res.append(temp)
    print(res)