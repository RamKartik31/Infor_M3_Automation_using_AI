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

def Update_M3_Site_ID_In_BOCAFORM():
	 strSQL_Customer_OIS002_SF_SPOT = "select M3_ADID from Customer_OIS002_SF_SPOT where SF_AId ='"+SF_Aid_in_BOCAFORM+"'"
	 cursor.execute(strSQL_Customer_OIS002_SF_SPOT) 
	 row_Customer_OIS002_SF_SPOT = cursor.fetchone()
	 M3_ADID_in_Customer_OIS002_SF_SPOT = row_Customer_OIS002_SF_SPOT[0]
	 
	 if(M3_ADID_in_Customer_OIS002_SF_SPOT ==''):
	     print("M3_ADID in table Customer_OIS002_SF_SPOT is missing: Probably Mandatory fields like BillingState is not there in data")
	 else:
	     print('M3_ADID in table Customer_OIS002_SF_SPOT: '+M3_ADID_in_Customer_OIS002_SF_SPOT)
	     strSQL_Update_BOCA_Form = "UPDATE BOCA_Form  SET M3_Site_ID='"+ M3_ADID_in_Customer_OIS002_SF_SPOT +"' where SF_BId ='"+BId+"'"
	     print(strSQL_Update_BOCA_Form)
	     cursor.execute(strSQL_Update_BOCA_Form)
	     cnxn.commit()		 
		 

BId =input(str("Enter BId (get this from email Alert) "))
strSQL_BOCAFORM = "SELECT SF_Aid,M3_Site_ID FROM BOCA_Form where SF_BId ='"+BId+"'"

cursor.execute(strSQL_BOCAFORM) 
row_BOCAFORM = cursor.fetchone() 
SF_Aid_in_BOCAFORM = row_BOCAFORM[0]
M3_Site_ID_in_BOCAFORM = row_BOCAFORM[1]

#print("SF_Aid : "+ SF_Aid_in_BOCAFORM)


	  
if(M3_Site_ID_in_BOCAFORM ==''):
  print("M3_Site_ID in BOCA_Form: is missing")
  Update_M3_Site_ID_In_BOCAFORM()
else:
  print("M3_Site_ID in table BOCA_Form: is there as "+ M3_Site_ID_in_BOCAFORM+"  BUT its failing to create P number.") 
  print("ensure all mandatory fields are correct in BOCA Form")
  print("1. Please check if the M3 site ID is there in the program MMS230")
  print("2. if still faiing check site id in CRS610--> addresses--> address type 2 and site ID: if its not there then wipeout M3_ADID in Customer_OIS002_SF_SPOT.")
  print("RUN BELOW UPDATE THEN it will be recreated in next iteration")
  print("UPDATE Customer_OIS002_SF_SPOT SET M3_ADID='' WHERE   SF_AId = '"+SF_Aid_in_BOCAFORM+"'")

	

 

