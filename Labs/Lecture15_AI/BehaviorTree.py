
level = 0
def indent():
    global level
    level += 1

def unindent():
    global level
    level -= 1

def print_indent():
    for i in range(level):
        print("    ", end='')


class BehaviorTree:
    FAIL, RUNNING, SUCCESS = -1, 0, 1

    def __init__(self, root_node):
        self.root = root_node

    def run(self):
        self.root.run()

    def print(self):
        self.root.print()


class Node:
    def add_child(self, child):
        self.children.append(child)
    def add_children(self, *children):
        for child in children:
            self.children.append(child)


<<<<<<< HEAD
class SelectorNode(Node): # 아래중 하나만 SUCCESS여도 가능
    def __init__(self, name):
        self.children = []
=======
class Selector(Node):
    def __init__(self, name, *nodes):
        self.children = list(nodes)
>>>>>>> c0296a243c1f50f168834b49f662a7f8cb8c036f
        self.name = name
        self.prev_running_pos = 0 # 앞선 실행에서, RUNNING으로 리턴한 자식 노드 위치를 저장

    def reset(self):
        self.prev_running_pos = 0
        for node in self.children:
            node.reset()


    def run(self):
        for pos in range(0, len(self.children)):
            result = self.children[pos].run()
            if BehaviorTree.RUNNING == result:
                self.prev_running_pos = pos
                return BehaviorTree.RUNNING
            elif BehaviorTree.SUCCESS == result:
                self.prev_running_pos = 0
                # now success, so right nodes (less import nodes) should be reset
                for node in self.children[pos+1:]:
                    node.reset()
                return BehaviorTree.SUCCESS
        self.prev_running_pos = 0
        return BehaviorTree.FAIL

    def print(self):
        print_indent()
        print("SELECTOR NODE: " + self.name)
        indent()
        for child in self.children:
            child.print()
        unindent()

<<<<<<< HEAD
class SequenceNode(Node): # 아래 있는 게 모두 SUCCESS여야 가능
    def __init__(self, name):
        self.children = []
=======
class Sequence(Node):
    def __init__(self, name, *nodes):
        self.children = list(nodes)
>>>>>>> c0296a243c1f50f168834b49f662a7f8cb8c036f
        self.name = name
        self.prev_running_pos = 0

    def reset(self):
        self.prev_running_pos = 0
        for node in self.children:
            node.reset()


    def run(self):
        for pos in range(self.prev_running_pos, len(self.children)):
            result = self.children[pos].run()
            if BehaviorTree.RUNNING == result:
                self.prev_running_pos = pos
                return BehaviorTree.RUNNING
            elif BehaviorTree.FAIL == result:
                self.prev_running_pos = 0
                return BehaviorTree.FAIL
        self.prev_running_pos = 0
        return BehaviorTree.SUCCESS

    def print(self):
        print_indent()
        print("SEQUENCE NODE: " + self.name)
        indent()
        for child in self.children:
            child.print()
        unindent()


class Leaf(Node):
    def __init__(self, name, func):
        self.name = name
        self.func = func

    def reset(self):
        pass

    def add_child(self, child):
        print("ERROR: you cannot add child node to leaf node")

    def add_children(self, *children):
        print("ERROR: you cannot add children node to leaf node")

    def run(self):
        return self.func()

    def print(self):
        print_indent()
        print("LEAF NODE: " + self.name)



