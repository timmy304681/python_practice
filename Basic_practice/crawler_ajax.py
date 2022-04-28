#抓取Medim.COM的文章
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import urllib.request as req
url='https://medium.com/_/api/home-feed'
#建立一個request物件，附加request headers的資訊
request=req.Request(url,headers={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
})


with req.urlopen(request) as response:
    data=response.read().decode('utf-8')   #根據觀察，取得的資料是JSON格式
#print(data)

#解析JSON，取得每篇文章的標題
import json
data=data.replace('])}while(1);</x>','')
data=json.loads(data) #把資料解析成字典/列表的表示形式
#取得json資料中文章標題
posts=data['payload']['references']['Post']
for key in posts:  
    post=posts[key]
    print(post['title'])
