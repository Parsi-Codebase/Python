import pandas as pd
data={
    'Name':['Sachin','Virat','Rohith'],
    'Age':[45,34,36],
    'City':['London','Paris','Delhi']
}
df=pd.DataFrame(data)
# filter data age >34
print(df[df['Age']>34])
filtered=df[df['Age']>34] # storing filtered data in variable
print(filtered)
# add column
df['Profession']=['cricket','football','tennies']
print(df)
# drop column
df.drop('Profession',axis=1,inplace=True) # axis=1 means column and inplace=True means change will be reflected in original df
print(df)