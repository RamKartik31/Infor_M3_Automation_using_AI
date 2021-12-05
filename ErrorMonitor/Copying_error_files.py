import os
import shutil
from os.path import join, getsize
from datetime import datetime, date, time, timedelta

sourceDir = 'C:\\Users\\suren\\OneDrive\\Surface_Backup\\RK\\RK_work\\Python_scripts\\ErrorMonitor\\Folder_2_Monitor'
destDir = 'C:\\Users\\suren\\OneDrive\\Surface_Backup\\RK\\RK_work\\Python_scripts\\ErrorMonitor\\Files_2_process'
  
# Returns the current local date 
today = datetime.today()
# print(type(today))
print("Today date is: ", today)
log_days_num = int(input("Enter no of days past to run the log files: "))
for root, dirs, files in os.walk(sourceDir):
    for file in files:
        sourceFile=os.path.join(sourceDir,file)
        print(sourceFile)
        # print(os.path.getctime(sourceFile))
        modTimesinceEpoc = os.path.getmtime(sourceFile)
        modificationTime = datetime.fromtimestamp(modTimesinceEpoc).strftime('%Y-%m-%d %H:%M:%S')
        print("Last Modified Time : ", modificationTime)
        # print(type(modificationTime))
        date_time_str = modificationTime[0:10]
        # print(date_time_str)
        # Converting strings to dates
        date = datetime.strptime(date_time_str, '%Y-%m-%d')
        print(date)
        print(type(date))
        delta = (today - date).days
        print (delta)
        if delta <= log_days_num:
            shutil.copy(sourceFile, destDir)
            print("true")