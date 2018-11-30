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
fin = open("prog.txt", "r")
prog = fin.read()
dic = dict()


# 初始赋值规约
def p_expr_assign(p):
    'term : INT ID ASSIGN expression'
    dic[p[2]] = p[4]
    p[0] = 0

# 赋值规约
def p_expression_assign(p):
    'expression : ID ASSIGN expression'
    p[0] = p[3]

# 数值规约
def p_factor_num(p):
    'expression : NUMBER'
    p[0] = p[1]

# ID规约
def p_expression_ID(p):
    'expression : ID'
    p[0] = dic[p[1]]

# if比较--------------------
# 逻辑大于
def p_greater(p):
    'expression : expression GREATER expression'
    if(p[1] > p[3]): p[0] = True
    else: p[0] = False

# 逻辑小于
def p_smaller(p):
    'expression : expression FEWER expression'
    if(p[1] < p[3]): p[0] = True
    else: p[0] = False

# 小括号
def p_paren_expr(p):
    'judge : LPAREN expression RPAREN'
    p[0] = p[2]


# 大括号
def p_bracket_expr(p):
    'brkt : LBRACKET expression RBRACKET'
    p[0] = p[2]

# 逻辑判断
def p_logic_judge(p):
    'term : IF judge brkt ELSE brkt '
    if(p[2]):
        p[0] = p[3]
    else:
        p[0] = p[5]

# 加法
def p_expression_plus(p):
    'expression : expression PLUS expression'
    p[0] = p[1] + p[3]

# 减法
def p_expression_minus(p):
    'expression : expression MINUS expression'
    p[0] = p[1] - p[3]

# 规约合并
def p_merge(p):
    'term : term term'
    p[0] = p[1] + p[2]


precedence = (
    ('right', 'IF', 'ELSE'),
    ('left', 'PLUS', 'MINUS'),
    ('right', 'INT'),
)


# Error rule for syntax errors
def p_error(p):
    print("ERROR: '{}'".format(p.value))



# Build the parser
parser = yacc.yacc()

result = parser.parse(prog)
print()
print("The result is : ", result)
fin.close()
