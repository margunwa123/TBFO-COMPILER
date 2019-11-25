import os.path
import argparse

def grammartolist(grammar):
    #grammar adalah nama file yang ingin dibaca
    fo = open(grammar,'r')
    grammar = fo.readlines()
    #asd = x.replace("->","") for x in grammar
    print(grammar)
    print("asd : ",asd)

gr = input("Masukan nama file : ")
asd = read_grammar(gr)
print(asd)