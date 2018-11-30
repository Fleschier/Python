import ply.lex as lex
import ply.yacc as yacc
import re
from math import *
from node import node

#TOKENS
tokens=('SELECT','FROM','WHERE','ORDER','BY','NAME','AVG','NUMBER')
  
literals = ['=','+','-','*', '^','>','<' ] 

#DEFINE OF TOKENS
def t_AVG(t):
    r'AVG'
    return t

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


def t_NUMBER(t):
    r'[0-9]+'
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

#PARSING
def p_query(t):
    '''query :  select '''
    if len(t)==2:
        t[0]=t[1]

def p_select(t):
    '''select :   SELECT list FROM table WHERE lst ORDER BY list
                | SELECT list FROM table WHERE lst
                | SELECT list FROM table ORDER BY list
                | SELECT list FROM table '''
    if len(t)==10:
        t[0]=node('QUERY')
        t[0].add(node('[SELECT]'))
        t[0].add(t[2])
        t[0].add(node('[FROM]'))
        t[0].add(t[4])
        t[0].add(node('[WHERE]'))
        t[0].add(t[6])
        t[0].add(node('[ORDER BY]'))
        t[0].add(t[9])
    elif len(t)==8:
        t[0]=node('QUERY')
        t[0].add(node('[SELECT]'))
        t[0].add(t[2])
        t[0].add(node('[FROM]'))
        t[0].add(t[4])
        t[0].add(node('[ORDER BY]'))
        t[0].add(t[7])
    elif len(t)==7:
        t[0]=node('QUERY')
        t[0].add(node('[SELECT]'))
        t[0].add(t[2])
        t[0].add(node('[FROM]'))
        t[0].add(t[4])
        t[0].add(node('[WHERE]'))
        t[0].add(t[6])
    else:
        t[0]=node('QUERY')
        t[0].add(node('[SELECT]'))
        t[0].add(t[2])
        t[0].add(node('[FROM]'))
        t[0].add(t[4])

def p_table(t):
    '''table : NAME '''
    if len(t)==2:
        t[0]=node('[TABLE]')
        t[0].add(node(t[1]))
    
        

def p_lst(t):
    ''' lst  : condition '''
    
    if len(t)==2:
        t[0]=node('[CONDITION]')
        t[0].add(t[1])
    
        

def p_condition(t):
    ''' condition : NAME '>' NUMBER
                  | NAME '<' NUMBER
                  | NAME '=' NUMBER
                  '''
    t[0]=node('[TERM]')
    if isinstance(t[1], node)==False:
        t[0].add(node(str(t[1])))
        t[0].add(node(t[2]))
        t[0].add(node(t[3]))
  


def p_list(t):
    ''' list : '*'
             | NAME
            '''
    if len(t)==2:
        t[0]=node('[FIELD]')
        t[0].add(node(t[1]))
  
    
def p_error(t):
    print("Syntax error at '%s'" % t.value)

yacc.yacc()

while 1:
    try:
        s = raw_input('-> ')  
        pass
    except EOFError:
        break
    parse=yacc.parse(s)
    parse.print_node(0)
