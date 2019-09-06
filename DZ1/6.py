import locale
def_coding = locale.getpreferredencoding()
print(def_coding)

f_n = open('test_file.txt', 'w')
f_n.write('сетевое программирование\nсокет\nдекоратор')
f_n.close()
print(type(f_n))

with open('test_file.txt'.encode('utf-8')) as f_n:
    for el_str in f_n:
        print(el_str, end='')