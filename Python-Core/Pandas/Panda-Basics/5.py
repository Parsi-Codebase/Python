# Simple Analysis example
import pandas as pd
data={
    'Name':['Akhil','Kiran','Ravi','Meena'],
    'Maths':[89,98,87,97],
    'Science':[88,78,89,90]
}
df=pd.DataFrame(data);
print(df)
df['Total']=df['Maths']+df['Science'] # add total column
print(df)
df['Avg']=df['Total']/2 # add Avg column
print(df)
# add/export to csv file
df.to_csv('output.csv',index=False)
output=pd.read_csv('output.csv')
print(output)