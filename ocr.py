import cv2
from matplotlib import test 
import pytesseract
import numpy as py

img = cv2.imread('image.jpg')

# get grayscale image
def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# noise removal
def remove_noise(image):
    return cv2.medianBlur(image,5)
 
#thresholding
def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

gray = get_grayscale(img)
thresh = thresholding(gray)

cv2.imshow('img', thresh)
cv2.waitKey(0)
pytesseract.pytesseract.tesseract_cmd = r"M:\Tesseract\tesseract.exe"
text = pytesseract.image_to_string(img)
print(text)
