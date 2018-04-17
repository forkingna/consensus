#coding = utf-8
import requests
import time
import re
from urllib import request
from bs4 import BeautifulSoup
import codecs
import pymysql as MySQLdb

def gethtml():
    res  = requests.get("http://www.eefung.com/hot-report/20180307174822").content
    soup = BeautifulSoup(res, 'html.parser')
    print(soup)
    ef_title = soup.find('div', class_='document-content')
    print(str(ef_title.get_text()))

gethtml()