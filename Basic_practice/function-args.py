#參數的預設資料
#def power(base,exp=0):
 #  print(base**exp)

#power(3,2)
#power(3)
#參數的名稱對應
# def divide(n1,n2):
#     print(n1/n2)

# divide(n1=50,n2=5)

#無限參數資料
def avg(*ns):
    sum=0
    for n in ns:
        sum=sum+n
    print(sum/len(ns))

avg(1,3)
avg(1,3,6)
avg(1,3,7,8)