import re

TOKEN_SPEC = [
    ('NUMBER',   r'\d+(\.\d*)?'),
    ('ID',       r'[A-Za-z_]\w*'),
    ('OP',       r'[+\-*/=]'),
    ('SEMI',     r';'),
    ('COMMA',    r','),
    ('LPAREN',   r'\('),
    ('RPAREN',   r'\)'),
    ('STRING',   r'".*?"'),
    ('SKIP',     r'[ \t]+'),
    ('NEWLINE',  r'\n'),
    ('MISMATCH', r'.'),
]

KEYWORDS = {'int', 'float', 'printf', 'scanf'}

def tokenize(code):
    tokens = []
    tok_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_SPEC)

    for mo in re.finditer(tok_regex, code, re.DOTALL):
        kind = mo.lastgroup
        value = mo.group()

        if kind == 'NUMBER':
            tokens.append(('NUMBER', value))
        elif kind == 'ID':
            if value in KEYWORDS:
                tokens.append((value.upper(), value))
            else:
                tokens.append(('ID', value))
        elif kind in ('OP', 'SEMI', 'COMMA', 'LPAREN', 'RPAREN', 'STRING'):
            tokens.append((kind, value))
        elif kind == 'NEWLINE' or kind == 'SKIP':
            continue
        elif kind == 'MISMATCH':
            raise SyntaxError(f'Lexical Error: Unexpected {value}')

    return tokens
