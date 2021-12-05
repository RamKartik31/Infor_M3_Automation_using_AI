#import mysql.connector
import pyodbc 

# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port

server = '##############'
database = '##############'
username = '##############'
password = '##############'
conStr = 'DRIVER={SQL Server Native Client 11.0};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password
#print(conStr)

cnxn = pyodbc.connect(conStr)
cursor = cnxn.cursor()

ContractNumber =input(str("Enter Contract Number: "))
SQL_FETCH_HEADER = "SELECT BHASTH,BHASTL,BHAHLD FROM MVXJDTA.STAGHE WHERE BHCONO = '909' AND BHAGNB = '"+ContractNumber+"'"
SQL_UPDATE_HEADER = "UPDATE MVXJDTA.STAGHE SET BHASTH = '05',BHAHLD='' WHERE BHCONO = 909 AND BHAGNB = '"+ContractNumber+"'"
SQL_FETCH_LINE = "SELECT BLPONR,BLASTH,BLCUPL,BLPYNO,case when BLCUPL=BLPYNO then 'good' else 'bad' end  FROM MVXJDTA.STAGLI WHERE BLCONO = 909 AND BLAGNB = 'P443585'"
SQL_UPDATE_LINE = "UPDATE MVXJDTA.STAGLI SET BLASTH = '05' WHERE BLCONO = 909 AND BLAGNB = 'P441632' AND BLASTH='12'"

cursor.execute(SQL_FETCH_HEADER)
HEADER_DATA = cursor.fetchone()
while HEADER_DATA:
	print('loop')
	print(HEADER_DATA[0])
	HEADER_DATA = cursor.fetchone()

if HEADER_DATA[1]==12:
	cursor.execute(SQL_UPDATE_HEADER)

cursor.execute(SQL_FETCH_LINE)
if BHASTH==12:
	cursor.execute(SQL_UPDATE_LINE)
	LINE_DATA = cursor.fetchone()
	

'''
while data:
    print('loop')
    print(data[0])
    data = cursor.fetchone()
'''