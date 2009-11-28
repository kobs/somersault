import string

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
     INTEGER,
     OPERATOR,
     STRING,
     WHITESPACE,
     COMMENT) = range(8)
    
class Lexer(object):
    """
    A basic lexer/scanner using a grammar derived from http://rpal.sourceforge.net/doc/lexer.pdf

    One token lookahead.
    """
    def __init__(self, source):
        self._position = 0
        self._lineno = 0
        self._source = source
        self._sourcelen = len(source)
        self._state = State.START

    def _advance(self):
        """
        Advance the input stream.
        """
        self._position += 1
        if self._position >= self._sourcelen:
            self._state = State.DONE    

    def in_range(self, c, start, end):
        """
        Returns True if character c is in the range [start, end].
        """
        return start <= c <= end

    def __iter__(self):
        return self
    
    def next(self):
        """
        Return the next token or raise StopIteration
        """
        if self._state is not State.DONE:
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
        if self._state is State.DONE:
            return None

        self._skip_whitespace()

        if self._state is State.DONE:
            return None

        c = self._next_char()
        if c in string.punctuation:
            return self._match_operator(c)
        if c in string.digits:
            return self._match_integer(c)
        if c in string.letters:
            return self._match_identifier(c)

        raise UnknownToken(c)

    def _match_identifier(self, c):
        """
        Match an identifier token.
        """
        self._state = State.IDENTIFIER

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
            if not next: break

        return Token(TokenType.INTEGER, num, self._lineno)

    def _match_operator(self, c):
        """
        Match an operator.
        """
        self._state = State.OPERATOR
        pass

    def _match_string(self, c):
        """
        Match a string literal.
        """
        pass

    def _peek(self):
        """
        Return the next character in the input stream without advancing.
        """
        if self._state is not State.DONE:
            return self._source[self._position]
        else:
            return None
        
    def _skip_whitespace(self):
        """
        Skips whitespace.
        """
        c = self._peek()
        while c in string.whitespace:
            if c == '\n':
                self._lineno += 1
            self._advance()
            c = self._peek()

        if self._position >= self._sourcelen:
            self._state = State.DONE



for t in Lexer("1234 \n56789 999999 1729 314159"):
    print t
