myfile = open('abc.txt','wb')
myfile.write(bytes('한글잘나오나',encoding='utf8'))
# print(bytes('한글잘나오나'),file=myfile)
myfile.close()

myfile = open('abc.txt','rb')
line = myfile.read()
str(line,encoding='utf8')
print(line)
# for line in myfile:
#     print(str(line),end="")
myfile.close()
# txt = myfile.read()
# print(txt)