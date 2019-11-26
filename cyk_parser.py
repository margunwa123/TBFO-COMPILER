import os.path
import argparse
import constant as cs

def read_grammar(grammar_file):
    with open(grammar_file) as cfg:
        lines = cfg.readlines()
    a = [x.replace("->", "").split() for x in lines]
    return a

def is_number(s):
    try:
        float(s)    
        return True
    except ValueError:
        return False


class Node:
    """
    Digunakan untuk menyimpan informasi dari simbol non terminal. Sebuah node bisa punya maksimal
    2 anak. Ada kemungkinan 
    Used for storing information about a non-terminal symbol. A node can have a maximum of two
    children because of the CNF of the grammar.
    It is possible though that there are multiple parses of a sentence. In this case information
    about an alternative child is stored in self.child1 or self.child2 (the parser will decide
    where according to the ambiguous rule).
    Either child1 is a terminal symbol passed as string, or both children are Nodes.
    """
    def __init__(self, symbol, child1, child2=None):
        self.symbol = symbol
        self.child1 = child1
        self.child2 = child2
    def __repr__(self):
        """
        :return: the string representation of a Node object.
        """
        return self.symbol


class Parser:
    """
    A CYK parser which is able to parse any grammar in CNF. The grammar can be read from a file or
    passed as a string. It either returns a string representation of the parse tree(s) or prints it
    to standard out.
    """

    def __init__(self, grammar, sentence):
        """
        Creates a new parser object which will read in the grammar and transform it into CNF and
        then parse the given sentence with that grammar.
        :param grammar: the file path to the grammar/the string repr. of the grammar to read in
        :param sentence: the file path to the sentence/the string repr. of the sentence to read in
        """
        self.parse_table = None
        self.prods = {}
        self.grammar = None
        if os.path.isfile(grammar):
            self.grammar_from_file(grammar)
        else:
            self.grammar_from_string(grammar)
        self.__call__(sentence)

    def __call__(self, sentence, parse=False):
        """
        Parse the given sentence (string or file) with the earlier given grammar.
        :param sentence: the sentence to parse with self.grammar
        """
        if os.path.isfile(sentence):
            with open(sentence) as inp:
                self.input = inp.readline().split()
                if parse:
                    self.parse()
        else:
            self.input = sentence.split()

    def grammar_from_file(self, grammar):
        """
        Reads in a CFG from a given file, converts it to CNF and stores it in self.grammar.
        :param grammar: the file in which the grammar is stored.
        """
        self.grammar = read_grammar(grammar)

    def parse(self):
        """
        Does the actual parsing according to the CYK algorithm. The parse table is stored in
        self.parse_table.
        """
        length = len(self.input)
        print("length is ",length)
        for i in range (length) :
            word = self.input[i]
            if word not in cs.terminal:
                print(word)
                if(is_number(word)):
                    self.input[i] = 'int'
                    print("word = ",self.input[i])
                else:
                    self.input[i] = 'word'
        #print("self input : ",self.input)
        #print(" ------------------- self grammar : ---------------\n ",self.grammar)
        # self.parse_table[y][x] is the list of nodes in the x+1 cell of y+1 row in the table.
        # That cell covers the word below it and y more words after.
        self.parse_table = [[[] for x in range(length - y)] for y in range(length)]

        for i, word in enumerate(self.input):
            # Find out which non terminals can generate the terminals in the input string
            # and put them into the parse table. One terminal could be generated by multiple
            # non terminals, therefore the parse table will contain a list of non terminals.
            for rule in self.grammar: #['S'.'WHILE_COND','EPSILON']
                if f"'{word}'" == rule[1]:
                    #print("f word : ",f"'{word}'")
                    self.parse_table[0][i].append(Node(rule[0], word))

        #print("--------------PARSE TABLE------------\n",self.parse_table)
        for words_to_consider in range(2, length + 1):
            for starting_cell in range(0, length - words_to_consider + 1):
                for left_size in range(1, words_to_consider):
                    right_size = words_to_consider - left_size
                    left_cell = self.parse_table[left_size - 1][starting_cell] 
                    # left cell berisi variable yang berada pada sebelah kiri
                    right_cell = self.parse_table[right_size - 1][starting_cell + left_size]
                    # right cell berisi variable yang berada pada sebelah kanan
                    for rule in self.grammar:
                        left_nodes = [n for n in left_cell if n.symbol == rule[1]]
                        

                        if left_nodes:
                            right_nodes = [n for n in right_cell if n.symbol == rule[2]]
                            self.parse_table[words_to_consider - 1][starting_cell].extend(
                                [Node(rule[0], left, right) for left in left_nodes for right in right_nodes]
                            )

    def print_tree(self, output=True):
        """
        Print the parse tree starting with the start symbol. Alternatively it returns the string
        representation of the tree(s) instead of printing it.
        """
        print(self.parse_table)
        if(len(self.parse_table) == 0):
            print("The given sentence is contained in the language produced by the given grammar!")
        else:
            start_symbol = self.grammar[0][0]
            final_nodes = [n for n in self.parse_table[-1][0] if n.symbol == start_symbol]
            if final_nodes:
                if output:
                    print("The given sentence is contained in the language produced by the given grammar!")
                    print("\nPossible parse(s):")
                trees = [generate_tree(node) for node in final_nodes]
                if output:
                    for tree in trees:
                        print(tree)
                else:
                    return trees
            else:
                print("The given sentence is not contained in the language produced by the given grammar!")


def generate_tree(node):
    """
    Generates the string representation of the parse tree.
    :param node: the root node.
    :return: the parse tree in string form.
    """
    if node.child2 is None:
        return f"[{node.symbol} '{node.child1}']"
    return f"[{node.symbol} {generate_tree(node.child1)} {generate_tree(node.child2)}]"


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument("grammar",
                           help="File containing the grammar or string directly representing the grammar.")
    argparser.add_argument("sentence",
                           help="File containing the sentence or string directly representing the sentence.")
    args = argparser.parse_args()
    CYK = Parser(args.grammar, args.sentence)
    CYK.parse()
    CYK.print_tree()