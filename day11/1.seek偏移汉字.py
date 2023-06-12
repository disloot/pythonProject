# author luke
# 2022年02月25日

def use_seek():
    file = open('file', mode='r+', encoding='utf8')
    file.seek(3)  # 如果存在汉字，偏移要是3个字节
    text = file.read()
    print(text)
    file.close()


# 写字节流到文件
def write_binary():
    file = open('file', mode='rb+')
    btext = file.read()
    print(btext)
    file.write('我很帅'.encode('utf8')) #以字节流形式写入，如果是英文b’hello123'
    file.close()


if __name__ == '__main__':
    # use_seek()
    write_binary()
