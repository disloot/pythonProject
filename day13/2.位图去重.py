
class BitMap:
    def __init__(self):
        self.bitmap = 0
        self.arr = [9, 20, 17, 16, 3, 4, 8, 2, 7, 9, 4, 3]
        self.newarr = []

    def duplicate_remove(self):
        for i in self.arr:
            if self.bitmap & 1 << i:
                pass
            else:
                self.newarr.append(i)
                self.bitmap |= 1 << i

if __name__ == '__main__':
    b=BitMap()
    b.duplicate_remove()
    print(b.newarr)