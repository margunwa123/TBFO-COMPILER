def readfile(filename:str):
    fo = open(filename,'r')
    content = fo.readlines()
    print(content)
    fw = open(filename+'hasil','w')
    fw.write(content)

readfile('grammar.txt')