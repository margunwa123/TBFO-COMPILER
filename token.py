import constant as cnst

#TOKEN
fo = open("input.txt", "r")
content = fo.readlines()
print('content')
print(content)
packed = []
for line in content:
    packed.append(line.split(' '))
print('packed : ',packed)
#content adalah array of words kita
global packed_list
packed_list = []
CKata = iter(content)

def flatten(l,package):
    for sublist in l:
        for item in sublist:
            if item != '':
                package.append(item)

flatten(packed,packed_list)
print(packed_list)

def del_newline(li : list):
    newli = []
    for i in range (len(li)):
        newli.append(li[i].rstrip())
        if '\n' in li[i]:
            newli.append('\n')
    return newli


packed_list = del_newline(packed_list)
#grammar = {V,Terminal,Start,Production}
print(packed_list)
terminal = [ 
    "!@*#(!@*()!*@)(*!@()#@(A))I)(DKSAN)",
    "False", "class", "is", "return", "None",
    #  1        2      3       4        5
    "continue", "for", "True", "def", "From",
    #    6        7      8       9      10
    "while", "and", "not", "with", "as",
    #  11      12     13     14     15
    "elif", "if", "or", "else", "import",
    #  16    17    18     19       20
    "pass", "break", "in", "raise", "(",
    #  21     22      23     24     25
    ")", ":","."
    #26  27  28
    ]

need_tikom = [
    "if","elif","else","while","for","def"
]
def is_identifier(string : str):
    return (string in terminal)

def checkKebenaranFile(li : list):
    check = True
    for i in range (len(li)):
        if not(is_identifier(li[i])):
            check = False
    return check

if checkKebenaranFile(packed_list):
    print('Benar')
else:
    print('Gabener')