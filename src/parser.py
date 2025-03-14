# Parses Python/JS code to an AST
from lark import Lark
# from cgi import parse

#Define a simple program for parsing python exp
python_grammar = """
    start: expr
    expr: term("+" term)*
    term: NUMBER
    %import common.NUMBER
    %import common.WS
    %ignore WS
"""

class PythonParser:
    def __init__(self):
        self.parser = Lark(python_grammar, start="start")

    def parse(self, code):
        return self.parse.parse(code)

if __name__ == "__main__":
    parser = PythonParser()
    tree = parser.parse("5 + 3 + 2")
    print(tree.pretty())
