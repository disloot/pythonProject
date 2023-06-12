#!usr/bin/python3
# author lyle

class MySort:
    def __init__(self, arr_list):
        self.__arr_list = arr_list
        self.__arr_length = len(self.__arr_list)

    def insert_sort(self):
        arr = self.__arr_list
        length = len(arr)
        for i in range(1, length, 1):
            insert_val = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > insert_val:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = insert_val

    def bubble_sort(self):
        arr = self.__arr_list
        flag = True
        for i in range(self.__arr_length - 1):
            for j in range(self.__arr_length - 1, i, -1):
                if arr[j] < arr[j - 1]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
                    flag = False
            if flag:
                break

    def select_sort(self):
        arr = self.__arr_list
        for i in range(self.__arr_length - 1):
            min_pos = i
            for j in range(i + 1, self.__arr_length):
                if arr[j] < arr[min_pos]:
                    min_pos = j
            arr[i], arr[min_pos] = arr[min_pos], arr[i]

    def partition(self, low, high):
        arr = self.__arr_list
        key = arr[low]
        low = low
        high = high
        while low < high:
            while low < high and arr[high] >= key:
                high -= 1
            arr[low] = arr[high]
            while low < high and arr[low] <= key:
                low += 1
            arr[high] = arr[low]
        arr[low] = key
        return low

    def quick_sort_r(self, low, high):
        if low < high:
            mid = self.partition(low, high)
            self.quick_sort(low, mid - 1)
            self.quick_sort(mid + 1, high)

    def quick_sort(self,low, high):
        stack = []
        while  len(stack):
            arr = self.__arr_list
            key = arr[i]
            i = low
            j = high
            while i < j:
                while i < j and arr[j] >= key:
                    j -= 1
                arr[i] = arr[j]
                while i < j and arr[i] <= key:
                    i += 1
                arr[j] = arr[i]
            arr[i] = key

    def ajust_maxheap(self, dad, length):
        arr = self.__arr_list
        son = dad * 2 + 1
        while son < length:
            if son + 1 < length and arr[son] < arr[son + 1]:
                son += 1
            if arr[son] > arr[dad]:
                arr[son], arr[dad] = arr[dad], arr[son]
                dad = son
                son = dad * 2 + 1
            else:
                break

    def heap_sort(self):
        arr = self.__arr_list
        for i in range(self.__arr_length // 2 - 1, -1, -1):
            self.ajust_maxheap(i, self.__arr_length)
        for i in range(self.__arr_length - 1, 1, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self.ajust_maxheap(0, i)

    def merge(self, low, high):
        temp_arr = [0] * self.__arr_length
        arr = self.__arr_list
        temp_arr[low:high] = arr[low:high]
        mid = (low + high) // 2
        i = low
        j = mid + 1
        k = low
        while i <= mid and j <= high:
            if temp_arr[i] <= temp_arr[j]:
                arr[k] = temp_arr[i]
                k += 1
                i += 1
            else:
                arr[k] = temp_arr[j]
                k += 1
                j += 1
        if i <= mid:
            arr[k:high] = temp_arr[i:mid]
        if j <= high:
            arr[k:high] = temp_arr[j:high]

    def merge_sort(self, low, high):
        if low < high:
            mid = (low + high) // 2
            self.merge_sort(low, mid)
            self.merge_sort(mid + 1, high)
            self.quick_sort(low, high)


if __name__ == '__main__':
    list1 = [3, 1, 6, 43, 86, 44, 5, 8, 0, -3]
    MySort(list1).merge_sort(0, 9)
    print(list1)
