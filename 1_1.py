import pandas as pd 
import numpy as np
df=pd.read_csv("dataset_Facebook.csv",delimiter=";")
df

subset1=df[['Type','Category','Post Month',]]
print(subset1.head(10))

subset2=df[['Type','Post Hour','like',]]
print(subset2.head(10))

merged= pd.concat([subset1,subset2],axis=1)
merged

sorted1=df.sort_values(by=['like'],ascending=True)
sorted1

sorted1.T

df.shape

arr=np.array(df[['Post Month','Post Weekday']].head(6))
arr

reshape=arr.reshape(3,4)
reshape
