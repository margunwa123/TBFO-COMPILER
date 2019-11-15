import constant as cnst
#TOKEN
fo = open("input.txt", "r")
content = fo.readlines()
packed = []
for line in content:
    packed.append(line.split(' '))
#content adalah array of words kita
global packed_list
packed_list = []
CKata = iter(content)
print(content)
print(packed)

def flatten(l,package):
    for sublist in l:
        for item in sublist:
            package.append(item)

flatten(packed,packed_list)
"""
def del_newline(l):
    asd = l
    for i in range(len(asd)):
        if ('\n' in asd[i]):
            asd[i].rstrip()
    return asd
"""
asd = ['asdsad\n\n']
if '\n' in asd[0]:
    print('sadasd')

asdf = del_newline(asd)
print(asdf)

while ('' in packed_list):
    packed_list.remove('')

print(packed_list)

"""
for strink in packed_list:
    if('\n' in strink):
        Idx = packed_list.index(strink)
        print(Idx)
        print(strink)
        strink.rstrip("\n")
        print(strink)
"""
print(packed_list)

#grammar = {V,Terminal,Start,Production}

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
    ")", ":"
    #26  27
    ]

def is_identifier(strink):
    return (strink in terminal)

if(is_identifier('\n')):
    print('benar')