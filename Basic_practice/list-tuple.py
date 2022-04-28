#coding=UTF-8
#有序可變動列表List
#grades=[12,60,15,70,90]
#grades[1:4]=[] #連續刪除列表中從1到編號4(不包含)
#grades=grades+[12,33]
#length=len(grades) #取得列表長度 len(列表長度)
#print(length)
#grades[0]=55 #把55放到列表第一個位置
#print(grades[1:4])
#data=[[3,4,5],[6,7,8]]
#print(data)
#data[0][0:1]=[5,5,5]
#print(data)
#有序不可變動列表 Tuple
data=(3,4,5)
data[0]=5 #錯誤: Tuple 的資料不可變動
print(data)