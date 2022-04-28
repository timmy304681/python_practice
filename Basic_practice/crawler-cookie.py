#抓取PTT八卦版的網頁原始碼(HTML)
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import urllib.request as req

def getData(url):
    #建立一個request物件，附加request headers的資訊
    request=req.Request(url,headers={
        'cookie':'over18=1',
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

    #抓取上一頁的連結
    nextLink=root.find('a',string='‹ 上頁') #找到內文是上頁的a標籤
    return nextLink['href']

pageURL='https://www.ptt.cc/bbs/Gossiping/index.html'
pageURL='https://www.ptt.cc'+getData(pageURL)
print(pageURL)
count=0
while count<3:
    pageURL='https://www.ptt.cc'+getData(pageURL)
    count+=1