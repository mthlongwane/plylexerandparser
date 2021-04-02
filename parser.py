# ------------------------------------------------------------
# Parser.py
# MT Hlongwane 2021 
# Compilers Assignment 3
# Adapted from PLY Documentation https://ply.readthedocs.io/en/latest/ply.html#lex-example
# ------------------------------------------------------------

import sys
import lex as lex
import yacc as yacc

# Step 1: Lexer work.

# List of token names.   This is always required
tokens = (
    'NAME',
    'NUMBER',
    'PLUS',
    'LPAREN',
    'RPAREN',
    'EQUALS',
)

# Regular expression rules for simple tokens
t_PLUS      = r'\+'
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_EQUALS    = r'\='
t_NAME      = r'\_?[A-Za-z]+(\_|[A-Za-z]|[0-9])*'

# A regular expression rule with some action code
def t_NUMBER(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
mylexer = lex.lex()
file_data = ""
while True:
    input_ = sys.stdin.readline()
    if input_ == '#\n':
        break
    file_data += input_

mylexer.input(file_data)

# Step 2: Parser.
# dictionary of names
names = {}

def p_statement_expression(p):
    '''statement : expression
                 | factor '''
    p[0] = p[1]
    
def p_statement_assign(p):
    '''statement   : NAME EQUALS expression'''
    p[1] = p[3]

def p_expression_plus(p) :  
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]
    
def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_expression_name(p):
    'term : NAME'
    p[0] = p[1]

def p_term_num(p):
    'term : NUMBER'
    p[0] = p[1]

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

# Error rule for syntax errors
def p_error(p):
        if p: 
            print("Error in input")
            print(p)
            exit(1)
        if not p:
            print(p)


# Build the parser
parser = yacc.yacc()
abstract_syntax_tree = yacc.parse(lexer = mylexer)

print (abstract_syntax_tree)