import pandas as pd
#data index
data=pd.Series([5,2,1,-4,7],index=['a','b','c','d','e'])
#print(data)

#observe data
# print('data type',data.dtype)
# print('data number',data.size)
# print('data index',data.index)

#obtain data: from sort,from index
# print("data from sort",data[2],data[0]) #get 3rd & 1st data
# print('data from index',data["e"])

#number caculation : 
# print("Max",data.max())
# print("sum",data.sum())
# print("Median",data.median())
# print("std",data.std())
# print('top 3',data.nlargest(3))

data=pd.Series(['Apple',"Tesla","Disney"])

#string caculation : normal, combine , search , replace
print(data.str.lower()) #小寫
print(data.str.len())  #calculate length
print(data.str.cat(sep='-')) #combine strings

print(data.str.contains("A")) #
print(data.str.replace("Apple","Banana"))
