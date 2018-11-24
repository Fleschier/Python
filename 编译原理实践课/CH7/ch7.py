import ply.lex as lex

# List of token names.   This is always required
tokens = (
   'NUMBER',
   # 'PLUS',
   # 'MINUS',
   # 'TIMES',
   # 'DIVIDE',
   # 'LPAREN',
   # 'RPAREN',
    'ELEMENT',
    # 'EQUALS'
)

# Regular expression rules for simple tokens
# t_PLUS    = r'\+'
# t_MINUS   = r'-'
# t_TIMES   = r'\*'
# t_DIVIDE  = r'/'
# t_LPAREN  = r'\('
# t_RPAREN  = r'\)'
t_ELEMENT = (r"C[laroudsemf]?|Os?|N[eaibdpos]?|S[icernbmg]?|P[drmtboau]?|"
r"H[eofgas]?|A[lrsgutcm]|B[eraik]?|Dy|E[urs]|F[erm]?|G[aed]|"
r"I[nr]?|Kr?|L[iaur]|M[gnodt]|R[buhenaf]|T[icebmalh]|"
r"U|V|W|Xe|Yb?|Z[nr]")
# t_EQUALS = r'\=='
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
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print ("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

## Build the lexer
lexer = lex.lex()
s = """He
H2
H2SO4
CH3COOH
NaCl
C60H60"""
lexer.input(s)
for tok in lexer:
    #print(lexer.token())
    print(tok)


import ply.yacc as yacc


def p_parse1(p):
    'species_list : species_list species'
    p[0] = p[1] + p[2]

def p_parse2(p):
    'species_list : species'
    p[0] = p[1]

def p_parse3(p):
    'species : ELEMENT'
    p[0] = 1            #每一个element计数为1

def p_parse4(p):
    'species : ELEMENT NUMBER'
    p[0] = p[2]


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()

result = parser.parse(s)
print("total number of elements is: ", result)