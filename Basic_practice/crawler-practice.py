import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import urllib.request
url='https://forum.gamer.com.tw/B.php?bsn=31078'
request=urllib.request.Request(url,headers={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
})
with urllib.request.urlopen(request) as response:
    data=response.read().decode('utf-8')
#print(data)

import bs4 
root=bs4.BeautifulSoup(data,'html.parser')
#print(root)
td=root.find_all('td',class_='b-list__main')
p=root.find_all('p',class_='b-list__main__title')

for title in p:
    print(title.string)