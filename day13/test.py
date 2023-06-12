#!usr/bin/python3
# author lyle
from operator import itemgetter
from re import sub

punctuation = '!,.;:?'


def remove_punctuation(text):
    text = sub('[{}]+'.format(punctuation), '', text)
    return text


class Hash_str(object):

    def __init__(self, length):
        self.hash_len = length
        self.hash_map = [None] * length

    def hash_elf_algorithm(self, string):
        h = 0

        g = 0
        for i in string:
            h = (h << 4) + ord(i)  # ASCII
            g = h & 0xf00000000
        if g:
            h ^= g >> 24
        h &= ~g
        return h % self.hash_len  # 取余使得其落在 len 范围


def use_hash():
    hash1 = Hash_str(1000)
    f = open('Bible.txt')
    text = f.read()
    text = remove_punctuation(text)
    for i in text.replace('\n', ' ').split(' '):
        if i != '':
            k = hash1.hash_elf_algorithm(i)
            if hash1.hash_map[k] is None:
                hash1.hash_map[k] = {i: 1}
            elif i not in hash1.hash_map[k].keys():
                hash1.hash_map[k].update({i: 1})
            else:
                hash1.hash_map[k][i] += 1
    f.close()
    dict1 = {}
    for i in hash1.hash_map:
        if i is not None:
            dict1.update(i)
    dict2 = sorted(dict1.items(), key=itemgetter(1), reverse=True)
    for i in range(100):
        print(dict2[i], end=' ')


def use_bitmap(arr):
    m = 0
    new_arr = []
    for i in arr:
        if m & 1 << i:
            pass
        else:
            m |= 1 << i
            new_arr.append(i)
    return new_arr


class DTNode:
    def __init__(self, val=None, count=0):
        self.value = val
        self.count = count
        self.flag = [False,0]
        self.child = {}


class DirTree:
    def __init__(self):
        self.__root = DTNode()

    def insert(self, string):
        cur = self.__root
        for i in string:
            if i not in cur.child:
                cur.child[i] = DTNode(i, 1)
                cur = cur.child[i]
            else:
                cur.child[i].count += 1
                cur = cur.child[i]
        cur.flag[0] = True
        cur.flag[1] += 1

    def search(self, string):
        cur = self.__root
        flag = True
        for i in string:
            if i in cur.child:
                cur = cur.child[i]
            else:
                flag = False
                break
        if not cur.flag[0]:
            flag = False
        return flag

    def delete(self, string):
        cur = self.__root
        flag = False
        if self.search(string):
            flag = True
            for i in string:
                cur.child[i].count -= 1
                if cur.child[i].count == 0:
                    cur.child.pop(i)
                    break
                else:
                    cur = cur.child[i]
            cur.flag[1] -= 1
            if not cur.flag[1]:
                cur.flag[0] = False
        return flag


if __name__ == '__main__':
    a = DirTree()
    a.insert('string')
    a.insert('haven')
    a.insert('str')
    a.insert('string1')
    a.insert('unto')

    print(a.search('str'))
    print(a.search('strin'))
    print(a.search('string1'))
    a.delete('str')
    print(a.search('str'))
