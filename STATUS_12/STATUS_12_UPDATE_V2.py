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
SQL_UPDATE_HEADER = "UPDATE MVXJDTA.STAGHE SET BHASTH = '05',BHAHLD='' WHERE BHCONO = 909 AND BHAGNB = '"+ContractNumber+"' and (BHASTH='12' or BHASTL='12')"
SQL_FETCH_LINE = "SELECT BLPONR,BLASTH,BLCUPL,BLPYNO,case when BLCUPL=BLPYNO then 'good' else 'BAD' end  FROM MVXJDTA.STAGLI WHERE BLCONO = 909 AND BLAGNB = '"+ContractNumber+"'"
SQL_UPDATE_LINE = "UPDATE MVXJDTA.STAGLI SET BLASTH = '05' WHERE BLCONO = 909 AND BLAGNB = '"+ContractNumber+"' AND BLASTH='12'"

cursor.execute(SQL_FETCH_HEADER)
HEADER_DATA = cursor.fetchone()
if HEADER_DATA:
	HEADER_BHASTH = HEADER_DATA[0]
	HEADER_BHASTL = HEADER_DATA[1]
	HEADER_BHAHLD = HEADER_DATA[2]
    
	print("HEADER_BHASTH:"+HEADER_BHASTH)
	print("HEADER_BHASTL:"+HEADER_BHASTL)
	print("HEADER_BHAHLD:"+HEADER_BHAHLD)
	HEADER_DATA = cursor.fetchone()
	if HEADER_BHASTH == '12' or HEADER_BHASTL == '12':
		print(SQL_UPDATE_HEADER)
        ch1 =input(str("To execute HEADER update stmt as shown above press y"))
        if ch1 = 'y':
            print("Update stmt executed and committed")
            #cursor.execute(SQL_UPDATE_HEADER)
            #cnxn.commit()
        else:
            print("HEADER update aborted")
	else:
		print("No need to execute Update stmt")
    
else:
    print("NO HEADER DATA")
    
print("--------------------------------")
cursor.execute(SQL_FETCH_LINE)
LINE_DATA = cursor.fetchone()
while LINE_DATA:
	LINE_BLPONR = LINE_DATA[0]
	LINE_BLASTH = LINE_DATA[1]
	LINE_BLCUPL = LINE_DATA[2]
	LINE_BLPYNO = LINE_DATA[3]
	LINE_STATUS = LINE_DATA[4]
    
	print("LINE_BLPONR:"+str(LINE_BLPONR))
	print("LINE_BLASTH:"+LINE_BLASTH)
	print("LINE_BLCUPL:"+LINE_BLCUPL)
	print("LINE_BLPYNO:"+LINE_BLPYNO)
	print("LINE_STATUS:"+LINE_STATUS)
	if LINE_BLASTH == '12':
		print(SQL_UPDATE_LINE)
        ch2 =input(str("To execute LINE update stmt as shown above press y"))
        if ch2 = 'y':
            print("LINE Update stmt executed and committed")
            #cursor.execute(SQL_UPDATE_LINE)
            #cnxn.commit()
        else:
            print("LINE update aborted")
		
	if LINE_STATUS == 'BAD':
		print("PLEASE OPEN STS100 and go to lines and add G panel and change the Payer in G Panel")
     
	LINE_DATA = cursor.fetchone()

