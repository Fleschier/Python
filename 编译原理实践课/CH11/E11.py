#! /usr/bin/env python
# coding=utf-8
import ply.lex as lex
import ply.yacc as yacc
from node import node
from fpdf import FPDF, HTMLMixin


def clear_text(text):
    lines = []
    for line in text.split('\n'):
        line = line.strip()
        if len(line) > 0:
            lines.append(line)
    return ' '.join(lines)


# TOKENS
tokens = (
    'TITLE', 'AUTHOR', 'ABS', 'DOC', 'SECTION', 'SUBSECTION', 'TEXT', 'ITEM', 'ITEMIZE', 'BEGIN', 'END', 'LB', 'RB')


# DEFINE OF TOKENS
def t_TITLE(t):
    r'\\title'
    return t


def t_AUTHOR(t):
    r'\\author'
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


def t_ITEM(t):
    r'\\item'
    return t


def t_ITEMIZE(t):
    r'itemize'
    return t


def t_TEXT(t):
    r'[a-zA-Z\s\.\,\'\:]+'
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
    if len(t) == 10:
        t[0] = node('[DOC]')
        t[0].add(t[5])


def p_content(t):
    r'''content : title abs sections
                | title author abs sections itemize'''
    if len(t) == 4:
        t[0] = node('[CONTENT]')
        t[0].add(t[1])
        t[0].add(t[2])
        t[0].add(t[3])
    if len(t) == 6:
        t[0] = node('[CONTENT]')
        t[0].add(t[1])
        t[0].add(t[2])
        t[0].add(t[3])
        t[0].add(t[4])
        t[0].add(t[5])


def p_title(t):
    r'title : TITLE LB TEXT RB'
    if len(t) == 5:
        t[0] = node('[TITLE]'
                    '')
        t[0].add(node(t[3]))


def p_author(t):
    r'author : AUTHOR LB TEXT RB'
    if len(t) == 5:
        t[0] = node('[AUTHOR]')
        t[0].add(node(t[3]))


def p_abs(t):
    r'abs : BEGIN LB ABS RB TEXT END LB ABS RB'
    if len(t) == 10:
        t[0] = node('[ABSTRACT]')
        t[0].add(node(t[5]))


def p_sections(t):
    '''sections : sections section
                | section'''
    if len(t) == 3:
        t[0] = node('[SECTIONS]')
        t[0].add(t[1])
        t[0].add(t[2])
    if len(t) == 2:
        t[0] = node('[SECTIONS]')
        t[0].add(t[1])


def p_subsections(t):
    r"""subsections : subsections subsection
                | subsection"""
    if len(t) == 3:
        t[0] = node("[SUBSECTIONS]")
        t[0].add(t[1])
        t[0].add(t[2])
    if len(t) == 2:
        t[0] = node("[SUBSECTIONS]")
        t[0].add(t[1])


def p_section(t):
    r'''section : SECTION LB TEXT RB TEXT
                    | subsections'''
    if len(t) == 6:
        t[0] = node('[SECTION](%s)' % t[3])
        t[0].add(node(t[5]))
    elif len(t) == 2:
        t[0] = node("[SECTION]")
        t[0].add(t[1])


def p_subsection(t):
    r"""subsection : SUBSECTION LB TEXT RB TEXT"""
    if len(t) == 6:
        t[0] = node("[SUBSECTION](%s)" % t[3])
        t[0].add(node(t[5]))


def p_itemize(t):
    r'itemize : BEGIN LB ITEMIZE RB items END LB ITEMIZE RB TEXT'
    if len(t) == 11:
        t[0] = node('[ITEMIZE]')
        t[0].add(t[5])
        t[0].add(node(t[10]))


def p_items(t):
    '''items : items item
                | item'''
    if len(t) == 3:
        t[0] = node('[items]')
        t[0].add(t[1])
        t[0].add(t[2])
    if len(t) == 2:
        t[0] = node('[items]')
        t[0].add(t[1])


def p_item(t):
    r'item : ITEM TEXT'
    if len(t) == 3:
        t[0] = node('[ITEM]')
        t[0].add(node(t[2]))


def p_error(t):
    print("Syntax error at '%s'" % t.value)


data = clear_text(open('example2.tex', 'r').read())

yacc.yacc()

parse = yacc.parse(data)
parse.print_node(0)

# 获得分析树的所有节点
node_lists = []


def parse_tree(root):
    children = root.getchildren()
    if len(children) == 0:
        node_lists.append(root)
    elif len(children) == 1:
        if children[0].getdata().startswith("["):
            parse_tree(children[0])
        else:
            node_lists.append(root)
    else:
        for c in root.getchildren():
            parse_tree(c)


parse_tree(parse.getchildren()[0])

print("------------------------------")
for i in node_lists:
    print(i.getdata())
# 解析为html

html = ""
section_num = 1
subsection_num = 1
for n in node_lists:
    data = n.getdata()
    if data == "[TITLE]":
        html += "<h1 align='center'><i>%s</i></h1>" % n.getchildren()[0].getdata()
    elif data == "[AUTHOR]":
        html += "<h2 align='center'>%s</h2>" % n.getchildren()[0].getdata()
    elif data == "[ABSTRACT]":
        html += "<h4 align='center'>abstract</h4>"
        html += "<p>%s</p>" % n.getchildren()[0].getdata()
    elif data.startswith("[SECTION]("):
        html += "<h2>%d.%s</h2>" % (section_num, data[10:-1])
        section_num = section_num + 1
        subsection_num = 1
        html += "<p>%s</p>" % n.getchildren()[0].getdata()
    elif data.startswith("[SUBSECTION]("):
        if subsection_num == 1:
            section_num = section_num - 1
        html += "<h3>%d.%d%s</h3>" % (section_num, subsection_num, data[13:-1])
        subsection_num = subsection_num + 1

        html += "<p>%s</p>" % n.getchildren()[0].getdata()
    elif data == "[ITEM]":
        html += "<p><i>%s</i></p>" % n.getchildren()[0].getdata()
    else:
        html += "<p>%s</p>" % data


class MyFPDF(FPDF, HTMLMixin):
    pass


pdf = MyFPDF()
pdf.add_page()
pdf.write_html(html)
pdf.output("text.pdf", 'F')
