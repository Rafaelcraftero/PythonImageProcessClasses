import numpy
import numpy as np
import cv2
import random


img = cv2.imread('../img/blurry_moon.png', cv2.IMREAD_GRAYSCALE)

#img2 = cv2.GaussianBlur(img, (11,11), 0)
img2= cv2.medianBlur(img, 11)
#El blur da un resultado mucho mejor porque el gaussiano aplica una mascara y da distintos pesos dependiendo e la sdistancia al centor entonces coge tanto pixlees como fuera como alrededores
#y hace una media  entonces el valor delruido estara en los extremos sin embargo el blur coge la todos los valores y coge la mediana,
cv2.imshow("moonOriginal",img)
cv2.imshow("moonEditada",img2)
img3=img-img2
img3=img3*img3
array1dimension=np.sum(img3, 0)
sumatorioFinal=np.sum(array1dimension, 0)

ErrorCuadratico= float(sumatorioFinal) / (img.shape[0] * img.shape[1])
print(ErrorCuadratico)
cv2.waitKey(0)
#El error es mucho mas alto en el filtro Gausiano