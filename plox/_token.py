""" Note that this module is prefixed by '_' so as to
not interfere with the 'token' standard python library:
    https://bugs.python.org/issue21924
"""
import enum


TokenType = enum.Enum(
    name='TokenType',
    value=[
        # Single-character tokens
        'LEFT_PAREN', 'RIGHT_PAREN', 'LEFT_BRACE', 'RIGHT_BRACE',
        'COMMA', 'DOT', 'MINUS', 'PLUS', 'SEMICOLON', 'SLASH', 'STAR',

        # One or two character tokens
        'BANG', 'BANG_EQUAL', 'EQUAL', 'EQUAL_EQUAL',
        'GREATER', 'GREATER_EQUAL', 'LESS', 'LESS_EQUAL',

        # Literals
        'IDENTIFIER', 'STRING', 'NUMBER',

        # Keywords
        'AND', 'CLASS', 'ELSE', 'FALSE', 'FUN', 'FOR', 'IF', 'NIL', 'OR',
        'PRINT', 'RETURN', 'SUPER', 'THIS', 'TRUE', 'VAR', 'WHILE',

        # End of file
        'EOF'
    ]
)


class Token:

    def __init__(self,
                 type: TokenType,
                 lexeme: str,
                 literal: object,
                 line: int):

        self.type = type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    def __repr__(self):
        return f"<{self.type} '{self.lexeme}'>"
