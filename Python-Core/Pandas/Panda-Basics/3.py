import pandas as pd
data={
    'Name':['Sachin','Virat','Rohith'],
    'Age':[45,34,36],
    'City':['London','Paris','Delhi']
}
print(data['Name'][0])
df=pd.DataFrame(data)
print(df)
print(df['Name']) # get a column
print(df.loc[1]) # get row by label
print(df.iloc[0,1]) #get element by position
