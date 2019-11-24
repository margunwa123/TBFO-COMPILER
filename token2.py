import constant as cs

def flatten(l : list):
    word = ''.join(l)
    return word

def cmpr(X:str,Y:str):
    return X == Y

#a adalah variabel untuk mengiterasikan file
global kata2 #ini PUSH DOWN AUTOMATA
EOF = ''
fo = open('input.txt','r')
content = fo.read()
CC = iter(content)
kata2 = []

def iterate():
    global a
    a = next(CC)
    print(a)
iterate()

def terminal(string : str):
    return (string in cs.terminal)

def operator(string : str):
    return (string in cs.operator)

def isEmpty(arr : list):
    return arr == []

def ignoreBlank():
    global a
    while(a == cs.blanks or a in cs.marks):
        if a in cs.marks:
            kata2.append(a)
        iterate()

def getKata():
    global a
    Kata = []
    ignoreBlank()
    while True:
        if ((a == ' ') or (Kata in cs.terminal) or (Kata in cs.operator) or (a in cs.marks) or (a == cs.NEWLINE)):
            break
        Kata.append(a)
        iterate()
    Kata = flatten(Kata)
    return Kata

def isOperation():
    global a
    Kata = getKata()
    print('dalam isoperation',Kata)
    if Kata in cs.operator:
        Kata = getKata()
        print('test',Kata)
        if (not(terminal(Kata)) and not(operator(Kata))):
            return True
        else:
            return False
    elif Kata == ':':
        return True

def evaluate():
    global a
    if (a == EOF):
        return True
    Kata = getKata()
    print('asdasda')
    if(Kata in cs.terminal):
        if(Kata == 'while' or Kata == 'def' or Kata == 'if' or Kata =='elif' or Kata =='else'):
            Kata = getKata()
            if a == ':':
                evaluate()
            else:
                if Kata in cs.operator:
                    return False
                else:
                    if(isOperation()):
                        Kata = getKata()
                        print('kata di isoperat',Kata)
                        if(Kata == ':'):
                            evaluate()
                        else:
                            return False
                    else:
                        return False
        else:
            Kata = getKata()
            print('Kataa di else ',Kata)
            if Kata in cs.operator:
                Kata = getKata()
                if Kata != cs.NEWLINE:
                    evaluate()
                else:
                    return False
            
A = evaluate()
if(A == True):
    print("STATEMENT BENAR")
else:
    print("STATEMENT SALAH")
            
    


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
