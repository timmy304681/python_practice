# #儲存檔案
# file=open("data.txt", mode="w", encoding="UTF-8")  #開啟
# file.write("中文來\nSecond Line") #操作
# file.close() #關閉

# with open('data.txt', mode="w", encoding="UTF-8") as file:
#     file.write("5\n3")

#讀取檔案
#把檔案裡的數字，一行一行的讀取出來，並計算總合
# sum=0
# with open('data.txt', mode="r", encoding="UTF-8") as file:
#     for line in file:
#         sum+=int(line)
# print(sum)

#使用Json來讀取檔案
import json
with open('config.json', mode='r') as file:
    data=json.load(file)
print(data) #data是一個字典資料
data["name"]="New Name"  #修改變數中的資料

with open('config.json', mode='w') as file:
    json.dump(data, file)

