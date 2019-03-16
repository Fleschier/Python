import ply.lex as lex
import ply.yacc as yacc
from node import node
from fpdf import FPDF, HTMLMixin

def clear_text(textlines):
    lines=[]
    for line in textlines:
        line=line.strip()
        if len(line)>0:
            lines.append(line)
    return ' '.join(lines)


# TOKENS
tokens=('TITLE','ABS','DOC','SECTION','SUBSECTION','TEXT','BEGIN','END','LB','RB','AUTHOR','ITEM','ITEMIZE')

#DEFINE OF TOKENS
def t_TITLE(t):
    r'\\title'
    return t
def t_ITEM(t):
    r'\\item'
    return t
def t_ITEMIZE(t):
    r'itemize'
    return t
def t_DOC(t):
    r'document'
    return t
def t_ABS(t):
    r'abstract'
    return t
def t_SUBSECTION(t):
    r'\\subsection'
    return t
def t_SECTION(t):
    r'\\section'
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
def t_AUTHOR(t):
    r'\\author'
    return t





# IGNORED
t_ignore = " \t"
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


data=clear_text(open('example2.tex', 'r').readlines())
# LEX
lexer = lex.lex()
# lexer.input(data)
# for tok in lexer:
#     #print(lexer.token())
#     print(tok)

# PARSE
def p_doc(t):
    r'doc : BEGIN LB DOC RB content END LB DOC RB'
    if len(t)==10:
        t[0]=node('[DOC]')
        t[0].add(t[5])


def p_content(t):
    r'content : title author abs sections itemize'
    t[0]=node('[CONTENT]')
    t[0].add(t[1])
    t[0].add(t[2])
    t[0].add(t[3])
    t[0].add(t[4])
    t[0].add(t[5])


def p_title(t):
    r'title : TITLE LB TEXT RB'
    if len(t)==5:
        t[0]=node('[TITLE]')
        t[0].add(node(t[3]))


def p_author(t):
    r'author : AUTHOR LB TEXT RB'
    if(len(t) == 5):
        t[0] = node('[AUTHOR]')
        t[0].add(node(t[3]))

def p_abs(t):
    r'abs : BEGIN LB ABS RB TEXT END LB ABS RB'
    if len(t)==10:
        t[0]=node('[ABSTRACT]')
        t[0].add(node(t[5]))


def p_sections(t):
    '''sections : sections section
                | section'''
    if len(t)==3:
        t[0]=node('[SECTIONS]')
        t[0].add(t[1])
        t[0].add(t[2])
        #print(t[1])    #匹配一次
    if len(t)==2:
        t[0]=node('[SECTIONS]')
        t[0].add(t[1])
        #print(t[1])     #匹配一次

def p_section(t):
    r'section : SECTION LB TEXT RB TEXT'
    if len(t)==6:
        t[0]=node('[SECTION](%s)' %t[3])
        t[0].add(node(t[5]))
        # print(t[5])    #正确匹配到两个section
        # print("-----------------------")

def p_subsections(t):
    '''section : section subsection
                | subsection
    '''
    if len(t)==3:
        t[0]=node('[SECTIONS]')
        t[0].add(t[1])
        t[0].add(t[2])
        #print(t[2])
    if len(t)==2:
        t[0]=node('[SECTIONS]')
        t[0].add(t[1])

def p_subsection(t):
    r'''subsection : SUBSECTION LB TEXT RB TEXT
    '''
    if len(t)==6:       #可以匹配
        t[0]=node('[SUBSECTION](%s)' %t[3])
        # print(t[3])
        # print("===============")
        t[0].add(node(t[5]))
        # print(t[5])
        # print("+++++++++++++++++++++++++++++")
    elif(len(t) == 8):
        t[0] = node('[SUBSECTION](%s)' % t[3])
        print(t[3])
        #print("===============")
        t[0].add(node(t[5]))
        t[0].add(t[6])
        #print(t[5])
        #print("***************************")
        t[0].add(node(t[7]))

def p_itemsize(t):
    r'itemize : BEGIN LB ITEMIZE RB items END LB ITEMIZE RB TEXT'
    if len(t) == 11:
        t[0] = node('[ITEMIZE]')
        t[0].add(t[5])
        t[0].add(node(t[10]))

def p_items(t):
    r'''items : items item
                | item
        '''
    if len(t) == 3:
        t[0] = node('[ITEMS]')
        t[0].add(t[1])
        t[0].add(t[2])
    elif len(t) == 2:
        t[0] = node('[ITEMS]')
        t[0].add(t[1])

def p_item(t):
    r'item : ITEM TEXT'
    t[0] = node('[ITEM]')
    t[0].add(node(t[2]))


def p_error(t):
    print("Syntax error at '%s'" % t.value)


yacc.yacc()

parse=yacc.parse(data)
parse.print_node(0)

# get all the nodes info

allNodes = []

def getNodesFromTree(node):
    if(len(node.getchildren()) == 0):
        allNodes.append(node)
    elif(len(node.getchildren()) == 1):
        child = node.getchild(0)
        if(child.getdata()[0] == '['):
            getNodesFromTree(child)
        else:
            allNodes.append(node)       #获取文字部分
    else:
        for item in node.getchildren():
            getNodesFromTree(item)

getNodesFromTree(parse.getchild(0))
# for i in allNodes:
#     print(i.getdata())

# build the html type input

html = ""
sectionNum = 1
subsectionNum = 1
for n in allNodes:
    data = n.getdata()
    if data == "[TITLE]":
        html += "<h1 align='center'><i>%s</i></h1>" % n.getchildren()[0].getdata()
    elif data == "[AUTHOR]":
        html += "<h2 align='center'>%s</h2>" % n.getchildren()[0].getdata()
    elif data == "[ABSTRACT]":
        html += "<h3 align='center'>abstract</h4>"
        html += "<p>%s</p>" % n.getchildren()[0].getdata()
    elif data.startswith("[SECTION]("):
        html += "<h3>%d %s</h2>" % (sectionNum, data[10:-1])
        sectionNum = sectionNum + 1
        subsectionNum = 1
        html += "<p>%s</p>" % n.getchildren()[0].getdata()
    elif data.startswith("[SUBSECTION]("):
        if subsectionNum == 1:
            sectionNum = sectionNum - 1
        html += "<h4>%d.%d %s</h3>" % (sectionNum, subsectionNum, data[13:-1])
        subsectionNum = subsectionNum + 1

        html += "<p>%s</p>" % n.getchildren()[0].getdata()
    elif data == "[ITEM]":
        html += "<p><i>%s</i></p>" % n.getchildren()[0].getdata()
    else:
        html += "<p>%s</p>" % data


class MypyFPDF(FPDF, HTMLMixin):
    pass


pdf = MypyFPDF()
pdf.add_page()
pdf.write_html(html)
# pdf.set_font('Arial', 'B', 16)
pdf.output("res.pdf", 'F')