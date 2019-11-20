fo = open('input.txt','r')
content = fo.read()
CC = iter(content)
global a
a = next(CC)
while(a !="\n"):
    print(a)
    a = next(CC)