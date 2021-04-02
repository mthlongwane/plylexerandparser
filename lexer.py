# ------------------------------------------------------------
# Lexer.py
# MT Hlongwane 2021 
# Compilers Assignment 3
#  Adapted from PLY Documentation https://ply.readthedocs.io/en/latest/ply.html#lex-example
# ------------------------------------------------------------
import sys
import lex as lex

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
lexer = lex.lex()

# Run the lexer
file_data = ""
while True:
    input_ = sys.stdin.readline()
    if input_ == '#\n':
        break
    file_data += input_

#file_to_be_read = sys.argv[1] 
#file_handler = open(file_to_be_read, "r")
#file_data = file_handler.read()

lexer.input(file_data)


while True:
    lex_token = lexer.token()
    if not lex_token:
        break      # No more input  
    else:
        # if lex_token.type == 'HASH':
        #    break # End of input token due to Hash
        if lex_token.type ==  'NAME': 
            print('(\''+lex_token.type+'\', \''+str(lex_token.value)+'\', '+str(lex_token.lineno)+', '+str(lex_token.lexpos)+')' )
        elif lex_token.type ==  'NUMBER':
            print('(\''+lex_token.type+'\', '+str(lex_token.value)+', '+str(lex_token.lineno)+', '+str(lex_token.lexpos)+')' )
        else:
            print('(\''+lex_token.value+'\', \''+lex_token.value+'\', '+str(lex_token.lineno)+', '+str(lex_token.lexpos)+')' )

#print (file_data)