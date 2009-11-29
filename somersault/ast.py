import operator

from exception import NotImplemented

class Node(object):
    """
    A Node represents a node in an abstract syntax tree.
    """
    def __init__(self, token):
        self.value = token.value

    def __iter__(self):
        return self

    def next(self):
        """
        Return the next child Node.
        """
        raise StopIteration

    def __str__(self):
        return "<Node: %s>" % self.value

    def eval(self, env):
        raise NotImplemented

class Identifier(Node):
    """
    Represents an Identifier Node.
    """
    def __init__(self, token):
        self.value = token.value
        self.children = None

    def __iter__(self):
        return self

    def next(self):
        raise StopIteration

    def __str__(self):
        return "<Identifier: %s>" % self.value

    def eval(self, env):
        return env[self.value]

class Nil(Node):
    """
    Represents nil
    """
    def __init__(self, token):
        self.value = "nil"

    def __iter__(self):
        return self

    def next(self):
        raise StopIteration

    def eval(self, env):
        return None

class Dummy(Node):
    """
    Represents dummy
    """
    def __init__(self, token):
        self.value = "dummy"
        self.token

    def __iter__(self):
        return self

    def next(self):
        raise StopIteration

    def eval(self):
        return None
        
class Bool(Node):
    """
    Represents a boolean Node.
    """
    def __init__(self, token):
        self.value = bool(token.value)

    def __iter__(self):
        return self

    def next(self):
        raise StopIteration

    def __str__(self):
        return "<Bool: %s>" % self.value

    def eval(self, env):
        return self.value
    
class Integer(Node):
    """
    Represents an integral Node.
    """
    def __init__(self, token):
        self.value = token.value
        self.children = None

    def __iter__(self):
        return self

    def next(self):
        raise StopIteration

    def __str__(self):
        return "<Integer: %s>" % self.value

    def eval(self, env):
        return self.value

class String(Node):
    """
    Represents a string literal Node.
    """
    def __init__(self, token):
        self.value = token.value
        self.children = None

    def __iter__(self):
        return self

    def next(self):
        raise StopIteration

    def __str__(self):
        return "<String: %s>" % self.value

    def eval(self, env):
        return self.value

class UnaryOp(Node):
    """
    Represents a unary expression.
    """
    ops = {"neg": operator.neg,
           "not": operator.not_}
    
    def __init__(self, token, operand):
        self.operator = token.value
        self.operand = operand

    def __iter__(self):
        return self

    def next(self):
        yield self.operand
        raise StopIteration

    def __str__(self):
        return "<UnaryOp: %s %s>" % (self.operand, self.operator)

    def eval(self, env):
        return ops[self.operator](self.operand.eval(env))
    
class BinaryOp(Node):
    """
    Represents a binary expression.
    """
    ops = {"+":   operator.add,
           "-":   operator.sub,
           "*":   operator.mul,
           "/":   operator.div,
           "**":  operator.pow,
           "@":   operator.add,

           "or":  operator.or,
           "&":   operator.and,
           "gr":  operator.gt,
           "ge":  operator.ge,
           "ls":  operator.lt,
           "le":  operator.le,
           "eq":  operator.eq,
           "ne":  operator.ne}
    
    def __init__(self, token, left, right):
        self.operator = token.value
        self.left = left
        self.right = right

    def __iter__(self):
        return self

    def next(self):
        yield self.left
        yield self.right
        raise StopIteration
    
    def __str__(self):
        return "<BinaryOp: %s %s %s>" % (self.left, self.operator, self.right)

    def eval(self, env):
        return ops[self.operator](self.left.eval(env), self.right.eval(env))

class AST(object):
    """
    A collection (tree) of Nodes representing an abstract syntax tree.
    """
    def __init__(self, nodes=None):
        self.nodes = nodes
