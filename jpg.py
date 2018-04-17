# -*- coding: utf-8 -*-
import requests
import os
url = "http://b143.photo.store.qq.com/psb?/V13Nef3z3m4nTv/x6xZKOXVB*WWz3Uo2IJIo2QtYVj6B.7l8.Az00H1EL4!/b/dI8AAAAAAAAA&bo=OASABwAAAAAFAJg!&rf=viewer_4.jpg"
root = "E://picture//"
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已经存在")
except:
    print("爬取失败")
