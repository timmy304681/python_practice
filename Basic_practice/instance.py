#上篇
#POINT實體物件的設計：平面座標上的點
#####__init__ <<<<兩個_
# class Point:
#     def __init__(self,x,y): 
#         self.x=x
#         self.y=y
# #建立第一個實體物件
# p1=Point(3,4)
# print(p1.x,p1.y)
# #建立第二個實體物件
# p2=Point(5,6)
# print(p2.x,p2.y)


# #FullName實體物件的設計：分開記錄姓，名資料的全名
# class FullName:
#     def __init__(self,first, last):
#         self.first=first
#         self.last=last

# name1=FullName("Y","Cheng")
# print(name1.first, name1.last)


###下篇
# class Point:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#     #定義實體方法：
#     def show(self):
#         print(self.x,self.y)
#     def distance(self,targetx,targety):
#          return (((self.x-targetx)**2+(self.y-targety)**2)**0.5)
# p1=Point(3,4)
# p1.show() #呼叫實體方法/函式
# result=p1.distance(0,0) #計算3,4和0,0之間距離
# print(result)


#File 實體物件的設計：包含檔案讀取的程式
class File:
    def __init__(self,name):
        self.name=name
        self.file=None #未開啟檔案：初始是 None
    def open(self):
        self.file=open(self.name,mode='r',encoding='utf-8')
    def read(self):
        return self.file.read()
#讀取檔案一
f1=File('MRT.txt')
f1.open()
data=f1.read()
print(data)
#讀取檔案二
f2=File('data.txt')
f2.open()
data=f2.read()
print(data)
