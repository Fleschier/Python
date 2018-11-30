import ply.lex as lex
import ply.yacc as yacc
from sql_example1.node import node

# TOKENS
literals = ['=','+','-','*', '^','>','<' ]

tokens=('SELECT','FROM','WHERE','ORDER','BY','NAME','AND','OR','COMMA',
'LP','RP','AVG','BETWEEN','IN','SUM','MAX','MIN','COUNT','NUMBER','AS',
'DOT')


# DEFINE OF TOKENS
def t_SELECT(t):
    r'SELECT'
    return t
def t_FROM(t):
    r'FROM'
    return t
def t_WHERE(t):
    r'WHERE'
    return t
def t_ORDER(t):
    r'ORDER'
    return t
def t_BY(t):
    r'BY'
    return t
def t_AND(t):
    r'AND'
    return t
def t_OR(t):
    r'OR'
    return t
def t_COMMA(t):
    r'\,'
    return t
def t_LP(t):
    r'\('
    return t
def t_RP(t):
    r'\)'
    return t
def t_AVG(t):
    r'AVG'
    return t
def t_BETWEEN(t):
    r'BETWEEN'
    return t
def t_IN(t):
    r'IN'
    return t
def t_SUM(t):
    r'SUM'
    return t
def t_MAX(t):
    r'MAX'
    return t
def t_MIN(t):
    r'MIN'
    return t
def t_COUNT(t):
    r'COUNT'
    return t
def t_NUMBER(t):
    r'[0-9]+'
    return t
def t_AS(t):
    r'AS'
    return t
def t_DOT(t):
    r'\.'
    return t
def t_NAME(t):
    r'[A-Za-z]+|[a-zA-Z_][a-zA-Z0-9_]*|[A-Z]*\.[A-Z]$'
    return t

# IGNORED
t_ignore = " \t"


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# LEX ANALYSIS
lex.lex()


# PARSING
def p_query(t):
    """
    query : select
            | LP query RP
    """
    if(len(t) > 2):
        t[0] = t[2]
    else:
        t[0] = t[1]

# 最终的token需要做成node,还可以规约的不用做成node

def p_select(t):
    """
    select : SELECT list FROM table WHERE lst ORDER BY list
            | SELECT list FROM table WHERE lst
            | SELECT list FROM table ORDER BY list
            | SELECT list FROM table
    """
    t[0] = node('QUERY')
    t[0].add(node('[SELECT]'))
    t[0].add(t[2])
    # print("+++++++++++")
    # print(type(t[2]))
    # print(t[2])
    # print("++++++++++++")
    t[0].add(node('[FROM]'))
    t[0].add(t[4])
    length = len(t)
    if(length == 10):
        t[0].add(node('[WHERE]'))
        t[0].add(t[6])
        t[0].add(node('[ORDER]'))
        t[0].add(node('[BY]'))
        t[0].add(t[9])
    elif(length == 7):
        t[0].add(node('WHERE'))
        t[0].add(t[6])
    elif(length == 8):
        t[0].add(node('[ORDER]'))
        t[0].add(node('[BY]'))
        t[0].add(t[7])
    else:       #length == 5
        pass

def p_table(t):
    """table : NAME
            | LP query RP
            | NAME AS NAME
            | table AS NAME
            | table COMMA table
    """
    length = len(t)
    t[0] = node('[TABLE]')
    if(length == 2):
        t[0].add(node(t[1]))
    else:
        if(t[1] == '('):
            t[0].add(t[2])
        else:
            if(t[2] == 'AS'):
                if(isinstance(t[1],node.__bases__)):       # NAME AS NAME
                    t[0].add(node(t[1]))
                else:
                    t[0].add(t[1])          # table AS NAME
                t[0].add(node('[AS]'))
                t[0].add(node(t[3]))
            else:       # table COMMA table
                t[0].add(t[1])
                t[0].add(node(t[2]))
                t[0].add(t[3])

def p_lst(t):
    """lst : condition
            | condition AND condition
            | condition OR condition
            | NAME BETWEEN NUMBER AND NUMBER
            | NAME IN LP query RP
            | NAME '<' agg
            | agg '<' NUMBER
            | NAME '>' agg
            | agg '>' NUMBER
            | NAME '=' agg
            | agg '=' NUMBER
    """
    t[0] = node('[lst]')
    if(len(t) == 2):
        t[0].add(t[1])
    elif(len(t) == 4):
        if(t[2] == 'AND'):
            t[0].add(t[1])
            t[0].add(node('[AND]'))
            t[0].add(t[3])
        elif(t[2] == 'OR'):
            t[0].add(t[1])
            t[0].add(node('[OR]'))
            t[0].add(t[3])
        elif(t[2] == '<'):
            if(isinstance(t[3],node.__bases__)):       # NAME '<' agg
                t[0].add(node(t[1]))
                t[0].add(node('<'))
                t[0].add(t[3])
            else:                   # agg '<' NUMBER
                t[0].add(t[1])
                t[0].add(node('<'))
                t[0].add(node(t[3]))
        elif(t[2] == '>'):
            if(isinstance(t[3],node.__bases__)):   # NAME '>' agg
                t[0].add(node(t[1]))
                t[0].add(node('>'))
                t[0].add(t[3])
            else:                       # agg '>' NUMBER
                t[0].add(t[1])
                t[0].add(node('>'))
                t[0].add(node(t[3]))
        elif(t[2] == '='):
            if(isinstance(t[3],node.__bases__)):       # NAME '=' agg
                t[0].add(node(t[1]))
                t[0].add(node('='))
                t[0].add(t[3])
            else:                       # agg '=' NUMBER
                t[0].add(t[1])
                t[0].add(node('='))
                t[0].add(node(t[3]))
    elif(len(t) == 6):
        if(t[2] == 'IN'):
            t[0].add(node(t[1]))
            t[0].add(node(t[2]))
            t[0].add(t[4])
        else:
            t[0].add(node(t[1]))
            t[0].add(node(t[2]))
            t[0].add(node(t[3]))
            t[0].add(node(t[4]))
            t[0].add(node(t[5]))


def p_agg(t):
    """agg : SUM LP NAME RP
            | AVG LP NAME RP
            | COUNT LP NAME RP
            | MIN LP NAME RP
            | MAX LP NAME RP
            | COUNT LP '*' RP
    """
    t[0] = node('[agg]')
    if(len(t) == 2):
        t[0].add(node(t[1]))
    elif(t[1] == 'SUM'):
        t[0].add(node('[SUM]'))
    elif(t[1] == 'AVG'):
        t[0].add(node('[AVG]'))
    elif(t[1] == 'COUNT'):
        t[0].add(node('[COUNT]'))
    elif(t[1] == 'MIN'):
        t[0].add(node('[MIN]'))
    elif(t[1] == 'MAX'):
        t[0].add(node('[MAX]'))
    t[0].add(node(t[3]))


def p_list(t):
    """list : '*'
            | NAME
            | NAME DOT NAME
            | list COMMA list
            | list AND NAME
            | list OR NAME
            | agg
    """
    t[0] = node('[FIELD]')
    if(len(t) == 2):
        # t[0]的type都是sql_example1.node.node!!!!!!
        # if (t[1] == '*'):       # '*'
        #     t[0].add(node(t[1]))
        if(isinstance(t[1],node.__bases__)):     # agg
            t[0].add(node(t[1]))            # 需要写成node(t[1]),为什么???
        else:               # NAME / '*'
            t[0].add(node(t[1]))
        # print(type(t[0]))     #t[0]的type都是sql_example1.node.node!!!!!!
        # print("++++++++++")
    else:
        if(t[2] == '.'):        # 这里不能写为\. 为什么
            t[0].add(node(t[1]))
            t[0].add(node(t[2]))
            t[0].add(node(t[3]))
        elif(t[2] == ','):          # 这里不能写为\, 为什么
            t[0].add(t[1])
            t[0].add(node(t[2]))
            t[0].add(t[3])
        elif(t[2] == 'AND'):
            t[0].add(t[1])
            t[0].add(node('[AND]'))
            t[0].add(node(t[3]))
        elif(t[2] == 'OR'):
            t[0].add(t[1])
            t[0].add(node('[OR]'))
            t[0].add(node(t[3]))

def p_condition(t):
    """
    condition : NAME
    """
    t[0] = node('[condition]')
    t[0].add(t[1])

def p_error(p):
    print("error in syntax")
yacc.yacc()

query = 'SELECT abc FROM def AS fsa'
query1 = 'SELECT sdf.mug FROM jh AS csf ORDER BY fgh AND fg'
query2 = 'SELECT COUNT (asd) FROM asd AS test WHERE asd = COUNT (tst) ORDER BY vdfs.fas OR vds'

parse = yacc.parse(query2)
parse.print_node(0)