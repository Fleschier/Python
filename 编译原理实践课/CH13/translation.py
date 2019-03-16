#! /usr/bin/env python
#coding=utf-8
from __future__ import division

v_table={} # variable table

def update_v_table(name,value):
    v_table[name]=value

def trans(node):
    
    # Translation

    # Assignment
    if (node.getdata() == '[ASSIGNMENT]'):
        # 引号注释
        '''assignment : VARIABLE '=' NUMBER
                    | VARIABLE '=' list
                    | VARIABLE '=' len
                    | VARIABLE '=' VARIABLE
                    | VARIABLE '=' '(' expr ')' '/' '/' NUMBER
        '''
        # 用getchild(x).getdata()来判断匹配到的是上面哪一条
        #for i in node.getchildren():
            #print(i.getdata())
        #print('++++')
        if(len(node.getchildren()) == 1):
            trans(node.getchild(0))
        else:
            judge = node.getchild(2).getdata()
            if(judge.isdigit()):        # VARIABLE '=' NUMBER
                #print(judge)
                value = node.getchild(2).getvalue()
                node.getchild(0).setvalue(value)
                # update v_table
                update_v_table(node.getchild(0).getdata(), value)
                # print(v_table)
            elif(judge == '[LIST]'):      # VARIABLE '=' list
                value = []
                getList(node.getchild(2), value)
                #print(value)
                node.getchild(0).setvalue(value)
                # update v_table
                update_v_table(node.getchild(0).getdata(), value)
            elif(judge == '[LEN]'):     # VARIABLE '=' len
                value = len(v_table[node.getchild(2).getchild(2).getdata()])
                #print(value)
                node.getchild(0).setvalue(value)
                # update v_table
                update_v_table(node.getchild(0).getdata(), value)
            elif(judge == '('):         #VARIABLE '=' '(' expr ')' '/' '/' NUMBER
                num = node.getchild(7).getdata()
                #print(num)
                value = calcExpr(node.getchild(3))
                #print(value)
                value1 = float(value) // float(num)
                node.getchild(0).setvalue(value1)
                # update v_table
                update_v_table(node.getchild(0).getdata(), value)
            else:       # VARIABLE '=' VARIABLE
                update(node.getchild(0).getdata(), node.getchild(2).getdata())


    # Operation
    elif node.getdata() == '[OPERATION]':
        '''operation : VARIABLE '=' expr
        '''
        tmpname = node.getchild(0).getdata()      #变量名
        tmpvalue = calcExpr(node.getchild(2))
        node.getchild(0).setvalue(tmpvalue)
        update_v_table(tmpname, tmpvalue)
        

    # Print
    elif node.getdata() == '[PRINT]':
        '''print : PRINT '(' values ')'
        '''
        tmpLst = []
        for i in node.getchildren():
            showPrintData(i, tmpLst)
        tmpLst.reverse()
        for i in tmpLst: print(v_table[i], end="  ")
        print()
    
    # If/Elif
    elif (node.getdata()=='[IF]'):
        r'''if : IF '(' condition ')' '{' statements '}' 
        + [IF]
             + [CONDITION]
               + a[j]
               + >
               + max_v
             + [STATEMENTS]
                ...
        '''
        children=node.getchildren()
        trans(children[0])
        condition=children[0].getvalue()
        if condition:
            for c in children[1:]:
                trans(c)

    #Elif
    # elif(node.getdata() == '[ELIF]'):
    #     ''' elif : ELIF '(' condition ')' '{' statements '}' '''
    #     print("test")
        #children = node.getchildren()
        # trans(children[0])
        # condition = children[0].getvalue()
        # if condition:
        #     trans(children[1])
                
    # While
    elif node.getdata()=='[WHILE]':
        r'''while : WHILE '(' condition ')' '{' statements '}' '''
        children=node.getchildren()
        while trans(children[0]):
            for c in children[1:]:
                trans(c)
            
    # For
    elif(node.getdata() == '[FOR]'):
        r''' for : FOR '(' conditions ')' '{' statements '}'
        '''
        res = []
        getForCondition(node.getchild(0), res)
        #print(res)
        #print(v_table)
        num1 = getValueWithName(res[0])
        num2 = getValueWithName(res[1])
        #print(num1, num2,'---------')
        # for i in node.getchildren():
        #     print(i.getdata())
        while(num1 < num2):
            trans(node.getchild(1))
            num1 += 1



    # Condition
    elif node.getdata()=='[CONDITION]':
        '''condition : VARIABLE '>' VARIABLE
                     | VARIABLE '<' VARIABLE
                     | VARIABLE '<' '=' VARIABLE
                     | VARIABLE '>' '=' VARIABLE
                     | assignment
                     | VARIABLE '+' '+'
            '''
        if(node.getchild(0).getdata() == '[ASSIGNMENT]'):       # assignment
            trans(node.getchild(0))
        elif(node.getchild(1).getdata() == '+'):          # VARIABLE '+' '+'
            v_table[node.getchild(0).getdata()] += 1
        elif(node.getchild(2).getdata() == '='):      # | VARIABLE '<' '=' VARIABLE | VARIABLE '>' '=' VARIABLE
            arg0 = getValue(node.getchild(0).getdata())
            arg1 = getValue(node.getchild(3).getdata())
            op = node.getchild(1).getdata()
            if op == '>':
                node.setvalue(arg0 >= arg1)
            elif op == '<':
                node.setvalue(arg0 <= arg1)
        else:
            #print("====================")
            #print(node.getchild(0).getdata(), node.getchild(2).getdata())
            arg0=getValue(node.getchild(0).getdata())
            arg1=getValue(node.getchild(2).getdata())
            op=node.getchild(1).getdata()
            if op=='>':
                node.setvalue(arg0>arg1)
            elif op=='<':
                node.setvalue(arg0<arg1)
                
    else:
        for c in node.getchildren():
            trans(c)
    
    return node.getvalue()
        

def showPrintData(item, tmpLst):        # 辅助函数: 递归输出树的所有节点
    if(item.getdata() == '[VARIABLE]'):     #只有单个元素
        #print(item.getchild(0).getdata(), end="\t")
        tmpLst.append(item.getchild(0).getdata())

    elif(item.getdata() == '[VARIABLES]'):
        tmpLst.append(item.getchild(2).getdata())   #item是variables标签,variables 下有一个并列的variable需要输出来
        for i in item.getchildren():
            if(len(i.getchildren()) == 3):      #i是variables标签,variables 下有一个并列的variable需要输出来
                # print(i.getchild(2).getdata(), end="++")
                tmpLst.append(i.getchild(2).getdata())
            for res in i.getchildren():
                #print(res.getdata())
                showPrintData(res, tmpLst)

def calcExpr(node):     #计算一个根节点为expr的值,每个有三个子节点的expr子节点为[expr, 运算符, term]
    res = 0
    #print(type(node))
    length = len(node.getchildren())
    #print(length)
    if(length == 3):        #3个子节点的情况
        if(node.getchild(1).getdata() == '+'):
            res = calcExpr(node.getchild(0)) + getFromTerm(node.getchild(2))
            #print(res, 1111)
        elif(node.getchild(1).getdata() == '-'):
            res = calcExpr(node.getchild(0)) - getFromTerm(node.getchild(2))

    elif(length == 1):
        return v_table[node.getchild(0).getchild(0).getchild(0).getdata()]  #expr -> term -> factor -> c

    return res

def getFromTerm(node):        #传入参数是一个term节点
    if(str(node.getchild(0).getchild(0).getdata()).isdigit()):
        return (int)(node.getchild(0).getchild(0).getdata())

    return v_table[node.getchild(0).getchild(0).getdata()]

def getList(node, res):
    #print(node.getdata())
    if(node.getdata() == '[NUMBER]'):
        res.append(node.getchild(0).getvalue())
    elif(node.getdata() == '[LIST]'):
        getList(node.getchild(1), res)
    elif(node.getdata() == '[NUMBERS]'):
        getList(node.getchild(0), res)
        res.append(node.getchild(2).getvalue())

def getForCondition(node, res):
    # 传入CONDITIONS结点
    #获取for循环的三个语句,第一个赋值语句直接计算出结果不必返回,返回第二个约束条件的语句,第三个自增语句不用处理.
    if(node.getdata() == '[CONDITIONS]'):
        #print("test")
        getForCondition(node.getchild(0), res)
        if(len(node.getchildren()) == 3):
            if(node.getchild(2).getchild(1).getdata() == '<'):
                res.append(node.getchild(2).getchild(0).getdata())   # i
                res.append(node.getchild(2).getchild(2).getdata())   # n
                #print(res)
    elif(node.getdata() == '[ASSIGNMENT]'):
        trans(node)         # 如果是赋值语句就计算这句

def isArrayIDX(varName):        #判断一个变量名是不是用下标对数组的引用
    if(varName[-1] == ']'):
        return True
    return False

def update(name, value):
    # 如果要更新的是一个数组的元素
    if(isArrayIDX(name)):
        if(isArrayIDX(value)): # 如果要赋的值也是一个数组的元素
            lst1 = splitStr(name)
            lst2 = splitStr (value)
            #print(lst1,lst2,'++++---+++')   #['a', 'i'] ['a', 'i_v']
            value1 = getValue(lst1[0])
            idx1 = int(getValue(lst1[1]))
            value2 = getValue(lst2[0])
            idx2 = int(getValue(lst2[1]))
            value1[idx1] = value2[idx2]

        else:
            lst = splitStr(name)
            #print(lst)
            var = getValue(lst[0])       # 取得数组名对应的数组
            idx = int(getValue(lst[1]))       # 取得下标对应的值
            var[idx] = value
    else:
        update_v_table(name, value)

def getValue(name):
    #print(name, "++++++++++++++")
    if(isArrayIDX(name)):
        lst = splitStr(name)
        #print(lst, '=-=-=-')
        var = getValueWithName(lst[0])  # 取得数组名对应的数组
        idx = getValueWithName(lst[1])  # 取得下标对应的值
        #print(var)
        #print(idx)
        return var[int(idx)]
    else:
        return getValueWithName(name)

def getValueWithName(name):
    #print(name,'----++++')
    value = v_table[name]
    #print(value,'+++++------')
    if(isinstance(value, str)):
        value = getValue(value)
    return value

def splitStr(name):
    res = []
    lst = name.split('[')
    res.append(lst[0])
    lst = lst[1].split(']')
    res.append(lst[0])
    return res
