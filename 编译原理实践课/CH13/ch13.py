#! /usr/bin/env python
#coding=utf-8
from py_yacc import yacc
from util import clear_text
from translation import trans,v_table

text1=clear_text(open('select_sort.py','r').readlines())
text2=clear_text(open('binary_search.py','r').readlines())

# syntax parse
root1=yacc.parse(text1)
root2=yacc.parse(text2)
print("select_sort.py:")
print("======================================================")
root1.print_node(0)
print()
print("binary_search.py:")
print("======================================================")
root2.print_node(0)

print('-------------------------------------')

# translation
print("translation: ")
print("select_sort.py:")
print("======================================================")
trans(root1)
print (v_table)
print()

v_table.clear()

print("binary_search.py:")
print("======================================================")
trans(root2)
print (v_table)


