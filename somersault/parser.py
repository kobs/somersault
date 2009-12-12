from ast import *
from exception import *
from lexer import *
from utils import *

class Parser(object):
    """
    An LL(1) parser for Somersault. This parser implementation is basically the grammar
    translated to Python. In other words, it's Somersault specific.
    """
    def __init__(self, source):
        self.lexer = Lexer(source)
        self.tokens = []
        self.nodes = [] # stack holding the AST nodes

    def parse(self):
        """
        Parse the input stream into an AST.
        """
        self.next = self.lexer.next()

    def print_tokens(self):
        """
        Print the tokens collected by the parser/lexer.
        """
        for token in self.tokens:
            print token

    def build_leaf(self, token):
        """
        Build an AST node with no children.
        """
        self.nodes.append(get_node(token))

    def build_parent(self, token, num_children=0):
        """
        Build an AST node with children.
        """
        parent = get_node(token)

        children = [] # stack of children Nodes
        for child in range(num_children):
            children.append(self.pop_node())

        for child in range(num_children, 0, -1):
            children[child].sibling = children[child - 1]

        if num_children > 0:
            parent.child = children[num_children - 1]

        self.nodes.append(parent)

    def pop_node(self):
        """
        Pop the tree node from the top of the stack.
        """
        return self.nodes.pop()
            
    def read(self, token):
        """
        Read an expected value. If token != next, error.
        If token is a rand, build a childless tree.
        """
        if token.type in tokens.rand:
            self.build_leaf(token)
        
        if self.next != token:
            error("Expected %s but found %s on line %d" % (next.value, token.value, next.lineno))

        next = self.lexer.next()

    #### Grammar specific methods ####
    def expression(self):
        """
        E  -> 'let' D 'in' E     => 'let'
           -> 'fn' Vb+ '.' E     => 'lambda'
           -> Ew;
        Ew -> T 'where' Dr       => 'where'
           -> T;
        """
        if next == "let":
            read("let")
            # definition()
            read("in")
            # expression()
            build_tree(let)
        elif next == "fn":
            read("fn")
            # for each parameter:
            #    variable()
            # read(".")
            # expression()
            # build_tree(lambda)
        else:
            pass # where()
    ##################################

def main():
    pass #p = Parser(file(sys.argv[1]).read())
    #p.parse()
    #p.print_tokens()
    
if __name__ == "__main__":
    main()
