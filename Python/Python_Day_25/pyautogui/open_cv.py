import cv2 
import os 

img_path=os.path.join(os.path.dirname(__file__),'./image.png')
img=cv2.imread(img_path)

cv2.imshow('Color Image',img)
print(img)
if img is None:
    print(f"Failed to load image at {img_path}")
else:
    print("Image loaded successfully")
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray Image', gray)
print(gray)
cv2.waitKey(0)
cv2.destroyAllWindows()