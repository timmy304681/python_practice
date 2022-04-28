#抓取PTT電影版的網頁原始碼(HTML)
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import urllib.request as req
url='https://www.ptt.cc/bbs/movie/index.html'
#建立一個request物件，附加request headers的資訊
request=req.Request(url,headers={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
})


with req.urlopen(request) as response:
    data=response.read().decode('utf-8')
#print(data)

#解析原始碼，取得每篇文章的標題
import bs4
root=bs4.BeautifulSoup(data,'html.parser')
#print(root.title)
titles=root.find_all('div',class_='title')#尋找clas='title的div標籤
#print(titles)
for title in titles:
     if title.a !=None: #如果a不是None，則印出來
         print(title.a.string)