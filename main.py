import cv2
import pytesseract
import imutils

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Tanisha Singh\Downloads\tesseract-ocr-w64-setup-5.3.1.20230401.exe"
count=7
plateCascade=cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")


img=cv2.imread('car2.jpg')
img=imutils.resize(img,width=100)
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img=cv2.bilateralFilter(img,11,17,17)
img=cv2.GaussianBlur(img,(3,3),0)


plates=plateCascade.detectMultiScale(img,1.1,4)

for (x,y,w,h) in plates:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    img=img[y:y+h,x:x+w]
    break

cv2.imshow('result',img)
plate = pytesseract.image_to_string(img)
print("Number plate is:", plate.replace(" ",""))
cv2.waitKey(0)
cv2.destroyAllWindows()

