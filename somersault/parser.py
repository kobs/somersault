from ast import *
from exception import *
from lexer import *
from utils import *

class Parser(object):
    """
    An LL(1) parser for Somersault.
    """
    def __init__(self, source):
        self.lexer = Lexer(source)
        self.tokens = []

    def parse(self):
        """
        Parse the input stream into an AST.
        """
        self.tokens = list(self.lexer)

    def print_tokens(self):
        for token in self.tokens:
            print token

def main():
    p = Parser(file(sys.argv[1]).read())
    p.parse()
    p.print_tokens()
    
if __name__ == "__main__":
    main()
