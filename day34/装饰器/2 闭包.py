

def line6(k, b):
    def create_line(x):
    
        print(k * x + b)

    return create_line


l1 = line6(2, 3)  # l1是create_line函数，函数中k的值是1，b的值是2
l1(3)

l2 = line6(5, 6)
l2(3)
