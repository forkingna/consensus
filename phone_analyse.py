import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab 
import pymysql as MySQLdb
from snownlp import SnowNLP
import time
import sys
TIMEBASE = 1452932340

db = MySQLdb.connect('localhost', 'root', '', 'consensus', charset = 'utf8')
cursor = db.cursor()
fp=open('comments.txt','w',encoding='utf-8')
#txt = unicode("campeón\n", "utf-8"))
sql = """select detail from weibo """
cursor.execute(sql)
for row in cursor.fetchall():
    fp.write(row[0])


exit()


y_num = [i for i in range(8)]
x_phone=['iPone', 'SAMSUNG', 'HUAWEI', 'MI', 'OPPO', 'VIVO', 'MEIZU', 'Others']
sql = """select phone from weibo where phone like '%iPhone%'
        or phone like '%iPad%' """
cursor.execute(sql)
y_num[0] = len(cursor.fetchall())

sql = """select phone from weibo where phone like '%三星%'"""
cursor.execute(sql)
y_num[1] = len(cursor.fetchall())

sql = """select phone from weibo where phone like '%华为%' 
        or phone like '%荣耀%' """
cursor.execute(sql)
y_num[2] = len(cursor.fetchall())

sql = """select phone from weibo where phone like '%米%' """
cursor.execute(sql)
y_num[3] = len(cursor.fetchall())

sql = """select phone from weibo where phone like '%OPPO%'
        or phone like '%oppo%' """
cursor.execute(sql)
y_num[4] = len(cursor.fetchall())

sql = """select phone from weibo where phone like '%vivo%'
        or phone like '%VIVO%' """
cursor.execute(sql)
y_num[5] = len(cursor.fetchall())

sql = """select phone from weibo where phone like '%魅%' """
cursor.execute(sql)
y_num[6] = len(cursor.fetchall())

sql = """select phone from weibo """
cursor.execute(sql)
y_num[7] = len(cursor.fetchall()) - sum([i for i in y_num[:6]])

fig = plt.figure()  
plt.bar(x_phone,y_num,0.4,color="green")  
plt.xlabel("phone")  
plt.ylabel("number")  
plt.title("Client From")  
    
  
plt.show()    