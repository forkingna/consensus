
import sys
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

reload(sys)
sys.setdefaultencoding('utf8')


ip_set=set()
asn_ip={}
asn_adj={}

while True:
    line = sys.stdin.readline()
    if not line:
        break
    inf = line.split('|')

    ip_set.add(inf[5])

    asn_list = inf[6].split(' ')
    len_asn_list = len(asn_list)
    if asn_ip.has_key(asn_list[-1]):
        asn_ip[asn_list[-1]].add(inf[5])
    else:
        asn_ip[asn_list[-1]] = set()
        asn_ip[asn_list[-1]].add(inf[5])

    for i in range(len(asn_list)-1):
        if asn_adj.has_key(asn_list[i]):
            asn_adj[asn_list[i]].add(asn_list[i+1])
        else:
            asn_adj[asn_list[i]] = set()
            asn_adj[asn_list[i]].add(asn_list[i+1])
        if asn_adj.has_key(asn_list[i+1]):
            asn_adj[asn_list[i+1]].add(asn_list[i])
        else:
            asn_adj[asn_list[i+1]] = set()
            asn_adj[asn_list[i+1]].add(asn_list[i])


#print "ip_set:"
#print ip_set
#print "asn_ip:"
#print asn_ip
#print "asn_adj:"
#print asn_adj


print "number of ip:", len(ip_set)
print "number of AS:", len(asn_adj)


#######    Prefix Frequency  ##########
ip_list =[]
for ip in asn_ip.values():
    ip_list.append(len(ip))
c = dict(Counter(ip_list))
x_list = c.keys()
x_list.sort()
y_list = []
for x in list(x_list):
    y_list.append(c[x])

x_degree = np.log(x_list)
y_degree = np.log(y_list)

plt.figure(1)
plt.title("Prefix Frequency(log-log)" )
plt.xlabel("Prefix" )
plt.ylabel("Frequency" )
z1 = np.polyfit (x_degree ,y_degree , 8)
p1 = np.poly1d(z1)
yvals=p1(x_degree )
plt.plot(x_degree ,y_degree ,"o",label='original values' )
plt.plot(x_degree , yvals, 'r',label='polyfit values' )
plt.show()
#plt.savefig("../pig1.png")

######     Degree Frequency ###########
adj_list =[]
for adj in asn_adj.values():
    adj_list.append(len(adj))
c = dict(Counter(adj_list))
x_list = c.keys()
x_list.sort()
y_list = []
for x in list(x_list):
    y_list.append(c[x])

x_degree = np.log(x_list)
y_degree = np.log(y_list)

plt.figure(2)
plt.title("Degree Frequency(log-log)" )
plt.xlabel("Degree" )
plt.ylabel("Frequency" )
z2 = np.polyfit (x_degree ,y_degree , 8)
p2 = np.poly1d(z2)
yvals=p2(x_degree )
plt.plot(x_degree ,y_degree ,"o",label='original values' )
plt.plot(x_degree , yvals, 'r',label='polyfit values' )
plt.show()
#plt.savefig("../pig2.png")

#########Degree vs Prefix #############
x3 = []
y3 = []

for s in asn_ip:	
	if(s in asn_adj ):
		if(len(asn_adj)!=0):
			x3.append(len(asn_adj[s]))
			y3.append(len(asn_ip[s]))

dic3 = {}
for i in range(len(x3)):
	tmp = x3[i]
	if(tmp in dic3):
		dic3[tmp] += y3[i]
	else:
		dic3[tmp] = y3[i]

dic4 = Counter(x3)
x4 = [0]*len(dic4)
y4 = [0]*len(dic4)
index = 0
for i in dic4:
	x4[index] = i
	if(i in dic3):
		dic3[i] = dic3[i]/dic4[i]
		y4[index] = dic3[i]
	index += 1

x4 = np.log(x4)
y4 = np.log(y4)
z3 = np.polyfit(x4, y4, 6)

x4_new = np.linspace(0,x4.max(),300)
p3 = np.polyval(z3,x4_new)
plt.figure()
plt.title('degree-prefix')
plt.xlim(0,x4.max())
# plt.ylim(0,y3.max())
plt.xlabel('degree')
plt.ylabel('prefix')
plt.scatter(x4,y4,label = "huitu3")
plt.plot(x4_new,p3,color = 'red')
plt.show()
'''
#########Degree vs Prefix #############
adj_dict = {}
for asn in asn_adj.keys():
    if adj_dict.has_key(len(asn_adj[asn])):
        adj_dict[len(asn_adj[asn])].add(asn)
    else:
        adj_dict[len(asn_adj[asn])]=set()
        adj_dict[len(asn_adj[asn])].add(asn)

y_list=[]
for asn in adj_dict.values():
    num = float(0)
    for asn_tmp in list(asn):
        if asn_ip.has_key(asn_tmp):
            num += len(asn_ip[asn_tmp])
    y_list.append(num/len(asn))
x_list = adj_dict.keys()
#print x_list
#print y_list

x_degree = np.log([i for i in x_list])
y_degree = np.log([i+1 for i in y_list])

plt.figure(1)
plt.title("Degree vs Prefix(log-log)" )
plt.xlabel("Degree" )
plt.ylabel("Frequency" )
z3 = np.polyfit (x_degree ,y_degree , 3)
p3 = np.poly1d(z3)
yvals=p3(x_degree )
plt.plot(x_degree ,y_degree ,"o",label='original values' )
plt.plot(x_degree , yvals, 'r',label='polyfit values' )
plt.show()

'''

'''
#########Degree vs Prefix #############
d = dict()
for asn in asn_ip.keys():
    d[len(asn_ip[asn])] = len(asn_adj[asn])
x_list = d.keys()
x_list.sort()
y_list = []
for x in list(x_list):
    y_list.append(d[x])

x_degree = np.log(x_list)
y_degree = np.log(y_list)

plt.figure(3)
plt.title("Degree vs Prefix(log-log)" )
plt.xlabel("Degree" )
plt.ylabel("Frequency" )
z3 = np.polyfit (x_degree ,y_degree , 3)
p3 = np.poly1d(z3)
yvals=p3(x_degree )
plt.plot(x_degree ,y_degree ,"o",label='original values' )
plt.plot(x_degree , yvals, 'r',label='polyfit values' )
plt.show()
#plt.savefig("../pig3.png")
'''
