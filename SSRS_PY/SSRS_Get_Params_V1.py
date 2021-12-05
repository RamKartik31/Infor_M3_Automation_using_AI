#https://github.com/FRReinert/PySSRS/releases
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import connection_data as d
# import context
from SSRS import SSRS


Service = 'http://cuspxk2o.carcgl.com/ReportServer_M3SQLRPTTST/reportservice2010.asmx?wsdl'
Execution = 'http://cuspxk2o.carcgl.com/ReportServer_M3SQLRPTTST/ReportExecution2005.asmx?wsdl'
User = 'carcgl\\chg0581'
passw = 'CARFEB2021*12345'

RS = SSRS(Service, Execution, User, passw)
#Methods = RS.ListMethods()
result  = RS.GetParameters(path='/IPAD_REPORTS_SANDBOX/1096')
Report = RS.RequestReport(path='/IPAD_REPORTS_SANDBOX/1096')

parameters_list=[]
for key, value in result.items() :
    # print('Name:', key)
    
    # for key2, value2 in value.items():
        # print(key2,':', value2)
    # if key=='Name:':
        # print(value)
    
    if key!='Type':
       # print(key) 
       parameters_list.append(key)
    # print('\n')
print('param list')
print(parameters_list)

n = len(parameters_list)
print(n)

n=len(parameters_list)
parameters_values=[]
input_string = input("Enter parameters_values separated by comma ")
parameters_values  = input_string.split(",")
print('param values')
parameters_dict=dict(zip(parameters_list, parameters_values))
print('param dic')
print(parameters_dict)

try:
    RenderedReport = RS.RenderReport(LoadedReport=Report, format='EXCEL', parameters=parameters_dict)
    print(type(RenderedReport))

except BaseException as e:
    print('Error rendering report: %s' % str(e))

print(RenderedReport['Extension'])

for k, v in RenderedReport.items():
    if k == 'Result':
        pass
    
    else:
        print(k,': ',v)

filename=r'C:\Users\suren\OneDrive\Surface_Backup\RK\RK_work\Python_scripts\\SSRS_PY\SSRS_OUTPUT_MAR.xls'
fopen = open(filename, 'wb')
fopen.write(RenderedReport['Result'])







