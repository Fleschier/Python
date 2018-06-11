dic1={'asd':345,'rggth':456,'dfg':'3456','345':678}
dic2={'asd2':345,'rggth2':'456','dfg2':3456,'a345':678}

for i in dic1:
    if dic1[i] in dic2.values():            #判断第一个字典中的键值是否在第二个字典中
        for j in dic2:
            if dic2[j]==dic1[i]:            #找出第二个字典中对应这个值的键，并输出
                print('dic1:{}  dic2:{}'.format(i,j))
                break