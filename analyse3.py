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
x_time1 = []
y_negativity1 = []

sql1 = """select time, forward from weibo order by time"""
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
        time_dict[hour].append(row[1])
    else:
        time_dict[hour]=[]
        time_dict[hour].append(row[1])

for key in time_dict:
    if key>30:
        break
    x_time1.append(key)
    #情感走势
   # y_negativity1.append(sum(time_dict[key])/len(time_dict[key]))
    #关注度走势
    #y_negativity1.append(len(time_dict[key])/6)    
    #评论 点赞 转发走势
    y_negativity1.append(sum(time_dict[key]))

x_time2 = []
y_negativity2 = []
sql2 = """select time, comment from weibo order by time"""
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
        time_dict[hour].append(row[1])
    else:
        time_dict[hour]=[]
        time_dict[hour].append(row[1])

for key in time_dict:
    if key>30:
        break
    x_time2.append(key)
    #情感走势
    #y_negativity2.append(sum(time_dict[key])/len(time_dict[key]))
    #关注度走势
    #y_negativity2.append(len(time_dict[key]))  
    #评论 点赞 转发走势
    y_negativity2.append(sum(time_dict[key]))
#====================================================================

x_time3 = []
y_negativity3 = []
sql3 = """select time, like_num from weibo order by time"""
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
        time_dict[hour].append(row[1])
    else:
        time_dict[hour]=[]
        time_dict[hour].append(row[1])

for key in time_dict:
    if key>30:
        break
    x_time3.append(key)
    #情感走势
    #y_negativity3.append(sum(time_dict[key])/len(time_dict[key]))
    #关注度走势
    #y_negativity3.append(len(time_dict[key]))
    #评论 点赞 转发走势
    y_negativity3.append(sum(time_dict[key]))


plt.figure(1)
plt.title("" )
plt.xlabel("time(day)" )
plt.ylabel("forward comment like" )

z1 = np.polyfit (x_time1 ,y_negativity1 , 6)
p1 = np.poly1d(z1)
yvals1=p1(x_time1) 

z2 = np.polyfit (x_time2 ,y_negativity2 , 6)
p2 = np.poly1d(z2)
yvals2=p2(x_time2) 

z3 = np.polyfit (x_time3 ,y_negativity3 , 6)
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