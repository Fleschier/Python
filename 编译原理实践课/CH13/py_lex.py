#! /usr/bin/env python
#coding=utf-8
import ply.lex as lex

# LEX for parsing Python

# Tokens
tokens=('VARIABLE', 'NUMBER','IF', 'WHILE', 'PRINT', 'FOR', 'LEN', 'ELIF', 'ELSE', 'BREAK')

literals=['=', '+', '-', '*', '/', '(', ')', '{', '}', '<', '>', '[', ']', ',', ';']

#Define of tokens

def t_NUMBER(t):
    r'[0-9]+'
    return t

def t_PRINT(t):
    r'print'
    return t

def t_IF(t):
    r'if'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_FOR(t):    #注意这里的t_FOR()必须写在t_VARIABLE()前面,否则for关键字会被匹配成VARIABLE!!
    r'for'
    return t

def t_LEN(t):   # LEN 与 FOR同理
    r'len'
    return t

def t_ELIF(t):
    r'elif'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_BREAK(t):
    r'break'
    return t

def t_VARIABLE(t):      # 总之VARIABLE的匹配要放在最后
    r'[a-zA-Z]+_*[a-zA-z]*'
    return t


# Ignored
t_ignore = " \t"

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
lexer = lex.lex()

# from util import clear_text
# text1=clear_text(open('select_sort.py','r').readlines())
# text2=clear_text(open('binary_search.py','r').readlines())
# lexer.input(text2)
# for i in lexer:
#     print(i)