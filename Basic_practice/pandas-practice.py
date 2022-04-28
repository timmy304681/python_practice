#import pandas module
import pandas as pd
#create Series
data=pd.Series([20,10,15])
#normal Series run
# print(data)
# print("Max",data.max())
# print("Medium",data.median())
# data=data*2
# print(data)
# data=data==20 #contrast with 20
# print(data)


#create DataFrame
data=pd.DataFrame({
    "name":["Amy","Timmy","Bacon"],
    "salary":["30000","80000","50000"]
})

#print(data)
#Get specific column
print(data["name"])
#Get specific row
print("============================")
print(data.iloc[0]) #print first row



