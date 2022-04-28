#隨機模組
#import random
#隨機選取
# data=random.sample([1,2,4,6,10,20], 3)
# print(data)
#隨機調換順序
# data=[1,5,6,20]
# random.shuffle(data)
# print(data)
#隨機取得亂數
# data=random.uniform(60,100)
# print(data)
#取得常態分配亂數
#平均數100，標準差10，得到的資料[多數]在90-110之間
# data=random.normalvariate(100,10)
# print(data)


#統計模組
import statistics as stat
data=stat.stdev([1,4,6,7,8,10])
print(data)

#平均數、中位數、標準差、常態分佈