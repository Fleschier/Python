# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex

#Dict of reserved word
reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'int': 'INT'
}

# List of token names.   This is always required
tokens = [
    'NUMBER',
    'PLUS',
    'MINUS',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'ASSIGN',
    'FEWER',
    'GREATER',
    'ID'
] + list(reserved.values())

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'\-'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACKET = r'\{'
t_RBRACKET = r'\}'
t_ASSIGN = r'\='
t_FEWER = r'\<'
t_GREATER = r'\>'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

#drop redundant
# def t_COMMENT(t):
#     r'\#.*'
#     pass
#     #return nothing Token discarded

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t;'

# Error handling rule
def t_error(t):
    print ("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

## Build the lexer
prog = '''int asd = 0;
int bc = 10;
if(bc - asd < 2){
	asd = asd + 1;
}else{
	asd = asd - 2;
}'''
lexer = lex.lex()
lexer.input(prog)
for tok in lexer:
    #print(lexer.token())
    print(tok)