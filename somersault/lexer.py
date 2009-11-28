import string
import sys

import tokens
from exception import *
from tokens import *
from utils import *

class State(object):
    """
    Represents the state of the lexer.
    """
    (START,
     DONE,
     IDENTIFIER,
     KEYWORD,
     INTEGER,
     OPERATOR,
     STRING,
     WHITESPACE,
     COMMENT) = range(9)
    
class Lexer(object):
    """
    A basic lexer/scanner using a grammar derived from http://rpal.sourceforge.net/doc/lexer.pdf

    One token lookahead.
    """
    def __init__(self, source):
        self._position = 0
        self._lineno = 1
        self._source = source
        self._sourcelen = len(source)
        self._state = State.START
        self._eof = False

    def _advance(self):
        """
        Advance the input stream.
        """
        self._position += 1
        if self._position >= self._sourcelen:
            self._eof = True   

    def in_range(self, c, start, end):
        """
        Returns True if character c is in the range [start, end].
        """
        return start <= c <= end

    def __iter__(self):
        return self

    def _match_comment(self, c):
        """
        Match a single line comment.
        """
        self._state = State.COMMENT
        s = ""
        next = self._peek()
        if not next or next != "/":
            return None
        self._advance()
        next = self._peek()
        if not next:
            return None

        while next != "\n" and next in tokens.string_comment_chars:
            s += next
            self._advance()
            next = self._peek()
            if not next:
                break
        self._advance()

        return Token(TokenType.COMMENT, s, self._lineno)
    
    def _match_identifier(self, c):
        """
        Match an identifier token.
        """
        self._state = State.IDENTIFIER
        s = c
        next = self._peek()
        if not next:
            return None

        while next in string.letters:
            s += next
            self._advance()
            next = self._peek()
            if not next:
                break

        # try to match a reserved keyword
        return Token(tokens.reserved.get(s, TokenType.IDENTIFIER), s, self._lineno)

    def _match_integer(self, c):
        """
        Match an integer literal.
        """        
        self._state = State.INTEGER
        num = int(c)
        next = self._peek()
        if not next:
            return None

        while next in string.digits:
            num = (num * 10) + int(next)
            self._advance()
            next = self._peek()
            if not next:
                break

        return Token(TokenType.INTEGER, num, self._lineno)

    def _match_operator(self, c):
        """
        Match an operator.
        """
        self._state = State.OPERATOR

        if c in tokens.reserved:
            return Token(tokens.reserved[c], c, self._lineno)
        # if c == "."

        if c == "\'":
            return self._match_string(c)

        if c == "/":
            return self._match_comment(c)
        
        s = c
        next = self._peek()
        if not next:
            return Token(TokenType.OPERATOR, s, self._lineno)

        while next in string.punctuation:
            s += next
            self._advance()
            next = self._peek()
            if not next:
                break
        return Token(TokenType.OPERATOR, s, self._lineno)

    def _match_string(self, c):
        """
        Match a string literal.
        """
        self._state = State.STRING
        s = ""
        next = self._peek()
        if not next:
            return None

        while next != "\'" and next in tokens.string_comment_chars:
            s += next
            self._advance()
            next = self._peek()
            if not next:
                break
        self._advance()

        return Token(TokenType.STRING, s, self._lineno)

    def next(self):
        """
        Return the next token or raise StopIteration
        """
        if not self._eof and self._state is not State.DONE:
            return self.next_token()
        else:
            raise StopIteration

    def _next_char(self):
        """
        Return the next character in the input stream and advance to the next.
        """
        c = self._peek()
        if c:
            self._advance()
            return c
        else:
            return None
        
    def next_token(self):
        """
        Scan the next Token and return it.
        """
        if self._eof or self._state is State.DONE:
            return None

        self._skip_whitespace()

        if self._state is State.DONE:
            return None

        c = self._next_char()
        if not c:
            return None
        
        if c in string.punctuation:
            return self._match_operator(c)
        if c in string.digits:
            return self._match_integer(c)
        if c in string.letters:
            return self._match_identifier(c)

        return Token(TokenType.UNKNOWN, c, self._lineno)
    
    def _peek(self):
        """
        Return the next character in the input stream without advancing.
        """
        if not self._eof and self._state is not State.DONE:
            return self._source[self._position]
        else:
            return None
        
    def _skip_whitespace(self):
        """
        Skips whitespace.
        """
        next = self._peek()
        if not next:
            return
        
        while next in string.whitespace:
            if next == '\n':
                self._lineno += 1
            self._advance()
            next = self._peek()
            if not next:
                break



for t in Lexer(file(sys.argv[1]).read()):
    print t
