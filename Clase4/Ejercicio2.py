import numpy as np
import cv2
img=cv2.imread('../img/coche_bordes.jpg', cv2.IMREAD_GRAYSCALE)

m=cv2.getStructuringElement(cv2.MORPH_RECT, (30,4))

dil1=cv2.dilate(img, m, 1)
ero1=cv2.erode(dil1, m, 1)

m2=cv2.getStructuringElement(cv2.MORPH_RECT, (4,40))

dil2=cv2.dilate(img, m2, 1)
ero3=cv2.erode(dil2, m2, 1)



cv2.imshow("resultado", ero3)
cv2.waitKey(0)