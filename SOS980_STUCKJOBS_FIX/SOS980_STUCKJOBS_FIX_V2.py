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

Stuck_job_number =input(str("Enter stuck job number: "))

Find_all_invoices_in_stuck_job = "SELECT top 1 STCONO,STCUNO,STIVNO,STGEOF,STGEOO,STGEOT,STITNO FROM MVXJDTA.FTAXTR	WHERE (STBJNO = '"+Stuck_job_number+"')"
cursor.execute(Find_all_invoices_in_stuck_job)
row_Find_all_invoices_in_stuck_job = cursor.fetchone()

print("Rows returned = ",row_Find_all_invoices_in_stuck_job.rowcount)
COMPANY_cono = row_Find_all_invoices_in_stuck_job[0]
CUSTOMER_NO = row_Find_all_invoices_in_stuck_job[1]
OLD_GEOCODE = row_Find_all_invoices_in_stuck_job[5]

def finalStep():
    print('Run the job in SOS980 program. After you run the job wait for job to process then refresh SOS980. That job will disappear from the job list. You may get a mail as well with invoice output')


if row_Find_all_invoices_in_stuck_job.rowcount == 0:
    print('Right click on job number and select run in program SOS980')
    finalStep()

else:
    Finding_UAADID_or_Site_ID = "SELECT UAADID,UACUA4, UAPYNO ,* FROM MVXJDTA.SDHEAD WHERE UAORST = 69 AND UAPYNO = '"+CUSTOMER_NO+"'"
    print("Goto CRS610 and update the geocode for site id: "+Finding_UAADID_or_Site_ID+" and Customer#"+CUSTOMER_NO+" and address type 2 press Y after refresh")
    isGeoCodeRefereshed =input(str("Is Geo COde Refreshded "))
    if isGeoCodeRefereshed == "Y" :
    
        NEW_GEOCODE_SQL = "select OPCONO,OPCUNO,OPADRT,OPADID,OPCUNM,OPGEOC,OPRGDT from MVXJDTA.OCUSAD WHERE OPCONO = '"+COMPANY_cono+"' AND OPADRT = 2 AND OPCUNO='"+CUSTOMER_NO+"'"
        cursor.execute(NEW_GEOCODE_SQL)
        row_NEW_GEOCODE_SQL = cursor.fetchone()
        NEW_GEOCODE = row_NEW_GEOCODE_SQL[5]

        if(OLD_GEOCODE == NEW_GEOCODE)
            is_AL_or_ML = input(str(' old and new geo code is same please conform for state AL or ME \n Enter choice Y or N'))
            if is_AL_or_ML == "Y":
                SQL_update_586 = "UPDATE MVXJDTA.FTAXTR SET STCONO = 586 WHERE STBJNO = '"+Stuck_job_number+"' AND STITNO = 9901 AND STCUNO = '"+CUSTOMER_NO+"' AND STGEOT = ''"+OLD_GEOCODE+"''
                print(SQL_update_586)
                is_OK_to_update_SQL_update_586 = input(str(' Shall I update above statemnet? presss Y or N'))
                    
                if is_OK_to_update_SQL_update_586 == 'Y':
                    cursor.execute(SQL_update_586)
                    cursor.execute(COMMIT)
                    finalStep()
                
                else:
                    print("No UPDATE DONE")
                    break
            else:
                print("if state is not AL or Me then I dont have a solution.....")
        
    else:
        update_SQL_update_GeoCOde = "UPDATE MVXJDTA.FTAXTR SET STGEOT = '"+NEW_GEOCODE+"' WHERE STBJNO = '"+Stuck_job_number+"' and STCUNO= '"+CUSTOMER_NO+"' and STGEOT = ''"+OLD_GEOCODE+"''
        print(update_SQL_update_GeoCOde)
        is_OK_to_update_SQL_update_GeoCOde = input(str('Do you want to execute the above SQL? \n Enter choice y or n'))
        
        if is_OK_to_update_SQL_update_GeoCOde == 'Y':
            cursor.execute(update_SQL_update_GeoCOde)
            cursor.execute(COMMIT)
            finalStep()
            
        else:
            break