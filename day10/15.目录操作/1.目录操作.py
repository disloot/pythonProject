# author luke
# 2022年02月24日
import os

def use_rename():
    os.rename('file','file1')
def use_remove():
    os.remove('file1')

def use_listdir():
    print(os.listdir('.'))


# 深度优先遍历
def dir_dfs(path,width):
    file_list=os.listdir(path)
    for filename in file_list: #遍历当前目录下的所有文件
        print(' '*width+filename)
        if os.path.isdir(path+'/'+filename): #如果是目录
            dir_dfs(path+'/'+filename,width+4)


if __name__ == '__main__':
    # use_rename()
    # use_remove()
    # use_listdir()
    dir_dfs('.',0)