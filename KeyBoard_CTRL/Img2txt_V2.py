import pytesseract
import os

CroppedScreens_data_list = []
def getCroppedScreendata():
    CroppedScreens_data_list = []
    FAS001_CroppedScreens_path = r'C:\Users\suren\OneDrive\Surface_Backup\RK\RK_work\Python_scripts\KeyBoard_CTRL\FAS001\FAS001_CroppedScreens'
    for file in os.listdir(FAS001_CroppedScreens_path):
        filepath = os.path.join(FAS001_CroppedScreens_path, file)
        # print(filepath)
        # print(pytesseract.image_to_string(filepath))
        str = pytesseract.image_to_string(filepath)
        print(str)
        CroppedScreens_data_list.append(str)
        
    print(CroppedScreens_data_list)
    return CroppedScreens_data_list

res = getCroppedScreendata()
PresentScreen_Data = pytesseract.image_to_string(r'C:\Users\suren\OneDrive\Surface_Backup\RK\RK_work\Python_scripts\KeyBoard_CTRL\FAS001\000EPanel.jpg')
# print(PresentScreen_Data)
print(CroppedScreens_data_list)
for val in res:
    print(val)
    if val in PresentScreen_Data:
        print('true')
    else:
        print('false')