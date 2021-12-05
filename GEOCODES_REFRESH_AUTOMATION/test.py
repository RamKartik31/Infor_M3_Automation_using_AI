Customer_nos = ['SC18590','SC23172' ,'SC01310']
Atp_nos = ['2','2']
Address_nos = ['216', '164', '354']


for index1,Customer_no in enumerate(Customer_nos):
    for index2,Atp_no in enumerate(Atp_nos):
        for index3,ad_no in enumerate(Address_nos):
            if index1==index2:
                print(Customer_no +':' +Atp_no+':' +ad_no)
            continue
        continue
    continue