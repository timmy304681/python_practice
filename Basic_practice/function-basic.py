#定義函式
#函式內部的程式碼，若是沒有做函式呼叫，就不會執行
#def multiply(n1,n2):
 #   return n1*n2
#呼叫函式
#value=multiply(3,4)+multiply(5,10)
#print(value)
#multiply(5,10)
#multiply(8,10)

#程式包裝:同樣程式邏輯重複利用
def wow(max):
    sum=0
    for n in range(1,max+1):
        sum=sum+n
    print(sum)

wow(10)
