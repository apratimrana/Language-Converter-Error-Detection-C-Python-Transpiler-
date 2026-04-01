class Program:
    def __init__(self, statements):
        self.statements = statements

class Declaration:
    def __init__(self, var_type, name, value):
        self.var_type = var_type
        self.name = name
        self.value = value

class Print:
    def __init__(self, values):
        self.values = values

class Scanf:
    def __init__(self, name):
        self.name = name

class BinOp:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Number:
    def __init__(self, value):
        self.value = value

class Identifier:
    def __init__(self, name):
        self.name = name

class String:
    def __init__(self, value):
        self.value = value
