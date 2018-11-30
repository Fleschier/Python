from ply import lex
from ply import yacc
from Calclex import tokens

# read file
f = open("prog.txt", "r")
text = f.read()
f.close()

# # construct lexer
# reserved = {
#     'if': 'IF',
#     'else': 'ELSE',
#     'int': 'INT'
# }
#
# tokens = [
#     'NUMBER',   # 23
#     'PLUS',     # '+'
#     'MINUS',    # '-'
#     'EQUAL',    # '='
#     'LP',       # '('
#     'RP',       # ')'
#     'LB',       # '{'
#     'RB',       # '}'
#     'SMALLER',   # '<'
#     'ID',
# ] + list(reserved.values())
#
# t_PLUS = r'\+'
# t_MINUS = r'\-'
# t_EQUAL = r'\='
# t_LP = r'\('
# t_RP = r'\)'
# t_LB = r'\{'
# t_RB = r'\}'
# t_SMALLER = r'\<'
#
#
# def t_ID(t):
#     r'[a-zA-Z_][a-zA-Z_0-9]+'
#     t.type = reserved.get(t.value, 'ID')
#     return t
#
#
# def t_NUMBER(t):
#     r'\d+'
#     t.value = int(t.value)
#     return t
#
#
# def t_newline(t):
#     r'\n+'
#     t.lexer.lineno += len(t.value)
#
#
# t_ignore = ' \t;'
#
#
# def t_error(t):
#     print("Illegal character '{}' ".format(t.value[0]))
#     t.lexer.skip(1)
#
#
# lexer = lex.lex()
#
# print("lex识别的Token：")
# lexer.input(text)
# for token in lexer:
#     print(token)

# yacc parser
var = dict()


def p_merge(p):
    'part : part part'
    p[0] = p[1] + p[2]


def p_initial_assignment(p):
    'part : INT ID ASSIGN expression'
    var[p[2]] = p[4]
    p[0] = 0


def p_assaignment(p):
    'expression : ID ASSIGN expression'
    p[0] = p[3]


def p_expression_plus(p):
    'expression : expression PLUS expression'
    p[0] = p[1] + p[3]


def p_expression_minus(p):
    'expression : expression MINUS expression'
    p[0] = p[1] - p[3]

def p_expression_smaller(p):
    'expression : expression FEWER expression'
    if p[1] < p[3]:
        p[0] = True
    else:
        p[0] = False


def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]


def p_expression_id(p):
    'expression : ID'
    p[0] = var[p[1]]


def p_block(p):
    'block : LBRACKET expression RBRACKET'
    p[0] = p[2]


def p_paren_expression(p):
    'paren_expression : LPAREN expression RPAREN'
    p[0] = p[2]


def p_if_else(p):
    'part : IF paren_expression block ELSE block'
    if p[2]:
        p[0] = p[3]
        # print(p[0])
    else:
        p[0] = p[5]
        # print(p[0])


def p_error(p):
    print("Syntax error in input!")


precedence = (
    ('right', 'IF', 'ELSE'),
    ('left', 'PLUS', 'MINUS'),
    ('right', 'INT'),
)

parser = yacc.yacc()
print("这段文本的结果是: ")
print(parser.parse(text))


