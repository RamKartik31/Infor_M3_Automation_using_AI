#https://pypi.org/project/sspyrs/

reporturl = 'http://cuspxk2o.utccgl.com/Reports/Pages/Report.aspx?ItemPath=%2fIPAD_REPORTS_SANDBOX%2fsample+report'
output_file = r'C:\Users\suren\OneDrive\Surface_Backup\RK\RK_work\Python_scripts\SSRS_OUTPUT'


import sspyrs
myrpt = sspyrs.report(reporturl,'carcgl\\chg0581','CARFEB2021*12345')
myrpt.directdown(output_file, 'Excel')



