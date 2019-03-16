#! /usr/bin/env python
#coding=utf-8
import ply.lex as lex
import ply.yacc as yacc
from example.node import node

def clear_text(textlines):
    lines=[]
    for line in textlines:
        line=line.strip()
        if len(line)>0:
            lines.append(line)
    return ' '.join(lines)



# TOKENS
tokens=('ITEMIZE', 'ITEM', 'AUTHOR', 'TITLE','ABS','DOC','SECTION', 'SUBSECTION', 'TEXT','BEGIN','END','LB','RB')

#DEFINE OF TOKENS
def t_ITEMIZE(t):
    r'itemize'
    return t

def t_ITEM(t):
    r'\\item'
    return t

def t_AUTHOR(t):
    r'\\author'
    return t

def t_TITLE(t):
    r'\\title'
    return t

def t_DOC(t):
    r'document'
    return t

def t_ABS(t):
    r'abstract'
    return t

def t_SECTION(t):
    r'\\section'
    return t

def t_SUBSECTION(t):
    r'\\subsection'
    return t

def t_TEXT(t):
    r'[a-zA-Z\s\.\,\:\']+'
    return t

def t_BEGIN(t):
    r'\\begin'
    return t


def t_END(t):
    r'\\end'
    return t


def t_LB(t):
    r'\{'
    return t

def t_RB(t):
    r'\}'
    return t


# IGNORED
t_ignore = " \t"
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# LEX
lex.lex()

# PARSE
def p_doc(t):
    r'doc : BEGIN LB DOC RB content END LB DOC RB'
    if len(t)==10:
        t[0]=node('[DOC]')
        t[0].add(t[5])

def p_content(t):
    r'''content :  title abs sections
                    | title author abs sections'''
    if len(t) == 4:
        t[0]=node('[CONTENT]')
        t[0].add(t[1])
        t[0].add(t[2])
        t[0].add(t[3])
    elif len(t) == 5:
        t[0]=node('[CONTENT]')
        t[0].add(t[1])
        t[0].add(t[2])
        t[0].add(t[3])
        t[0].add(t[4])

def p_itemsize(t):
    r'itemize : BEGIN LB ITEMIZE RB items END LB ITEMIZE RB'
    if len(t) == 10:
        t[0] = node('[ITEMIZE]')
        t[0].add(t[5])

def p_items(t):
    r'''items : items item
                | item'''
    if len(t) == 3:
        t[0] = node('[ITEMS]')
        t[0].add(t[1])
        t[0].add(t[2])
    elif len(t) == 2:
        t[0] = node('[ITEMS]')
        t[0].add(t[1])

def p_item(t):
    r'item : ITEM TEXT'
    if len(t) == 3:
        t[0] = node('[ITEM]')
        t[0].add(node(t[2]))


def p_title(t):
    r'title : TITLE LB TEXT RB'
    if len(t)==5:
        t[0]=node('[TITLE]')
        t[0].add(node(t[3]))

def p_author(t):
    r'author : AUTHOR LB TEXT RB'
    if len(t)==5:
        t[0]=node('[AUTHOR]')
        t[0].add(node(t[3]))


def p_abs(t):
    r'abs : BEGIN LB ABS RB TEXT END LB ABS RB'
    if len(t)==10:
        t[0]=node('[ABSTRACT]')
        t[0].add(node(t[5]))

def p_sections(t):
    '''sections : subsection
                | section
                | sections section
                | sections subsection'''
    if len(t) == 2:
        t[0] = node('[SECTIONS]')
        t[0].add(t[1])
    elif len(t) == 3:
        t[0]=node('[SECTIONS]')
        t[0].add(t[1])
        t[0].add(t[2])

def p_section(t):
    r'''section : SECTION LB TEXT RB TEXT
                | SECTION LB TEXT RB TEXT itemize TEXT'''
    if len(t)==6:
        t[0]=node('[SECTION](%s)' %t[3])
        t[0].add(node(t[5]))
    elif len(t) == 8:
        t[0] = node('[SUBSECTION](%s)' %t[3])
        t[0].add(node(t[5]))
        t[0].add(t[6])
        t[0].add(node(t[7]))
def p_subsection(t):
    r'''subsection : SUBSECTION LB TEXT RB TEXT
                    | SUBSECTION LB TEXT RB TEXT itemize TEXT'''
    if len(t)==6:
        t[0]=node('[SUBSECTION](%s)' %t[3])
        t[0].add(node(t[5]))
    elif len(t) == 8:
        t[0] = node('[SUBSECTION](%s)' %t[3])
        t[0].add(node(t[5]))
        t[0].add(t[6])
        t[0].add(node(t[7]))
def p_error(t):
    print("Syntax error at '%s'" % t.value)

data=clear_text(open('example2.tex','r').readlines())

# lexer = lex.lex()
# lexer.input(data)
# for k in  lexer:
#     print(k)
yacc.yacc()

parse=yacc.parse(data)
parse.print_node(0)
#f = open('./result.txt', 'w')
#parse.print_node_to_file(0, f)
#f.close()