

def change(num_list):
    num_list += [1, 2, 3]  #只有+=与extend等价
    # num_list.extend([1, 2, 3])

    print(num_list)
    print('-'*50)


gl_list = [6, 7, 8]
change(gl_list)
print(gl_list)