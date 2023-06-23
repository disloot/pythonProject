
class File():

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print("entering")
        self.f = open(self.filename, self.mode)
        return self.f

    def __exit__(self, *args):
        print("will exit")
        self.f.close()

def class_use_with():

    with File('output.txt','r') as f:
        print('I will write')
        f.write('python better')

def method_use_with():
    from contextlib import contextmanager

    @contextmanager
    def my_open(path, mode):
        try:
            f = open(path, mode)
            yield f
        except Exception as result:
            print(result)
        finally:
            f.close()  #一旦发生异常，不会走到这里的close


    with my_open('output.txt', 'r') as f:
        f.write("hello , the simplest context manager")



if __name__ == '__main__':
    method_use_with()