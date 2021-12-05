import pytesseract
import os 

# os.chmod('Img2txt.py', 0o777)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
print('cropped_img.JPG-----------------------------------------------------------------------------------------------------------')
print(pytesseract.image_to_string(r'C:\Users\suren\OneDrive\Surface_Backup\RK\RK_work\Python_scripts\KeyBoard_CTRL\FAS001\cropped_img.jpg'))

