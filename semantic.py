class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = {}

    def visit(self, node):
        method = f'visit_{type(node).__name__}'
        return getattr(self, method)(node)

    def visit_Program(self, node):
        for stmt in node.statements:
            self.visit(stmt)

    def visit_Declaration(self, node):
        if node.name in self.symbol_table:
            raise Exception(f"Semantic Error: {node.name} already declared")

        self.symbol_table[node.name] = node.var_type
        self.visit(node.value)

    def visit_Print(self, node):
        for val in node.values:
            self.visit(val)

    def visit_Scanf(self, node):
        if node.name not in self.symbol_table:
            raise Exception(f"Semantic Error: Variable {node.name} must be declared before scanf")

    def visit_BinOp(self, node):
        self.visit(node.left)
        self.visit(node.right)

    def visit_Number(self, node):
        pass

    def visit_Identifier(self, node):
        if node.name not in self.symbol_table:
            raise Exception(f"Semantic Error: {node.name} not declared")

    def visit_String(self, node):
        pass
