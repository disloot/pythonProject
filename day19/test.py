#!/usr/bin/python
#author: Lyle
#time：2023/06/09 16:11

def test(args, kwargs=None, others=None):
    print(*args)
    

if __name__ == '__main__':
    # test(1,2,3,4)
    test((1,2,3,4),others = {})