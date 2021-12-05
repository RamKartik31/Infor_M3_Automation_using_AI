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

def Update_M3_Site_ID_In_BOCAFORM(BId,M3_Site_ID_in_BOCA_form,M3_ADID_in_Customer_OIS002_SF_SPOT):

	 if(M3_Site_ID_in_BOCA_form !=''):
	     print(str(M3_Site_ID_in_BOCA_form)+":Please add this ID in program MMS230")
	 else:
	     print('M3_ADID in table Customer_OIS002_SF_SPOT: '+str(M3_ADID_in_Customer_OIS002_SF_SPOT))
	     strSQL_Update_BOCA_Form = "UPDATE BOCA_Form  SET M3_Site_ID='"+ M3_ADID_in_Customer_OIS002_SF_SPOT +"' where SF_BId ='"+BId+"'"
	     print(strSQL_Update_BOCA_Form)
	     ch= input('Press Y to execute above SQL : ')
	     if ch == 'Y':
	          print('SQL stmt executed')
	          # cursor.execute(strSQL_Update_BOCA_Form)
	          # cnxn.commit()

def Process_All_Rows():
    try:
        cnxn = pyodbc.connect(conStr)
        cursor = cnxn.cursor()

        BOCA_FORM_IDS_WITH_EMPTY_SITE_ID = "SELECT SF_BId,SF_Aid,A.M3_Site_ID,B.M3_ADID,A.CRS_M3_Quote_Number__c FROM BOCA_Form A inner join Customer_OIS002_SF_SPOT B on A.SF_Aid = B.SF_AId where  A.CRS_M3_Quote_Number__c='' AND B.M3_ADID !=''"
        print(BOCA_FORM_IDS_WITH_EMPTY_SITE_ID)
        cursor.execute(BOCA_FORM_IDS_WITH_EMPTY_SITE_ID) 
        row_BOCAFORM = cursor.fetchall()
        
        print(row_BOCAFORM)
        print("Total rows are: ", len(row_BOCAFORM))
        
        if len(row_BOCAFORM)==0:
            print("No records")
        else:
            for row in row_BOCAFORM:
                print('for loop')
                BId = row[0] //SF_BId
                M3_ADID_in_Customer_OIS002_SF_SPOT = row[3] //M3_ADID
                M3_Site_ID_in_BOCA_form = row[2] //M3_Site_ID
                print(BId)
                print("M3_Site_ID_in_BOCA_form : "+M3_Site_ID_in_BOCA_form)
                Update_M3_Site_ID_In_BOCAFORM(BId,M3_Site_ID_in_BOCA_form,M3_ADID_in_Customer_OIS002_SF_SPOT)
        cursor.close()
        
    except pyodbc.Error as error:
        print("Failed to read data from table", error)


Process_All_Rows()
