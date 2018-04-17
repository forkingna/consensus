import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab 
import pymysql as MySQLdb
from snownlp import SnowNLP
import time
import sys
TIMEBASE = 1452932340
'''
users = [632 ,78 ,94 , 44]
fig, ax = plt.subplots()#创建子图
plt.rcParams['font.sans-serif']=['SimHei']
labels = '普通用户', '个人认证', '微博大V', '官方微博'
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
explode = (0, 0, 0, 0)
ax.pie(users, explode=explode, labels=labels, colors=colors,
  autopct='%1.1f%%', shadow=True, startangle=90,radius=1.0)
ax.set(aspect="equal", title='用户比例')#设置标题以及图形的对称
plt.show()
exit()
'''
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
db = MySQLdb.connect('localhost', 'root', '', 'consensus', charset = 'utf8')
cursor = db.cursor()
x_time1 = []
y_negativity1 = []

sql1 = """select time, detail from weibo order by time"""
try:
    cursor.execute(sql1)
    results = cursor.fetchall()
except:
    print(sql1) #print(sql)

time_dict={}
for row in results:
    #hour = int(((time.mktime(time.strptime(str(row[0]), "%Y-%m-%d %H:%M:%S")))-TIMEBASE)/3600)
    hour = int(((time.mktime(time.strptime(str(row[0]), "%Y-%m-%d %H:%M:%S")))-TIMEBASE)/86400)
    if hour in time_dict:
        time_dict[hour].append(1-(SnowNLP(row[1]).sentiments))
    else:
        time_dict[hour]=[]
        time_dict[hour].append(1-(SnowNLP(row[1]).sentiments))

for key in time_dict:
    if key>30:
        break
    x_time1.append(key)
    #情感走势
    y_negativity1.append(sum(time_dict[key])/len(time_dict[key]))
    #关注度走势
    #y_negativity1.append(len(time_dict[key])/6)    

x_time2 = []
y_negativity2 = []
sql2 = """select time, detail from weibo 
        where identity='微博达人' or identity='官方认证' or identity='微博大V' 
        order by time"""
try:
    cursor.execute(sql2)
    results = cursor.fetchall()
except:
    print(sql2) #print(sql)

time_dict={}
for row in results:
    #hour = int(((time.mktime(time.strptime(str(row[0]), "%Y-%m-%d %H:%M:%S")))-TIMEBASE)/3600)
    hour = int(((time.mktime(time.strptime(str(row[0]), "%Y-%m-%d %H:%M:%S")))-TIMEBASE)/86400)
    if hour in time_dict:
        time_dict[hour].append(1-(SnowNLP(row[1]).sentiments))
    else:
        time_dict[hour]=[]
        time_dict[hour].append(1-(SnowNLP(row[1]).sentiments))

for key in time_dict:
    if key>30:
        break
    x_time2.append(key)
    #情感走势
    y_negativity2.append(sum(time_dict[key])/len(time_dict[key]))
    #关注度走势
    #y_negativity2.append(len(time_dict[key]))  
#====================================================================

x_time3 = []
y_negativity3 = []
sql3 = """select time, detail from weibo 
        where  identity='官方认证'  
        order by time"""
try:
    cursor.execute(sql3)
    results = cursor.fetchall()
except:
    print(sql3) #print(sql)

time_dict={}
for row in results:
    #hour = int(((time.mktime(time.strptime(str(row[0]), "%Y-%m-%d %H:%M:%S")))-TIMEBASE)/3600)
    hour = int(((time.mktime(time.strptime(str(row[0]), "%Y-%m-%d %H:%M:%S")))-TIMEBASE)/86400)
    if hour in time_dict:
        time_dict[hour].append(1-(SnowNLP(row[1]).sentiments))
    else:
        time_dict[hour]=[]
        time_dict[hour].append(1-(SnowNLP(row[1]).sentiments))

for key in time_dict:
    if key>30:
        break
    x_time3.append(key)
    #情感走势
    y_negativity3.append(sum(time_dict[key])/len(time_dict[key]))
    #关注度走势
    #y_negativity3.append(len(time_dict[key]))  


plt.figure(1)
plt.title("negivitity-time" )
plt.xlabel("time(day)" )
plt.ylabel("negivitity" )

z1 = np.polyfit (x_time1 ,y_negativity1 , 8)
p1 = np.poly1d(z1)
yvals1=p1(x_time1) 

z2 = np.polyfit (x_time2 ,y_negativity2 , 6)
p2 = np.poly1d(z2)
yvals2=p2(x_time2) 

z3 = np.polyfit (x_time3 ,y_negativity3 , 5)
p3 = np.poly1d(z3)
yvals3=p3(x_time3) 

#plt.plot(x_time1, y_negativity1 ,"w",label='original values' )
plt.plot(x_time1 , yvals1, 'r',label='polyfit values' )

#plt.plot(x_time2, y_negativity2 ,"w",label='original values' )
plt.plot(x_time2 , yvals2, 'y',label='polyfit values' )

plt.plot(x_time3 , yvals3, 'b',label='polyfit values' )

plt.yticks([])
plt.show()
##################
exit()
##############
y_num = []
x_phone=['苹果', '三星', '华为', '小米', 'OPPO', 'VIVO', '魅族', '其他']
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
y_num[7] = len(cursor.fetchall()) - sum([y_num[i] for i in y_num[:6]])

fig = plt.figure()  
plt.bar(x_phone,y_num,0.4,color="green")  
plt.xlabel("pyhone")  
plt.ylabel("number")  
plt.title("bar chart")  
    
  
plt.show()    