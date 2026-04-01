class CodeGenerator:
    def __init__(self, symbol_table=None):
        self.symbol_table = symbol_table or {}

    def generate(self, node):
        method = f'gen_{type(node).__name__}'
        return getattr(self, method)(node)

    def gen_Program(self, node):
        return '\n'.join(self.generate(stmt) for stmt in node.statements)

    def gen_Declaration(self, node):
        return f"{node.name} = {self.generate(node.value)}"

    def gen_Print(self, node):
        if len(node.values) > 1:
            fmt = self.generate(node.values[0])
            args = ", ".join(self.generate(v) for v in node.values[1:])
            if len(node.values) == 2:
                return f"print({fmt} % {args})"
            else:
                return f"print({fmt} % ({args}))"
        return f"print({self.generate(node.values[0])})"

    def gen_Scanf(self, node):
        var_type = self.symbol_table.get(node.name, 'int')
        if var_type == 'int':
            return f"{node.name} = int(input())"
        elif var_type == 'float':
            return f"{node.name} = float(input())"
        return f"{node.name} = input()"

    def gen_BinOp(self, node):
        return f"{self.generate(node.left)} {node.op} {self.generate(node.right)}"

    def gen_Number(self, node):
        return node.value

    def gen_Identifier(self, node):
        return node.name

    def gen_String(self, node):
        return node.value
