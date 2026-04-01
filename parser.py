from ast_nodes import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def eat(self, token_type):
        tok = self.current()
        if tok and tok[0] == token_type:
            self.pos += 1
            return tok
        else:
            raise SyntaxError(f"Expected {token_type}, got {tok}")

    def parse(self):
        statements = []
        while self.current():
            statements.append(self.statement())
        return Program(statements)

    def statement(self):
        tok = self.current()

        if tok[0] in ('INT', 'FLOAT'):
            return self.declaration()
        elif tok[0] == 'PRINTF':
            return self.print_stmt()
        elif tok[0] == 'SCANF':
            return self.scanf_stmt()
        else:
            raise SyntaxError("Invalid statement")

    def declaration(self):
        var_type = self.eat(self.current()[0])[1]
        name = self.eat('ID')[1]
        self.eat('OP')
        value = self.expression()
        self.eat('SEMI')
        return Declaration(var_type, name, value)

    def print_stmt(self):
        self.eat('PRINTF')
        self.eat('LPAREN')
        values = []
        if self.current() and self.current()[0] != 'RPAREN':
            values.append(self.expression())
            while self.current() and self.current()[0] == 'COMMA':
                self.eat('COMMA')
                values.append(self.expression())
        self.eat('RPAREN')
        self.eat('SEMI')
        return Print(values)

    def scanf_stmt(self):
        self.eat('SCANF')
        self.eat('LPAREN')
        name = self.eat('ID')[1]
        self.eat('RPAREN')
        self.eat('SEMI')
        return Scanf(name)

    def expression(self):
        left = self.term()
        while self.current() and self.current()[1] in ('+', '-'):
            op = self.eat('OP')[1]
            right = self.term()
            left = BinOp(left, op, right)
        return left

    def term(self):
        left = self.factor()
        while self.current() and self.current()[1] in ('*', '/'):
            op = self.eat('OP')[1]
            right = self.factor()
            left = BinOp(left, op, right)
        return left

    def factor(self):
        tok = self.current()

        if tok[0] == 'NUMBER':
            self.eat('NUMBER')
            return Number(tok[1])
        elif tok[0] == 'ID':
            self.eat('ID')
            return Identifier(tok[1])
        elif tok[0] == 'STRING':
            self.eat('STRING')
            return String(tok[1])
        elif tok[0] == 'LPAREN':
            self.eat('LPAREN')
            expr = self.expression()
            self.eat('RPAREN')
            return expr
        else:
            raise SyntaxError(f"Invalid factor: {tok}")
