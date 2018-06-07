import mysql

conn = MySQLdb.connect(host="192.16.0.12",user="walk",passwd="sn,Z1gddrB#911",db="netgame_trade",charset='utf8')
cur = conn.cursor()

#执行数据库的操作cur.execute
cur.execute('select ID,GOODS_ID,GAME_ID,SERVER_ID,CREATED_BY,CREATED_BY_INFO,ATTRS_VALUE from SELLING_GOODS where ID=1963259')
rows = cur.fetchall()
print rows
f=open('goods.txt', 'w')
f.write(str(rows))
f.close()
conn.close()