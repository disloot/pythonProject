# author luke
# 2022年02月25日

class Stack:
    def __init__(self):
        self.stack = []  #使用列表实现

    def push(self, ele):
        self.stack.append(ele)

    def pop(self):
        return self.stack.pop()

    def top(self):
        if self.empty():
            return "stack is empty"
        return self.stack[-1]  #获取列表末尾元素，就是栈顶元素

    def empty(self):
        return self.stack == []

    def size(self):
        return len(self.stack)


if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.stack)
    print(stack.pop())
    stack.pop()
    print(stack.size())
    print(stack.stack)