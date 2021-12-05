import pandas as pd

file1 = pd.read_csv (r'C:\Users\suren\OneDrive\Surface_Backup\RK\RK_work\Python_scripts\EMPLOYEE_TERMINATION\HVAC Commercial Service Terminations_37_3484279927206886878_V2.csv')
df1 = pd.DataFrame(file1, columns= ['EMPLID','BU'])
# print (df)
# print (type(df))

file1_data_list = df1.values.tolist()
print (type(file1_data_list))

Empl_ID = []
for ele in file1_data_list:
    # print(ele)
    if ele[1] == 'HVAC RENTAL SYSTEMS SPOT' or ele[1] == 'HVAC RENTAL SYSTEMS NA':
        # print(ele[0])
        Empl_ID.append(ele[0])
        
print(Empl_ID)
Empl_ID_list_string = map(str, Empl_ID) 
data = list(Empl_ID_list_string)
        
file2 = pd.read_csv ('4.20.2021_ALLUsers_Carcgl.csv', low_memory=False)
df2 = pd.DataFrame(file2, columns= ['utc-com-1987-LDAP-WorkDayEmployeeID'])

key = 3035745
def checkIfValuesExists1(df2, listOfValues):
    ''' Check if given elements exists in dictionary or not.
        It returns a dictionary of elements as key and thier existence value as bool'''
    resultDict = {}
    # Iterate over the list of elements one by one
    for elem in listOfValues:
        # Check if the element exists in dataframe values
        if elem in df2.values:
            resultDict[elem] = True
        else:
            resultDict[elem] = False
    # Returns a dictionary of values & thier existence flag        
    return resultDict
    
# Check if given values exists in the DataFrame or not
result = checkIfValuesExists1(df2, Empl_ID)
print('Dictionary representing if the given keys exists in DataFrame or not : ')
print(result)