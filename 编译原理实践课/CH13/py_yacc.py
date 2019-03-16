#! /usr/bin/env python
#coding=utf-8
import ply.yacc as yacc
from py_lex import *
from node import node,num_node

# YACC for parsing Python

def simple_node(t,name):
    t[0]=node(name)
    for i in range(1,len(t)):
        t[0].add(node(t[i]))
    return t[0]

def p_program(t):
    r'''program : statements'''
    if len(t)==2:
        t[0]=node('[PROGRAM]')
        t[0].add(t[1])
        
def p_statements(t):
    r'''statements : statements statement
                  | statement'''
    if len(t)==3:
        t[0]=node('[STATEMENTS]')
        t[0].add(t[1])
        t[0].add(t[2])
    elif len(t)==2:
        t[0]=node('[STATEMENTS]')
        t[0].add(t[1])

def p_statement(t):
    r''' statement : assignment
                  | operation
                  | print
                  | if
                  | elif
                  | while
                  | for
                  | else
                  '''
    if len(t)==2:
        t[0]=node('[STATEMENT]')
        t[0].add(t[1])

# def p_variable(t):
#     ''' variable : VARIABLE
#                 | VARIABLE '[' VARIABLE ']'
#     '''
#     if(len(t) == 2):
#         t[0] = node('[VARIABLE]')
#         t[0].add(node(t[1]))
#     else:
#         t[0] = simple_node(t, '[VARIABLE_IDX]')



def p_assignment(t):
    r'''assignment : VARIABLE '=' NUMBER
                    | VARIABLE '=' list
                    | VARIABLE '=' len
                    | VARIABLE '=' VARIABLE
                    | VARIABLE '=' '(' expr ')' '/' '/' NUMBER
    '''
    t[0] = node('[ASSIGNMENT]')
    t[0].add(node(t[1]))
    t[0].add(node(t[2]))
    if(len(t) == 4):
        if(type(t[3]) == type(t[0])):
            t[0].add(t[3])
        else:
            if(t[3].isdigit()):
                t[0].add(num_node(t[3]))
            else:
                t[0].add(node(t[3]))
    elif(len(t) == 9):
        t[0].add(node(t[3]))
        t[0].add(t[4])
        t[0].add(node(t[5]))
        t[0].add(node(t[6]))
        t[0].add(node(t[7]))
        t[0].add(num_node(t[8]))

def p_list(t):
    '''list : '[' nums ']' '''
    t[0] = node('[LIST]')
    t[0].add(node(t[1]))
    t[0].add(t[2])
    t[0].add(node(t[3]))

def p_nums(t):
    r''' nums : nums ',' NUMBER
            | NUMBER
    '''
    if(len(t) == 2):
        t[0] = node('[NUMBER]')
        t[0].add(num_node(t[1]))
    else:
        t[0] = node('[NUMBERS]')
        t[0].add(t[1])
        t[0].add(node(t[2]))
        t[0].add(num_node(t[3]))

def p_LEN(t):
    r''' len : LEN '(' VARIABLE ')' '''
    #t[0] = node('[LEN]')
    t[0] = simple_node(t, '[LEN]')

def p_operation(t):
    r'''operation : VARIABLE '=' expr
    '''
    if len(t) == 4:
        t[0] = node('[OPERATION]')
        t[0].add(node(t[1]))
        t[0].add(node(t[2]))
        t[0].add(t[3])


"""expr -> expr + term | term
term -> term * factor | factor
factor -> id | (expr)"""

def p_expr(t):
    r'''expr : expr '+' term
            | expr '-' term
            | term
    '''
    t[0] = node('[expr]')
    if(len(t) == 2):
        t[0].add(t[1])
    else:
        t[0].add(t[1])
        t[0].add(node(t[2]))
        t[0].add(t[3])

def p_term(t):
    r'''term : term '*' factor
            | term '/' factor
            | factor
    '''
    t[0] = node('[term]')
    if(len(t) == 2):
        t[0].add(t[1])
    else:
        t[0].add(t[1])
        t[0].add(node(t[2]))
        t[0].add(t[3])

def p_factor(t):
    r'''factor : VARIABLE
            | NUMBER
    '''
    t[0] = node('[factor]')
    # if(type(t[1]) == type(t[0])):
    #     print(type(t[1]))
    #     t[0].add(t[1])
    if(t[1].isdigit()):       #数字
        t[0].add(num_node(eval(t[1])))
    else:
        t[0].add(node(t[1]))

def p_print(t):
    r'''print : PRINT '(' values ')'
    '''
    t[0] = node('[PRINT]')
    t[0].add(node(t[1]))
    t[0].add(node(t[2]))
    t[0].add(t[3])
    t[0].add(node(t[4]))

def p_values(t):
    r'''values : VARIABLE
                | values ',' VARIABLE
    '''
    if(len(t) == 4):
        t[0] = node('[VARIABLES]')
        t[0].add(t[1])
        t[0].add(node(t[2]))
        t[0].add(node(t[3]))
    else:
        t[0] = node('[VARIABLE]')
        t[0].add(node(t[1]))

def p_conditions(t):
    r''' conditions : conditions ';' condition
                    | condition
     '''
    if(len(t) == 4):
        t[0] = node('[CONDITIONS]')
        t[0].add(t[1])
        t[0].add(node(t[2]))
        t[0].add(t[3])
    if(len(t) == 2):
        t[0] = node('[CONDITIONS]')
        t[0].add(t[1])

def p_condition(t):
    r'''condition : VARIABLE '>' VARIABLE
                 | VARIABLE '<' VARIABLE
                 | VARIABLE '<' '=' VARIABLE
                 | VARIABLE '>' '=' VARIABLE
                 | assignment
                 | VARIABLE '+' '+'
                '''
    if len(t)==4:       #VARIABLE > or < VARIABLE or VARIABLE ++
        t[0]=simple_node(t,'[CONDITION]')
    elif(len(t) == 5):
        t[0] = simple_node(t, '[CONDITION]')
    elif(len(t) == 2):
        t[0] = node('[ASSIGNMENT]')
        t[0].add(t[1])

def p_if(t):
    r'''if : IF '(' condition ')' '{' statements '}'
    '''
    if len(t)==8:
        t[0]=node('[IF]')
        t[0].add(t[3])
        t[0].add(t[6])
        
def p_elif(t):
    r'''elif : ELIF '(' condition ')' '{' statements '}' '''
    if len(t)==8:
        t[0]=node('[ELIF]')
        t[0].add(t[3])
        t[0].add(t[6])

def p_else(t):
    r'''else : ELSE '{' BREAK '}'   '''
    t[0] = simple_node(t, '[ELSE]')

def p_while(t):
    r''' while : WHILE '(' condition ')' '{' statements '}' '''
    if len(t)==8:
        t[0]=node('[WHILE]')
        t[0].add(t[3])
        t[0].add(t[6])


def p_for(t):
    r''' for : FOR '(' conditions ')' '{' statements '}'
    '''
    if(len(t) == 8):
        t[0] = node('[FOR]')
        t[0].add(t[3])
        t[0].add(t[6])


def p_error(t):
    print("Syntax error at '%s'" % t.value)

yacc.yacc()
