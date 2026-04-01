from lexer import tokenize
from parser import Parser
from semantic import SemanticAnalyzer
from codegen import CodeGenerator

print("Enter your code (press Enter on an empty line to finish):")
lines = []
while True:
    try:
        line = input()
        if line == "":
            break
        lines.append(line)
    except EOFError:
        break

code = "\n".join(lines)

if not code.strip():
    print("No code provided. Exiting.")
else:
    try:
        tokens = tokenize(code)

        parser = Parser(tokens)
        ast = parser.parse()

        semantic = SemanticAnalyzer()
        semantic.visit(ast)

        generator = CodeGenerator(semantic.symbol_table)
        output = generator.generate(ast)

        print("\nGenerated Python Code:\n")
        print(output)

        print("\nExecuting Generated Code:\n")
        exec(output)
    except Exception as e:
        print(f"\nError: {e}")
