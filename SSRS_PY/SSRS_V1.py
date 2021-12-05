import requests
from requests_ntlm import HttpNtlmAuth

reporturl = 'http://cuspxk2o.utccgl.com/Reports/Pages/Report.aspx?ItemPath=%2fIPAD_REPORTS_SANDBOX%2fsample+report'
output_file = r'C:\Users\suren\OneDrive\Surface_Backup\RK\RK_work\Python_scripts\File.html'


session = requests.Session()
session.auth = HttpNtlmAuth('carcgl\\chg0581','CARFEB2021*12345')
response = session.get(reporturl,stream=True)
print (response.status_code)
#print (response.content)
with open(output_file,'wb') as pdf:
    for chunk in response.iter_content(chunk_size=100000):
        if chunk:
            pdf.write(chunk)
session.close()


