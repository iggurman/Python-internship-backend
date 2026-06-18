# source code is the code that we can read 
"""
excecution process:-
1)tokenization-what ever we type it gets converted to tokens(source code gets converted to tokens)
code-
1st file:
a=10
b=20
2nd file:
import tokenize
with open(" ", "rb")as f:
    tokens=tokenize.tokenize(f.readline)
    for token in tokens:
    print(tokens)
this generates the tokens for all the lines
2)parser-checks the sequence\grammer of tokens and syntax errors and creates a ast 
3)ast-abstract syntax tree-parser builds an Abstract Syntax Tree (AST) — a tree-shaped representation of the program's logic. 
----------work is being done in source code rn
4)compiler-Converts the AST into bytecode — a compact, low-level set of instructions. This bytecode is cached in .pyc files inside the __pycache__ folder so it doesn't recompile every run. 
"""