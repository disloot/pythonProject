

MAXKEY=1000

def elf_hash(hash_str):
    h = 0
    g = 0
    for i in hash_str:
        h = (h << 4) + ord(i)
        g = h & 0xf0000000
        if g:
            h ^= g >> 24
        h &= ~g
    return h % MAXKEY

def use_hash():
    str_list=["xiongda","lele","hanmeimei","wangdao","fenghua"]  #要存到哈希表的数据
    hash_table=[None]*MAXKEY  #哈希表初始化
    for i in str_list:
        if hash_table[elf_hash(i)]:
            print('哈希冲突')
        else:
            hash_table[elf_hash(i)]=i
    pass

if __name__ == '__main__':
    use_hash()
    pass
    print(hash('xiongda'))
    print(hash('xiongda'))
