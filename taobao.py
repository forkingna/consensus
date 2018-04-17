import re
import requests
from bs4 import BeautifulSoup
def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)#时间超过30s就会报错
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

def goodsList(html, infolist):#"view_price":"79.00
                              #"raw_title":"卡拉羊双肩包女生韩版小学生初中生书包中学生休闲旅行背包学院风"
    try:
        pricelt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)#\ 代表将后面的字符处理为特殊字符 \n 代表换行符
        titlelt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        for i in range(len(pricelt)):
            price = eval(pricelt[i].split(":")[1])#eval 可以将字符串转列表 字符串转字典 字符串转元祖
            title = eval(titlelt[i].split(":")[1])
            infolist.append([ price, title])
    except:
        print("")

def printGoodsList(infolist):
    tplt = "{:^4}\t{:^8}\t{:^16}"
    print (tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in infolist:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))
    return ""

def main():
    start_url = "https://s.taobao.com/search?q="
    goods = "书包"
    depth = 2
    infoList = []
    for i in range(depth):
        try:
            url = start_url + goods + '&s=' + str(i*44)
            html = getHTMLText(url)
            goodsList(html, infoList)
        except :
            continue
    printGoodsList(infoList)
main()




