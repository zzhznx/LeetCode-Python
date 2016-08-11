import queue
from io import StringIO

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


def level_print(root):
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


class Queue(object):
    def __init__(self):
        self.queue = []

    def enqueue(self, b):
        self.queue.insert(0, b)

    def dequeue(self):
        return self.queue.pop()

    def isEmpty(self):
        return self.queue == []


def add_padding(str, pad_length_value):
    str = str.strip()
    return str.center(pad_length_value, ' ')


def pretty_print(root):
    output = StringIO()
    pretty_output = StringIO()
    current_level = Queue()
    next_level = Queue()
    current_level.enqueue(root)
    depth = 0

    # get the depth of current tree
    # get the tree node data and store in list
    if root:
        while not current_level.isEmpty():
            current_node = current_level.dequeue()
            output.write('%s ' % current_node.val if current_node else 'N ')
            next_level.enqueue(current_node.left if current_node else current_node)
            next_level.enqueue(current_node.right if current_node else current_node)
            if current_level.isEmpty():
                if sum([i is not None for i in next_level.queue]):  # if next level has node
                    current_level, next_level = next_level, current_level
                    depth += 1
                output.write('\n')
    print('the tree print level by level is :')
    print(output.getvalue())
    print("current tree's depth is %i" % (depth + 1))

    # add space to each node
    output.seek(0)
    pad_length = 3
    keys = []
    spaces = 2 ** depth
    while spaces > 0:
        skip_start = spaces * pad_length
        skip_mid = (2 * spaces - 1) * pad_length
        key_start_spacing = ' ' * skip_start
        key_mid_spacing = ' ' * skip_mid
        keys = output.readline().split(' ')  # read one level to parse
        padded_keys = (add_padding(key, pad_length) for key in keys)
        padded_str = key_mid_spacing.join(padded_keys)
        complete_str = ''.join([key_start_spacing, padded_str])
        pretty_output.write(complete_str)

        # add space and slashes to middle layer
        slashes_depth = spaces
        print('current slashes depth im_resize:')
        print(spaces)
        print("current levle's list is:")
        print(keys)

        spaces //= 2
        if spaces > 0:
            pretty_output.write('\n')  # print '\n' each level

            cnt = 0
            while cnt < slashes_depth:
                inter_symbol_spacing = ' ' * (pad_length + 2 * cnt)
                symbol = ''.join(['/', inter_symbol_spacing, '\\'])
                symbol_start_spacing = ' ' * (skip_start - cnt - 1)
                symbol_mid_spacing = ' ' * (skip_mid - 2 * (cnt + 1))
                pretty_output.write(''.join([symbol_start_spacing, symbol]))
                for i in keys[1:-1]:
                    pretty_output.write(''.join([symbol_mid_spacing, symbol]))
                pretty_output.write('\n')
                cnt += 1
    print(pretty_output.getvalue())


root = get_one()
pretty_print(root)