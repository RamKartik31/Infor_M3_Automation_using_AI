import pandas as pd
import numpy as np

Empl_ID = [216000,260815,291967,214195]


print(Empl_ID)
print('------------------------------------------------------------')
        
file2 = pd.read_csv ('4.20.2021_ALLUsers_Carcgl.csv', chunksize=10000)
df2 = pd.concat(file2)
chunk = pd.DataFrame(df2, columns= ['utc-com-1987-LDAP-WorkDayEmployeeID', 'samaccountname'])
chunk_without_na = chunk.dropna()
# print(chunk_without_na)
# print(type(chunk_without_na))
chunk_list = chunk_without_na.values.tolist()
# print(chunk_list)

emp_list = [df2.columns.values.tolist()] + chunk_list
f = '{:<8}|{:<15}' # formatting
result = []
emp_str_from_df = []

print('Emp details from 4.20.2021_ALLUsers_Carcgl.csv')
for i in emp_list:
    result = f.format(*i)
    # print(result)
    # print(type(result))
    emp_str_from_df = result[0:7]
    # print(emp_str_from_df)
    for id in Empl_ID:
        if str(id) in emp_str_from_df:
            print(str(id) + ' '+ result[9:])
         
