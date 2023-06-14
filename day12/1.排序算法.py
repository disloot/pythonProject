
import random


class MySort:
    def __init__(self, arr_len):
        # self.arr = [3, 87, 2, 93, 78, 56, 61, 38, 12, 40]  # 列表
        self.arr = []
        self.arr_len = arr_len  # 列表长度
        self.temp_arr = [0] * self.arr_len

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

    def test_sort(self, sort_method, *args, **kwargs):
        print(self.arr)
        sort_method(*args, **kwargs)
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
        while i < right:
            if arr[i] < arr[right]:  # k始终指向要存放比分割值小的下标
                arr[i], arr[k] = arr[k], arr[i]
                k += 1
            i += 1
        arr[k], arr[right] = arr[right], arr[k]
        return k

    def quick(self, left, right):
        if left < right:
            pivot = self.partition(left, right)
            self.quick(left, pivot - 1)  # 排左边一半
            self.quick(pivot + 1, right)  # 排右边一半

    def ajust_max_heap(self, dad, arr_len):
        """
        将某颗子树调整为大根堆
        :param dad:
        :param arr_len:
        :return:
        """
        arr = self.arr
        son = 2 * dad + 1  # 找到左孩子位置
        while son < arr_len:
            # 拿左孩子和右孩子进行比较
            if son + 1 < arr_len and arr[son] < arr[son + 1]:
                son += 1
            if arr[son] > arr[dad]:  # 一旦发生交换，孩子变为父亲继续调整
                arr[son], arr[dad] = arr[dad], arr[son]
                dad = son
                son = 2 * dad + 1
            else:
                break

    def heap(self):
        arr = self.arr
        for i in range(self.arr_len // 2 - 1, -1, -1):
            self.ajust_max_heap(i, self.arr_len)
        # 交换根部元素和数组最后一个元素
        arr[0], arr[self.arr_len - 1] = arr[self.arr_len - 1], arr[0]
        for i in range(self.arr_len - 1, 1, -1):
            self.ajust_max_heap(0, i)
            arr[0], arr[i - 1] = arr[i - 1], arr[0]

    def merge(self, low, mid, high):
        temp_arr = self.temp_arr
        arr = self.arr
        temp_arr[low:high + 1] = arr[low:high + 1]
        i = low
        j = mid + 1
        k = low
        while i <= mid and j <= high:
            if temp_arr[i] < temp_arr[j]:
                arr[k] = temp_arr[i]
                k += 1
                i += 1
            else:
                arr[k] = temp_arr[j]
                k += 1
                j += 1
        # 某一个剩余的比较多
        while i <= mid:
            arr[k] = temp_arr[i]
            k += 1
            i += 1

        while j <= high:
            arr[k] = temp_arr[j]
            k += 1
            j += 1

    def merge_sort(self, low, high):
        if low < high:
            mid = (low + high) // 2
            self.merge_sort(low, mid)
            self.merge_sort(mid + 1, high)
            self.merge(low, mid, high)  # 合并两个有序数组





if __name__ == '__main__':
    temp = MySort(10)
    temp.random_int()
    temp.test_sort(temp.merge_sort, 0, temp.arr_len - 1)  # 方法也可以传递
