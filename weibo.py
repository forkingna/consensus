#coding = utf-8
import requests
import time
import re
from urllib import request
from bs4 import BeautifulSoup
import codecs
import pymysql as MySQLdb

TOPIC = "#北医三院产妇事件#"


def gethtml(id, pages):

    file_path='.\\htmls\\' + str(pages) + '.jsp'
    with codecs.open(file_path, encoding='utf-8') as f:
        txt_all = f.readlines()
    tmp = "".join(txt_all)
    soup = BeautifulSoup(tmp, 'lxml')
    # print(soup.select("screen_box"))
    db = MySQLdb.connect('localhost', 'root', '', 'consensus', charset = 'utf8')
    cursor = db.cursor()
   #id = 0
    count = 1
    #分析网页数据
    for tmp1 in soup.find_all('div', 'WB_cardwrap WB_feed_type S_bg2 WB_feed_like'):
        #删去每一页前两条微博
        count += 1
        if (id != 0) and (count==1 or count ==2):
            continue
        #获取用户名
        tmp2 = tmp1.find('div', 'WB_detail')
        tmp3 = tmp2.find('div', 'WB_info')
        wb_name = tmp3.get_text().strip()
        #获取微博时间
        tmp5 = tmp2.find('div', 'WB_from S_txt2')
        time_tmp = tmp5.find('a')
        from_tmp = time_tmp.get_text().strip()
        wb_time = from_tmp if from_tmp.find('最后评论')==-1 else from_tmp[:len(from_tmp)-5]

        wb_phone = '' if len(tmp5.find_all('a'))==1 else tmp5.find_all('a')[1].get_text().strip()
     #   print('来自:', phone_tmp)

        tmp4 = tmp2.find('div', 'WB_text W_f14')
        wb_detail = tmp4.get_text().strip()[len(TOPIC)-1+3:]
    #    print('内容:', wb_detail)

        wb_indentity=''
        if(str(tmp3).find('W_icon icon_approve')!=-1):
            wb_indentity = '个人认证'
        if(str(tmp3).find('W_icon icon_approve_co')!=-1):
            wb_indentity = '官方认证'
        if(str(tmp3).find('W_icon icon_club')!=-1):
            wb_indentity = '微博达人'
        if(str(tmp3).find('W_icon icon_approve_gold')!=-1):
            wb_indentity = '微博大V'

        try:
            tmp6 = tmp1.find_all('span', class_='line S_line1')[1].find_all('em')[1]
            wb_forward_t = tmp6.get_text() if tmp6.get_text().strip()!='转发' else '0'
            wb_forward = int(str(wb_forward_t))
        except IndexError:
            print('forward error:',pages, wb_name)
            wb_forward=0

        try:
            tmp7 = tmp1.find_all('span', class_='line S_line1')[2].find_all('em')[1]
            wb_comment_t = tmp7.get_text() if tmp7.get_text().strip()!='评论' else '0'
            wb_comment = int(str(wb_comment_t))
        except IndexError:
            print('comment error:',pages, wb_name)
            wb_comment=0

        try:
            tmp8 = tmp1.find_all('span', class_='line S_line1')[3].find_all('em')[1]
            wb_like_t = tmp8.get_text() if str(tmp8.get_text().strip()).isdigit() else '0'
            wb_like = int(str(wb_like_t))
        except IndexError:
            print('like error:',pages, wb_name)
            wb_like=0

        #单条微博信息写入数据库
        id += 1
        sql = """insert into weibo (id, name, time, phone, detail, identity, forward,
                comment, like_num)
                values(%d, '%s', '%s', '%s', '%s', '%s', '%d', '%d', '%d')"""%(
                id, wb_name, wb_time, wb_phone, wb_detail, wb_indentity, wb_forward,
                wb_comment, wb_like)

        try:       
            cursor.execute(sql)
            db.commit()
        except:
            print(pages, wb_name, sql)
            db.rollback()

       # print(count)
    return id
      
def main():
    id = 0
    for i in range(23):
      #  print(i)
        id = gethtml(id, i+1)


main()
