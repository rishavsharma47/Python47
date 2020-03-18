import cv2 as cv
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\ADMIN\AppData\Local\Tesseract-OCR\tesseract.exe'

image = cv.imread("SuccessQuote.jpg", 1)
text = pytesseract.image_to_string(image)
print(text)