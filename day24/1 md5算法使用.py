import hashlib
f = open('./test.log', 'rb')
f_md5 = hashlib.md5()
f_md5.update(f.read())
print (f_md5.hexdigest())
