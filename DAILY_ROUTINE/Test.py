import pandas

excel_data_df = pandas.read_excel('DAILY_ROUTINE_SQLS.xlsx', 'Sheet1')
# print(excel_data_df[0])
File_Name = excel_data_df['File_Name'].tolist()
SQL = excel_data_df['SQL'].tolist()

# print(File_Name)
# print(SQL)

res = list(dict(zip(File_Name, SQL)))
  
# Printing resultant dictionary 
print ("Resultant dictionary is : " +  str(res))
print(res[0])