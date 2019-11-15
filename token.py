import constant as cnst
#TOKEN
fo = open("input.txt", "r")
content = fo.read()
#content adalah array of words kita
CC = iter(content)
print(content)
#grammar = {V,Terminal,Start,Production}
terminal = [ 
    "",
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
   # 26
    ]

print(terminal[10])
imp = 0

def is_identifier(strink):
    return (strink in terminal)

if(is_identifier('fabianu')):
    print('benar')