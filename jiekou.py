# coding: utf-8 
"""
import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView

class Render(QWebEngineView):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebEngineView.__init__(self)
        self.loadFinished.connect(self._loadFinished)
        self.load(QUrl(url))
        self.app.exec_()

    def _loadFinished(self, result):
        # This is an async call, you need to wait for this
        # to be called before closing the app
        self.page().toHtml(self.callable)

    def callable(self, data):
        self.html = data
        # Data has been stored, it's safe to quit the app
        self.app.quit()



import lxml.html

#定义一个网页地址
url = 'https://www.baidu.com'

r = Render(url)
result = r.html
tree = lxml.html.fromstring(result)

"""




"""
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
def render(source_html):

    class Render(QWebEngineView):
        def __init__(self, html):
            self.html = None
            self.app = QApplication(sys.argv)
            QWebEngineView.__init__(self)
            self.loadFinished.connect(self._loadFinished)
            self.setHtml(html)
            self.app.exec_()

        def _loadFinished(self, result):
            # what's going on here? how can I get the HTML from toHtml?
            self.page().toHtml(self.callable)
            self.app.quit()

        def callable(self, data):
            self.html = data

    return Render(source_html).html
print(render("http://www.widlabs.com"))
"""




"""
import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView
app = QApplication(sys.argv)
browser = QWebEngineView()
browser.load(QUrl("http://www.widlabs.com/"))

browser.page().toHtml(this._callable)

browser.show()
app.exec_()
"""




"""  
import sys  
from PyQt5.QtCore import *  
from PyQt5.QtWidgets import *  
from PyQt5.QtGui import *  
from PyQt5.QtWebEngineWidgets import *  
  
class MainWindow(QMainWindow):  
    def __init__(self, *args, **kwargs):  
    super().__init__(*args, **kwargs)  
    self.setWindowTitle("client")  
    self.setWindowIcon(QIcon('icons/icon.png'))  
    self.resize(900, 600)  
    self.show()  
  
    self.browser = QWebEngineView()  
    url = 'https://www.baidu.com'  
    self.browser.load(QUrl(url))  
    self.setCentralWidget(self.browser)  
  
if __name__=='__main__':  
    app = QApplication(sys.argv)  
    window = MainWindow()  
    window.show()  
    sys.exit(app.exec_())  
"""





"""
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
#from PyQt5.QtWebKitWidgets import QWebView
from PyQt5.QtCore import QEventLoop
#import lxml.html
from bs4 import BeautifulSoup
from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView
url = 'https://zhuanlan.zhihu.com/p/27363298'

app = QApplication([])
webview = QWebEngineView()
loop = QEventLoop()

webview.loadFinished.connect(loop.quit)
webview.load(QUrl(url))
loop.exec_()
html = webview.page().mainFrame().toHtml()
#tree = lxml.html.fromstring(html)
#fixed_html = lxml.html.tostring(tree, pretty_print=True)
soup = BeautifulSoup(html, 'html.parser')
fixed_html = soup.prettify()
title = soup.find(class_="PostIndex-title av-paddingSide av-titleFont")
#print(fixed_html)
"""




"""
import sys,re
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
 
 
p = re.compile(r'<a class="J_AtpLog" href="(.*)" title')
 
fp = open('deatailUrl.txt','a+')
class Render(QWebPage):  
  def __init__(self, url):  
    self.app = QApplication(sys.argv)  
    QWebPage.__init__(self)  
    self.loadFinished.connect(self._loadFinished)  
    self.mainFrame().load(QUrl(url))  
    self.app.exec_()  
   
  def _loadFinished(self, result):  
    self.frame = self.mainFrame()  
    self.app.quit()  
 
if __name__=='__main__':
   
  r = Render(sys.argv[1])
##  r = Render(r'http://list.taobao.com/itemlist/default.htm?spm=a2106.2206569.0.0.Ou8oRH&cat=51108009')
  html = r.frame.toHtml()
  result = p.findall(html)
  i = 0
  for uri in result:
    i+=1
    print(uri,file = fp)
##  print(i)
fp.close()
"""



'''
from PyQt5.QtCore import QEventLoop,QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication
import sys
import PyQt5
webView.page().currentFrame().documentElement().toInnerXml()
'''


"""
class Render(QWebEngineView):
    #Render HTML with PyQt5 WebEngine.

    def __init__(self, html):
        self.html = None
        self.app = QApplication(sys.argv)
        QWebEngineView.__init__(self)
        self.loadFinished.connect(self._loadFinished)
#         self.setHtml(html)
        self.load(QUrl(html))
        while self.html is None:
            self.app.processEvents(
                QEventLoop.ExcludeUserInputEvents |
                QEventLoop.ExcludeSocketNotifiers |
                QEventLoop.WaitForMoreEvents)
        self.app.quit()
        
    def _callable(self, data):
#         print(data)
        self.html = data
        
    def _loadFinished(self, result):
        self.page().toHtml(self._callable)

r=Render('http://www.eefung.com/search.html?s=13607004796980319409&entry=1&q=%E5%8C%BB%E6%82%A3%E5%85%B3%E7%B3%BB')
html = r.html  
print(html) 
"""


"""
"""
from aip import AipNlp
import urllib.request
import urllib.parse
import json
"""
with open('Untitled-2.json', 'r') as f:
    data = json.load(f)
print(data["result"]["cmntlist"][1]["content"])

"""



APP_ID = '11093674'
API_KEY = '48ggC2n9icnpX4iQnceFOaVK'
SECRET_KEY = 'WKQLbR46GwowaQyD3WPUdG4mEezlTq7n'

#client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
f = open("news.txt", "r")

str_list =[]
for line in f.readlines():
    line = line.strip()
    str_list.append(line)
text = " ".join(str_list)



client = AipNlp(APP_ID, API_KEY, SECRET_KEY)
#text = "我真的心寒，不止在一个评论下面看到了劝人学医，天打雷劈。我当初就不应该想不开学医，以及那些说医院黑的，我不否认没有医黑，但是都黑吗？如果觉得都黑你们就不用来医院了，刚好我们少伺候点人，我特么血压天天量到想吐，还经历各种白眼，说我们医院乱收钱，什么错了都怪医院，干的真的很好。有时候看到这种新闻，抬头看着我书架子上满满的医书，我在想，要不要现在就放弃了，可是想起老师他们在学校说的，我们的职业……算了，真的心寒，谁还把我们当白衣天使？各个都当伸手要钱的魔鬼罢收
#text = line#"我真的心寒，不止在一个评论下面看到了劝人学医，天打雷劈。"
text = """医闹就是恶劣的行为！别的病人还需要医生！如果其他病人因为这样得不到及时治疗是不是你们医闹的家属负责！一律走司法程序！尸检是医疗事故就让医院赔！不然就接受事实！让死者安息！"""
res=client.sentimentClassify(text)

jsonstr = json.dumps(res, indent=1)
print(res)


