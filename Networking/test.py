# -*- coding: utf-8 -*-

#if 判斷 , if true d =4 , else d = 2
#a = 1
a = "abcdefghijklmnopqrstuvwxyz123456789"
d = 4 if isinstance(a, str) else 2
print (d)

#xrange 使用方法
#for i in xrange(0,10,2):
#    print (i)


#List裡面 分割參數 , i:i 是決定位置 +16 是要 i的位置後面的16個字元， ex s = a[0:0 +16] , 0:0本身沒值 但是位置出來了
for i in xrange(0, len(a), 16):
    print (i)
    s = a[i:i + 16]
    print (s)


# Create a bytes object with no "bytes" keyword.
value1 = b"desktop"
print(value1)

# Use bytes keyword.
value2 = bytes(b"desktop")
print(value2)

# Compare two bytes objects.
if value1 == value2:
    print(True)

#join

a1 = b' '.join('test')
print (a1)

a2 = bytes(b' ').join('test')
print (a2)

if a1 == a2:
    print(True)

#ord() , 轉成unicode 字元

print(ord("a"))


#%0*X 要用到幾個 bits的寫法 ， %04X = 0000

target = 'hello'

hexa = ['%0*X' %(4,ord(each_char)) for each_char in target]
print (hexa)


#這邊判別 如果字串沒超過unicode範圍則正常輸出， 超過範圍則用 .取代
a1 = "-abcdefghijklmnopqrstuvwxyz123456789"
s1 = a1[32:32 + 16]
text = [x if 0x20 <= ord(x) <0x7F else b'.' for x in s1]
print (text)

#

result = []

result.append(b"%40X %-*s %s" %(0, 80 ,hexa, text))
print (result)


result2 = []
for i in xrange(0, len(a), 16):

    s = a[i:i + 16]
    hexa = ['%0*X' % (4, ord(each_char)) for each_char in s]
    text = [x if 0x20 <= ord(x) < 0x7F else b'.' for x in s]
    result2.append(b"%40X %-*s %s" % (0, 80, hexa, text))

print (result2)

print
print

###

u = 1
if u == 1:
    print (u)

while True:
    print(u)
    u +=1
    if u == 10:
        break