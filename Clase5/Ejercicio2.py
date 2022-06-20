
from matplotlib import pyplot as plt
import numpy as np
import cv2 as cv

img=cv.imread('../img/house.png', 0)

cv.imshow('img', img)
img=cv.blur(img, (11,11))
hist=cv.calcHist(img, [0], None, [256], [0,256])
#hist[0:10]=0 ; para eliminar parte del histograma

plt.plot(hist, color='gray')
plt.xlabel('intensidad de iluminacion')
plt.ylabel('cantidad de pixeles')
plt.show()

ret3,th3 = cv.threshold(img,0,200,cv.THRESH_OTSU)
cv.imshow('im2g', th3)
cv.waitKey(0)

#el suavizado si lo mejora