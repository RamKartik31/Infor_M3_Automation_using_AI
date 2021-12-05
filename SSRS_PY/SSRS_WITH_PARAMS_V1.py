#https://pypi.org/project/sspyrs/
import requests
from requests_ntlm import HttpNtlmAuth

#reporturl = 'http://cuspxk2o.utccgl.com/Reports/Pages/Report.aspx?ItemPath=%2fIPAD_REPORTS_SANDBOX%2fsample+report'
#reporturl = 'http://cuspxk2o.utccgl.com/Reports/Pages/Report.aspx?ItemPath=%2fIPAD_REPORTS_SANDBOX%2f1096'
reporturl ='http://cuspxk2o.utccgl.com/Reports/Pages/Report.aspx?ItemPath=%2fIPAD_REPORTS_SANDBOX%2ftransfer+form'
output_file = r'C:\Users\suren\OneDrive\Surface_Backup\RK\RK_work\Python_scripts\SSRS_OUTPUT'


import sspyrs
from requests_ntlm import HttpNtlmAuth
User = 'carcgl\\chg0581'
passw = 'CARFEB2021*12345'
#params_multi  = {'FACILITY': '101','STARTDATE':'03/03/2021','ENDDATE':'04/04/2021'}
params_multi  = {'FACILITY': '101-BOSTON','MODEL SELECTED':'Movincool'}
myrpt = sspyrs.report(reporturl,User,passw,parameters=params_multi )
myrpt.directdown(output_file, 'PDF')



