# author luke
# 2022年02月25日

import random


class MySort:
    def __init__(self, arr_len):
        self.arr = []  # 列表
        self.arr_len = arr_len  # 列表长度

    def random_int(self):
        for i in range(self.arr_len):
            self.arr.append(random.randint(0, 99))

    def bubble(self):
        arr = self.arr
        i = self.arr_len - 1

        while i > 0:  # 外层循环控制的无序数的数目
            j = 0
            flag = 1
            while j < i:
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    flag = 0
                j += 1
            if flag:  # 如果某一趟没有交换过，就代表已经有序
                break
            i -= 1

    def test_sort(self, sort_method,*args,**kwargs):
        print(self.arr)
        sort_method(*args,**kwargs)
        print(self.arr)

    def select(self):
        arr = self.arr
        for i in range(self.arr_len - 1):
            min_pos = i
            for j in range(i + 1, self.arr_len):
                if arr[j] < arr[min_pos]:
                    min_pos = j
            arr[i], arr[min_pos] = arr[min_pos], arr[i]

    def insert(self):
        arr = self.arr
        i = 1
        while i < self.arr_len:  # 外层控制要插入的数
            insert_val = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > insert_val:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = insert_val
            i += 1

    def shell(self):
        arr = self.arr
        gap = self.arr_len >> 1
        while gap > 0:
            i = gap
            while i < self.arr_len:  # 外层控制要插入的数
                insert_val = arr[i]
                j = i - gap
                while j >= 0 and arr[j] > insert_val:
                    arr[j + gap] = arr[j]
                    j -= gap
                arr[j + gap] = insert_val
                i += 1
            gap >>= 1

    def partition(self, left, right):
        arr = self.arr
        k = left
        i = left
        while i<right:
            if arr[i]<arr[right]:# k始终指向要存放比分割值小的下标
                arr[i],arr[k]=arr[k],arr[i]
                k+=1
            i+=1
        arr[k],arr[right]=arr[right],arr[k]
        return k

    def quick(self,left,right):
        if left <right:
            pivot=self.partition(left,right)
            self.quick(left,pivot-1)  #排左边一半
            self.quick(pivot+1,right)  #排右边一半

if __name__ == '__main__':
    temp = MySort(10)
    temp.random_int()
    temp.test_sort(temp.quick,0,temp.arr_len-1)  # 方法也可以传递
