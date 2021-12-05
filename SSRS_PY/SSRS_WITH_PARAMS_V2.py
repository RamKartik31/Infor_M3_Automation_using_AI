#https://github.com/FRReinert/PySSRS/releases
# -*- coding: utf-8 -*-
# ITS A WORKING CODE
#import connection_data as d
#import context
#import os
from SSRS import SSRS


Service = 'http://cuspxk2o.carcgl.com/ReportServer_M3SQLRPTTST/reportservice2010.asmx?wsdl'
Execution = 'http://cuspxk2o.carcgl.com/ReportServer_M3SQLRPTTST/ReportExecution2005.asmx?wsdl'
User = 'carcgl\\chg0581'
passw = 'CARFEB2021*12345'

RS = SSRS(Service, Execution, User, passw)

'''
Part 1
    This Section will load the report and it's data
    you can get parameters data, page size, and every info from it
'''
try:
    Report = RS.RequestReport(path='/IPAD_REPORTS_SANDBOX/transfer form')

except BaseException as e:
    print('Error loadint report: %s' % str(e))


'''
Part 2
    This section will use the pre-loaded data to render the report
'''
try:
    # Put the parameters into a dictionary
    Parameters = {
        'FACILITY' : '101',
        'SUPPLIER' : 'Movincool' 
    }
    
    RenderedReport = RS.RenderReport(LoadedReport=Report, format='PDF', parameters=Parameters)

except BaseException as e:
    print('Error rendering report: %s' % str(e))


# This block will return all the information that SSRS can handle
for k, v in RenderedReport.items():
    if k == 'Result':
        pass
    
    else:
        print(k,': ',v)

'''
This block will render the report into a file
But you can use it in Django/Flask Request, for example...
    
    <> IMPORTANT - If you want to render a file <>
    Compiled files like PDF, Word, Excel should use "wb" on the file opening
    Text based files (xml, html...) are "OK" to use the "w" mode 
'''
        
#filename = os.path.join(os.path.dirname(__file__),'report'+ '.' + RenderedReport['Extension'])
filename=r'C:\Users\suren\OneDrive\Surface_Backup\RK\RK_work\Python_scripts\\SSRS_PY\SSRS_OUTPUT2.PDF'
fopen = open(filename, 'wb')
fopen.write(RenderedReport['Result'])
    
    
