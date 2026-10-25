# basic operations
import pandas as pd
data={
    'Name':['Akhil','Kiran','Ravi','Meena'],
    'Maths':[89,98,87,97],
    'Science':[88,78,89,90]
}
df=pd.DataFrame(data)
print(df.head()) # First 5 rows
print(df.info()) # Info about datatypes
print(df.shape) #(rows,columns)
print(df.describe()) # Summary statistics (for numbers)