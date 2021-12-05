import pandas as pd
empIDs=[]
ADIDs=[]

def check_if_string_in_file(file_name, string_to_search):
    """ Check if any line in the file contains given string """
    # Open the file in read only mode
    string_to_search_formatted = string_to_search[0:(len(string_to_search)-2)]
    print(string_to_search_formatted)
    #print("string_to_search"+str(int(string_to_search)))
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            if string_to_search_formatted in line:
                print(line)
                return True
    return False
def getADID(file_path,col_names, col_value):
    print("EMP ID:"+str(col_value))
    file = pd.read_csv (file_path, low_memory=False)
    df2 = pd.DataFrame(file, columns= col_names)
    column_data = df2.values.tolist()
    print(len(column_data))
    for values in column_data:
     #print(str(values[0])+'--'+str(values[1]))
     if col_value == values[0]:
       print(values[1])
       
def getEmployeeID(file_path,col_names, col_value):
    file = pd.read_csv (file_path, low_memory=False)
    df2 = pd.DataFrame(file, columns= col_names)
    column_data = df2.values.tolist()
    #print(column_data)
    for values in column_data:
     #print(str(values[0])+'--'+str(values[1]))
     if col_value == values[1]:
       #print(str(values[0]))
       empIDs.append(values[0])
       #getADID('4.20.2021_ALLUsers_Carcgl.csv',['utc-com-1987-LDAP-WorkDayEmployeeID','samaccountname'],values[0])
       check_if_string_in_file('HVAC Commercial Service Terminations_35_6607410730003451005.csv',str(values[0]))



       
getEmployeeID('HR_FILE.csv',['EMPLID','BU'],'HVAC RENTAL SYSTEMS SPOT')
getEmployeeID('HR_FILE.csv',['EMPLID','BU'],'HVAC RENTAL SYSTEMS NA')

#check_if_string_in_file('4.20.2021_ALLUsers_Carcgl.csv','224333')

