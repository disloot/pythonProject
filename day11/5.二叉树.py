# author luke
# 2022年02月25日


class Node(object):
    """节点类"""

    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

class Tree:
    def __init__(self):
        self.root=None
        self.queue=[]
    def insert_node(self,elem):
        new_node=Node(elem)  #对新结点进行初始化
        self.queue.append(new_node)  #放入队列
        if self.root is None:
            self.root=new_node  #树为空，new_node就是树根
        else:
            if self.queue[0].lchild is None:  #判断左孩子是否为空
                self.queue[0].lchild=new_node
            elif self.queue[0].rchild is None:  #判断右孩子是否为空
                self.queue[0].rchild = new_node
                self.queue.pop(0)  #出队

    def preorder(self,current_node:Node):
        if current_node:
            print(current_node.elem,end=' ')
            self.preorder(current_node.lchild)
            self.preorder(current_node.rchild)

    def midorder(self,current_node:Node):
        if current_node:
            self.midorder(current_node.lchild)
            print(current_node.elem, end=' ')
            self.midorder(current_node.rchild)

    def lastorder(self, current_node: Node):
        if current_node:
            self.lastorder(current_node.lchild)
            self.lastorder(current_node.rchild)
            print(current_node.elem, end=' ')

if __name__ == '__main__':
    tree=Tree()
    for i in range(1,11):
        tree.insert_node(i)
    tree.preorder(tree.root)
    print()
    tree.midorder(tree.root)
    print()
    tree.lastorder(tree.root)
    print()
