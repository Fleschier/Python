import ply.yacc as yacc

import ply.yacc as yacc
from Calclex import tokens


#每个文法规则（grammar rule）被描述为一个函数，
# 这个函数的文档字符串（doc string）描述了对应的上下文无关文法的规则。
# 函数体用来实现规则的语义动作。每个函数都会接受一个参数p，这个参数是一个序列（sequence），
# 包含了组成这个规则的所有的语法符号，p[i]是规则中的第i个语法符号。


# def p_expression_plus(p):
#     'expression : expression PLUS term'
#     p[0] = p[1] + p[3]
#
#
# def p_expression_minus(p):
#     'expression : expression MINUS term'
#     p[0] = p[1] - p[3]

#这样的定义说明PLUS/MINUS标记具有相同的优先级和左结合性,TIMES/DIVIDE具有相
#同的优先级和左结合性。在precedence声明中,标记的优先级从低到高。因此,这个声明
#表明TIMES/DIVIDE(他们较晚加入precedence)的优先级高于PLUS/MINUS。
# precedence = (
# ('left', 'PLUS', 'MINUS'),
# ('left', 'TIMES', 'DIVIDE'),
# )

# 规约加减
def p_expression(p):
    '''expression : SID '+' factor
                | SID '-' factor'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]

# 最终规约到expression
# one statement
def p_state_match(p):
    '''expression : expression END '''
    p[0] = p[1]


# 从赋值规约到数值-------
# Assign value of int
def p_expr_assign(p):
    '''SID : INT ID ASSIGN NUMBER
                | ID ASSIGN expression
    '''
    if(len(p) == 5):
        p[0] = p[4]
    else:
        p[0] = p[3]


def p_expre_factor(p):
    'expression : factor'
    p[0] = p[1]


def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_ID(p):
    'factor : SID'
    p[0] = p[1]

#---------------------


# if比较--------------------
def p_compare(p):
    '''BOOL : expression GREATER NUMBER
                | expression FEWER NUMBER'''
    if(p[2] == '>'):
        if(eval(p[1]) > eval(p[3])): p[0] = True
        else: p[0] = False
    elif(p[2] == '<'):
        if(eval(p[1]) < eval(p[3])): p[0] = True
        else: p[0] = False


def p_factor_expr(p):
    'judge : LPAREN BOOL RPAREN'
    p[0] = p[2]


def p_logic_judge(p):
    'expression : IF judge LBRACKET expression RBRACKET ELSE LBRACKET expression RBRACKET '
    if(p[2] == True):
        p[0] = p[4]
    else: p[0] = p[8]
    #p[0] = p[8]
#-----------------------------



# Error rule for syntax errors
def p_error(p):
    #p.lexer.skip(1) #跳过一个字符
    print("Syntax error in input!")



# Build the parser
parser = yacc.yacc()

prog = '''int asd = 0;
int bc = 10;
if(bc - asd < 2){
	asd = asd + 1;
}else{
	asd = asd - 2;
}'''
result = parser.parse(prog)
print(result)
