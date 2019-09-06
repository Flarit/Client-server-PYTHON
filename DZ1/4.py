a = "разработка"
b = "администрирование"
c = "protocol"
d = "standard"

en_a = a.encode("utf-8")
en_b = b.encode("utf-8")
en_c = c.encode("utf-8")
en_d = d.encode("utf-8")

print(en_a)
print(en_b)
print(en_c)
print(en_d)

d_a = b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0'
d_b = b'\xd0\xb0\xd0\xb4\xd0\xbc\xd0\xb8\xd0\xbd\xd0\xb8\xd1\x81\xd1\x82\xd1\x80\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5'
d_c = b'protocol'
d_d = b'standard'

a1 = d_a.decode("utf-8")
b1 = d_b.decode("utf-8")
c1 = d_c.decode("utf-8")
d1 = d_d.decode("utf-8")

print (a1)
print (b1)
print(c1)
print(d1)

