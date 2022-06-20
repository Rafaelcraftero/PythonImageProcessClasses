import numpy as np
import cv2
img=cv2.imread('../img/house.png', 0)

cv2.imshow("resultado img", img)
imgblur = cv2.blur(img, (5,5))


sobel_x=cv2.Sobel(imgblur,cv2.CV_64F,1,0)
sobel_y=cv2.Sobel(imgblur,cv2.CV_64F,0,1)
 # Utilice la matriz de imagen de tipo int8 sin signo directamente, lo que dará como resultado la pérdida de algunos valores negativos o valores superiores a 255 después de la derivada direccional

cv2.convertScaleAbs(sobel_x)
cv2.convertScaleAbs(sobel_y)

imgW=cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)

T, imgresult= cv2.threshold(imgW, 50, 255, type=cv2.THRESH_BINARY)

canny= cv2.Canny(img,120, 255)

 # El uso directo de la matriz de imagen de tipo float32 no causará la pérdida de algunos valores de la imagen de salida, sino porque la función cv2.imshow () no admite la salida
 # float32 image, por lo que debe cambiar la imagen de salida a uint8 type a través de cv2.convertScaleAbs ()

cv2.imshow("resultado img", img)
cv2.imshow("resultado gauImage", imgblur)
cv2.imshow("resultado imgresult", imgresult)
cv2.imshow("resultado canny", canny)
cv2.waitKey(0)