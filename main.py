#1st
import numpy as np
from utils import *
data={'Name':['Bhavya','Dhanu','Sindhu'],
      'Age':[22,19,20]}
df=pd.DataFrame(data)
print(df)
df=add_column(df,'Dept',['HR','MR','HR'])
df=add_column(df,'Review',[50,70,30])
print(df)
df=remove_column(df,'Age')
print(df)
df=filter_rows(df, 'Dept == "HR"')
print(df)
df=rename_columns(df, {'Name':'Names',
                       'Dept':'Departments'})
print(df)
print(df.head())
df=sum_column(df,'Review')
print(df)
