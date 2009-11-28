class UnknownToken(Exception):
    """
    Exception raised if the lexer encounters an unknown token.
    """
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return "UnknownToken:", text
