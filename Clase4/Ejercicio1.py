import numpy as np
import cv2
img=cv2.imread('../img/circulos_ruidos.png', cv2.IMREAD_GRAYSCALE)

m=np.array([[1], [1], [1]])
dil1=cv2.dilate(img, m, 1)
ero1=cv2.erode(dil1, m, 1)

m2=np.array([[1, 1, 1]])
ero2=cv2.erode(ero1, m2, 1)
dil2=cv2.dilate(ero2,m2, 1)

mse=np.divide(np.sum(np.square(np.subtract (dil2, img))), np.shape(img)[0]*np.shape(img)[1])
lol=cv2.absdiff(img, dil2)
print(mse)

#cv2.imshow("resultado", img)
#cv2.waitKey(0)
#0.026798248291015625 2x3
#0.001308441162109375 3x3
# eliminar blancos verticales 1x3 y eliminar negros horizontales 3x1 0.001018524169921875

#b)

m3=cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (31,31))

dil3=cv2.dilate(dil2, m3, 1)
ero3=cv2.erode(dil3, m3, 1)

m4=cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (35,2))

ero4=cv2.erode(ero3, m4, 1)
dil4=cv2.dilate(ero4, m4, 1)



cv2.imshow("resultado", dil4)
cv2.waitKey(0)