from exceptions import *

class TokenType(object):
    """
    Valid token types. Derived from http://rpal.sourceforge.net/doc/lexer.pdf
    """
    (
     # lexical grammar
     IDENTIFIER,
     INTEGER,
     OPERATOR,
     STRING,
     LPAREN,
     RPAREN,
     SEMICOLON,
     COMMA,
     ASSIGN,
     EOF,

     # reserved words
     LET,
     REC,
     WHERE,
     WITHIN,
     AND,
     IN,
     

     # reserved operator words
     OR,
     AMPERSAND,
     NOT,
     GR,
     GE,
     LS,
     LE,
     EQ,
     NE,
     NEG,
     ) = range(26)

    
     
class Token(object):
    """
    Represents a well-formed token.
    """
    def __init__(self, type, value=None, lineno=None):
        self.type = type
        self.value = value
        self.lineno = lineno

    def type_str(self, type):
        """
        Return the string representation of the token type. Ugly.
        """
        if type == TokenType.IDENTIFIER: return "IDENTIFIER"
        if type == TokenType.INTEGER: return "INTEGER"
        if type == TokenType.OPERATOR: return "OPERATOR"
        if type == TokenType.STRING: return "STRING"
        if type == TokenType.LPAREN: return "LPAREN"
        if type == TokenType.RPAREN: return "RPAREN"
        if type == TokenType.SEMICOLON: return "SEMICOLON"
        if type == TokenType.COMMA: return "COMMA"
        if type == TokenType.ASSIGN: return "ASSIGN"
        if type == TokenType.EOF: return "EOF"
        
        if type == TokenType.LET: return "LET"
        if type == TokenType.REC: return "REC"
        if type == TokenType.WHERE: return "WHERE"
        if type == TokenType.WITHIN: return "WITHIN"
        if type == TokenType.AND: return "AND"
        if type == TokenType.IN: return "IN"

        if type == TokenType.OR: return "OR"
        if type == TokenType.AMPERSAND: return "AMPERSAND"
        if type == TokenType.NOT: return "NOT"
        if type == TokenType.GR: return "GR"
        if type == TokenType.GE: return "GE"
        if type == TokenType.LS: return "LS"
        if type == TokenType.LE: return "LE"
        if type == TokenType.EQ: return "EQ"
        if type == TokenType.NE: return "NE"
        if type == TokenType.NEG: return "NEG"

        return "UnknownToken"
    
    def __str__(self):
        return "(%s, %s, %d)" % (self.type_str(self.type), str(self.value), self.lineno)

# reserved keywords/operators
reserved = {"(": TokenType.LPAREN,
            ")": TokenType.RPAREN,
            ";": TokenType.SEMICOLON,
            ",": TokenType.COMMA,
            "=": TokenType.ASSIGN,
            
            "let": TokenType.LET,
            "rec": TokenType.REC,
            "where": TokenType.WHERE,
            "within": TokenType.WITHIN,
            "and": TokenType.AND,
            "in": TokenType.IN,
            
            "or": TokenType.OR,
            "&": TokenType.AMPERSAND,
            "not": TokenType.NOT,
            "gr": TokenType.GR,
            "ge": TokenType.GE,
            "ls": TokenType.LS,
            "le": TokenType.LE,
            "eq": TokenType.EQ,
            "ne": TokenType.NE,
            "neg": TokenType.NEG}
