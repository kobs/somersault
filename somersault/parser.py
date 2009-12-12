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
        self.next_token()
        self.parameter()

    def print_ast(self):
        """
        Print the abstract syntax tree of the source file.
        """
        def preorder(root, depth):
            if root:
                for i in range(depth):
                    print ".",
                print root
                preorder(root.child, depth + 1)
                preorder(root.sibling, depth)
                
        preorder(self.nodes.pop(), 0)

        if len(self.nodes) > 0:
            error("Possible error: extra nodes remain on the stack.")

    def print_tokens(self):
        """
        Print the tokens collected by the parser/lexer.
        """
        for token in self.tokens:
            print token

    def next_token(self):
        self.next = self.lexer.next()
        if self.next:
            self.tokens.append(self.next)
        return self.next
    
    def build_leaf(self, token):
        """
        Build an AST node with no children.
        """
        if isinstance(token, Token):
            self.nodes.append(get_node(token))
        else:
            self.nodes.append(token)

    def build_parent(self, token, num_children=0):
        """
        Build an AST node with children.
        """
        parent = get_node(token)

        children = [] # stack of children Nodes
        for child in range(num_children):
            children.append(self.pop_node())

        for child in range(num_children - 1, 0, -1):
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
        Read an expected token.
        If token is a rand, build a childless tree.
        """
        if token.type in tokens.rand:
            self.build_leaf(token)
        
        self.next_token()

    def read_string(self, value):
        """
        Read an expected string value.
        """
        if self.next != value:
            error("Expected %s but found %s on line %d" % (self.next.value, value, self.next.lineno))

        self.next_token()

    #### Grammar specific methods ####
    def expression(self):
        """
        E  -> 'let' D 'in' E     => 'let'
           -> 'fn' Vb+ '.' E     => 'lambda'
           -> Ew;
        Ew -> T 'where' Dr       => 'where'
           -> T;
        """
        if self.next == "let":
            self.read("let")
            # definition()
            self.read("in")
            # expression()
            # ew, the number of children should probably be a property of the Node object.
            build_tree(let, 2)
        elif self.next == "fn":
            self.read("fn")
            n = 0
            while self.next.type == TokenType.IDENTIFIER or self.next.type == TokenType.LPAREN:
                # parameter()
                n += 1
            self.read(".")
            # expression()
            # build_tree(lambda, n + 1)
        else:
            pass # where()

    def parameter(self):
        """
        Vb -> '<IDENTIFIER>'
           -> '(' Vl ')'
           -> '(' ')'          => '()'
        """
        if self.next.type == TokenType.IDENTIFIER:
            self.read(self.next)
        elif self.next.type == TokenType.LPAREN:
            self.read_string("(")
            if self.next.type == TokenType.IDENTIFIER:
                self.parameter_list()
                self.read_string(")")
            else:
                self.read_string(")")
                self.build_leaf(Unit())
        else:
            error("Expected an IDENTIFIER or '(', but found a(n) %s (of value %s) on line %d." % (self.next.type_str(), self.next.value, self.next.lineno))

    def parameter_list(self):
        """
        Vl -> '<IDENTIFIER>' list ','  => ','?
        """
        n = 0
        if self.next.type == TokenType.IDENTIFIER:
            self.read(self.next)

        token = self.next
        while self.next.type == TokenType.COMMA:
            self.read_string(",")
            if self.next.type != TokenType.IDENTIFIER:
                error("Expected an IDENTIFIER, but found a(n) %s (of value %s) on line %d." % (self.next.type_str(), self.next.value, self.next.lineno))
            self.read(self.next)
            n += 1

        if n > 0:
            self.build_parent(token, n + 1)
            
    ##################################

def main():
    p = Parser(file(sys.argv[1]).read())
    p.parse()
    print "---"
    p.print_tokens()
    print "---"
    p.print_ast()

if __name__ == "__main__":
    main()
