from _token import Token, TokenType


class Scanner:

    def __init__(self, source: str):
        self.source = source
        self.tokens = []
        self.start = 0
        self.current = 0
        self.line = 1
        self.had_error = False

    def scan(self):
        while not self.is_at_end():
            self.start = self.current
            self.scan_token()
        print(self.tokens)

        token = Token(
            type=TokenType.EOF, lexeme="",
            literal=None, line=self.line
        )
        self.tokens.append(token)

    def error(self, message):
        print(f"[line: {self.line}] Error: {message}")
        self.had_error = True

    def is_at_end(self):
        return self.current >= len(self.source)

    def advance(self):
        c = self.source[self.current]
        self.current += 1
        return c

    def scan_token(self):
        c = self.advance()

        if c == '(':
            self.add_token(TokenType.LEFT_PAREN)
        elif c == ')':
            self.add_token(TokenType.RIGHT_PAREN)
        elif c == '{':
            self.add_token(TokenType.LEFT_BRACE)
        elif c == '}':
            self.add_token(TokenType.RIGHT_BRACE)
        elif c == ',':
            self.add_token(TokenType.COMMA)
        elif c == '.':
            self.add_token(TokenType.DOT)
        elif c == '-':
            self.add_token(TokenType.MINUS)
        elif c == '+':
            self.add_token(TokenType.PLUS)
        elif c == ';':
            self.add_token(TokenType.SEMICOLON)
        elif c == '*':
            self.add_token(TokenType.STAR)
        elif c == '!':
            self.add_token(
                TokenType.BANG_EQUAL
                if self.match('=') else TokenType.EQUAL
            )
        elif c == '=':
            self.add_token(
                TokenType.EQUAL_EQUAL
                if self.match('=') else TokenType.EQUAL
            )
        elif c == '<':
            self.add_token(
                TokenType.LESS_EQUAL
                if self.match('=') else TokenType.LESS
            )
        elif c == '>':
            self.add_token(
                TokenType.GREATER_EQUAL
                if self.match('=') else TokenType.GREATER
            )
        elif c == '/':
            if self.match('/'):
                while self.peek() != '\n' and not self.is_at_end():
                    self.advance()
            else:
                self.add_token(TokenType.SLASH)
        elif c in (' ', '\r', '\t'):
            pass
        elif c == '\n':
            self.line += 1
        elif c == '"':
            self.string()
        else:
            msg = f'Unexpected character "{c}"'
            self.error(msg)

    def string(self):
        while self.peek() != '"' and not self.is_at_end():
            if self.peek() == '\n':
                self.line += 1
            self.advance()
        if self.is_at_end():
            self.error("Unterminated string!")
            return

        # Close the '"'
        self.advance()
        value = self.source[self.start+1:self.current-1]
        self.add_token(TokenType.STRING, value)

    def match(self, expected):
        if self.is_at_end():
            return False
        elif self.source[self.current] != expected:
            return False
        else:
            self.advance()
            return True

    def peek(self):
        if self.is_at_end():
            return '\0'
        else:
            return self.source[self.current]

    def add_token(self,
                  type: TokenType,
                  literal: object = None):
        text = self.source[self.start:self.current]
        self.tokens.append(
            Token(type=type, lexeme=text, literal=literal, line=self.line)
        )
