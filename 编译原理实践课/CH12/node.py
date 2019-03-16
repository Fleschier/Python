#! /usr/bin/env python
#coding=utf-8
class node:

    def __init__(self, data):
        self._data = data   # 节点存储的值
        self._children = [] # 子节点
        self._value=None    # 如果是数值,则将数值的值存储在这个字段中
 
    def getdata(self):
        return self._data
    
    def setvalue(self,value):
        self._value=value
    
    def getvalue(self):
        return self._value
    
    def getchild(self,i):
        return self._children[i]
 
    def getchildren(self):
        return self._children
 
    def add(self, node):
        self._children.append(node)
 
    def print_node(self, prefix):
        print ('  '*prefix,'+',self._data)
        for child in self._children:
            child.print_node(prefix+1)
            
def num_node(data):     # 数值类型节点
    t=node(data)
    t.setvalue(float(data))
    return t