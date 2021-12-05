import pytesseract
import os 

os.chmod('Img2txt.py', 0o777)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
print(pytesseract.image_to_string(r'C:\Users\suren\OneDrive\Surface_Backup\RK\RK_work\Python_scripts\KeyBoard_CTRL\FAS001\FAS001_Screens\FAS001_B1.JPG'))
print(pytesseract.image_to_string(r'C:\Users\suren\OneDrive\Surface_Backup\RK\RK_work\Python_scripts\KeyBoard_CTRL\FAS001\FAS001_Screens\FAS001_E.JPG'))
print(pytesseract.image_to_string(r'C:\Users\suren\OneDrive\Surface_Backup\RK\RK_work\Python_scripts\KeyBoard_CTRL\FAS001\FAS001_Screens\FAS001_F.JPG'))
print(pytesseract.image_to_string(r'C:\Users\suren\OneDrive\Surface_Backup\RK\RK_work\Python_scripts\KeyBoard_CTRL\FAS001\FAS001_Screens\FAS001_G.JPG'))
print(pytesseract.image_to_string(r'C:\Users\suren\OneDrive\Surface_Backup\RK\RK_work\Python_scripts\KeyBoard_CTRL\FAS001\FAS001_Screens\FAS002_B.JPG'))
print(pytesseract.image_to_string(r'C:\Users\suren\OneDrive\Surface_Backup\RK\RK_work\Python_scripts\KeyBoard_CTRL\FAS001\FAS001_Screens\FAS003_B.JPG'))
print(pytesseract.image_to_string(r'C:\Users\suren\OneDrive\Surface_Backup\RK\RK_work\Python_scripts\KeyBoard_CTRL\FAS001\FAS001_Screens\FAS004_B.JPG'))
print(pytesseract.image_to_string(r'C:\Users\suren\OneDrive\Surface_Backup\RK\RK_work\Python_scripts\KeyBoard_CTRL\FAS001\FAS001_Screens\M3_TEXT.JPG'))
print(pytesseract.image_to_string(r'C:\Users\suren\OneDrive\Surface_Backup\RK\RK_work\Python_scripts\KeyBoard_CTRL\FAS001\savedImage.JPG'))
