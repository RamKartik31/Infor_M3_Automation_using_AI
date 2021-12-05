import requests
url = 'http://cuspxk2o.utccgl.com/Reports/Pages/Report.aspx?ItemPath=%2fIPAD_REPORTS_SANDBOX%2fsample+report'

s = requests.Session()
s.post(url, data={'_username': 'carcgl\chg0581', '_password': 'CARFEB2021*12345'})

r = s.get(url)

output_file = r'C:\Users\suren\OneDrive\Surface_Backup\RK\RK_work\Python_scripts\File.txt'

downloaded_file = open(output_file, 'wb')
for chunk in r.iter_content(100000):
    downloaded_file.write(chunk)
    
