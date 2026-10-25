import pandas as pd
#custome index
data=[10,20,30,40,59]
index_labels=['a','b','c','d','e']
s=pd.Series(data,index=index_labels)
print(s)
s=pd.Series([10,20,30],index=['pen','pencil','book'])
print(s)
# access pen price
# access like dictionary
print(s['pen'])