#網路連線
# import urllib.request as request
# src="https://www.ntu.edu.tw"
# with request.urlopen(src) as response:
#     data=response.read().decode("utf-8")
# print(data)


import urllib.request as request
import json
src="https://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid=cf6540e6-4df2-4afa-a71c-c6efdf62318d"
#臺北捷運全系統旅運量統計，發現資料室json格式
with request.urlopen(src) as response:
    data=json.load(response)
#將公司名稱列出來
clist=data["result"]["results"]
with open("MRT.txt","w", encoding="utf-8") as file:
    for day in clist:
        file.write(day["營運日"]+'\n')
