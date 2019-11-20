import constant as cs

def flatten(l : list):
    word = ''.join(l)
    return word

def cmpr(X:str,Y:str):
    return X == Y

global a #a adalah variabel untuk mengiterasikan file

fo = open('input.txt','r')
content = fo.read()
CC = iter(content)

def iterate():
    global a
    a = next(CC)
iterate()

def ignoreBlank():
    global a
    while(a in cs.blanks):
        iterate()

def ignoreWord():
    global a
    ignoreBlank()
    while(not(a in cs.blanks)):
        iterate()
    ignoreBlank()

def IgnoreTilOperator():
    ignoreBlank()
    while(not(a in cs.blanks) and not(a in cs.operator)):
        iterate()
    ignoreBlank()

def ignoreLine():
    global a
    while(a != '\n'):
        iterate()

def getKata():
    global a
    Kata = []
    ignoreBlank()
    while True:
        if (a == ' ') or (len(Kata) >= 12) or (Kata in cs.terminal):
            break
        Kata.append(a)
        iterate()
    Kata = flatten(Kata)
    return Kata


def cekValidasiKata(X=str):
    global a
    if(cmpr(X,"if") or cmpr(X,"for") or cmpr(X,"def") or cmpr(X,"while") or cmpr(X,"elif") or cmpr(X,"else")):
        IgnoreTilOperator()
         

#def run()


adx = "asdasdas"
"""
if(x*5 == )
terminal = [ 
    "\*@(!&@#@\)",
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
"""
