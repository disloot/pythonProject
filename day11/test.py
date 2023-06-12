from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque([])

    def enqueue(self, elem):
        self.queue.append(elem)

    def dequeue(self):
        return self.queue.popleft()


class CirQueue:
    def __init__(self, size):
        self.__queue = list('0' * (size + 1))
        self.__size = size + 1
        self.__front = 0
        self.__rear = 0

    def isempty(self):
        return self.__front == self.__rear

    def enqueue(self, elem):
        if self.__front == (self.__rear + 1) % self.__size:
            print('队列已满')
        else:
            self.__queue[self.__rear] = elem
            self.__rear = (self.__rear + 1) % self.__size

    def dequeue(self):
        if self.isempty():
            print('队列为空')
        else:
            elem = self.__queue[(self.__front)]
            self.__front = (self.__front + 1) % self.__size
            return elem

    def __str__(self):
        return str(self.__queue)


class Node:
    def __init__(self, elem):
        self.elem = elem
        self.lchild = None
        self.rchild = None

    def __str__(self):
        return str(self.elem)


class BiTree:
    def __init__(self):
        self.root = None

    def que_build(self, elem_list: list):
        queue = []
        for i in elem_list:
            new_node = Node(i)
            queue.append(new_node)
            if self.root is None:
                self.root = new_node
            else:
                if queue[0].lchild is None:
                    queue[0].lchild = new_node
                elif queue[0].rchild is None:
                    queue[0].rchild = new_node
                    queue.pop(0)

    def bst_build(self, new_node: Node, root: Node):

        if self.root is None:
            self.root = new_node
        else:
            if new_node.elem < root.elem:
                if root.lchild is None:
                    root.lchild = new_node
                else:
                    self.bst_build(new_node, root.lchild)
            else:
                if root.rchild is None:
                    root.rchild = new_node
                else:
                    self.bst_build(new_node, root.rchild)

    def bst(self, elem_list: list):
        for i in elem_list:
            node = Node(i)
            self.bst_build(node, self.root)

    def mid_order(self, root: Node):
        if root:
            self.mid_order(root.lchild)
            print(root, end=' ')
            self.mid_order(root.rchild)


if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    list2 = [3, 1, 4, 2, 4, 6, 8, 5, 7]
    tree1 = BiTree()
    tree2 = BiTree()
    tree1.que_build(list1)
    tree2.bst(list2)
    tree1.mid_order(tree1.root)
    print()
    tree2.mid_order(tree2.root)
    pass
