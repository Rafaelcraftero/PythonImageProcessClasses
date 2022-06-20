import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

#PREGUNTA 1
#
# Busca una imagen en escala de grises con poco contraste y clara (o luminosa). Cárgala como imagen en escala de grises, calcula y visualiza su histograma
# y justifica que efectivamente es una imagen con poco contraste y clara. Aumenta el contraste de la imagen:
#a) Mediante una tansformación de tipo raíz o potencia entera, justificando cuál es más apropiada. Diseña la operación para que el resultado se encuentre en [0.255].
#b) Mediante una ecualización del histograma. Explica en qué consiste este método.
#Compara los histogramas obtenidos y saca conclusiones. Explica detallada y razonadamente la solución aportada.

imgOrig = cv.imread('../img/clara_poco__contraste.bmp', 0)
cv.imshow('imgagen', imgOrig)
cv.waitKey(0)
imgHist = cv.calcHist([imgOrig], [0], None, [256], [0, 256])
plt.xlabel('Gris')
plt.ylabel('pxl')
plt.plot(imgHist)
plt.show()
cv.waitKey(0)
# Es una imagen con poco contraste porque casi todos los grises se acumulan en una pequeña franja y es claro porque está muy a la izquierda en el histograma es decir se acercan mucho a
# el blanco

#A)
n=3
filas, columnas = imgOrig.shape
imgPot = np.zeros((filas, columnas),dtype=np.uint8)
r = np.max(imgOrig)
c = r / pow(r, n)
for x in range(filas):
    for y in range(columnas):
        imgPot[x, y] = c * (pow(imgOrig[x, y], n))
cv.imshow("resultado potencia", imgPot)
imgHist2 = cv.calcHist([imgPot], [0], None, [256], [0, 256])
plt.xlabel('Gris')
plt.ylabel('pxl')
plt.plot(imgHist2)
plt.show()
cv.waitKey(0)

# Utilizo transformaciones tipo potencia de 3 debido a que es la que mejor contraste le da en vez de la transformacción tipo raiz la cual
# elimina aun mas el contrate, si aumentasemos la potencia en 1 se distorcionaría la imagen por lo tante el máximo que le podemos dar es de 3.
# La escala de grises es mucho mas amplia en este nuevo histograma, lo comprobamos viendo como los pixeles se agrupan mas uniformemente
# que antes que se agrupaban todos en una pequeña franja.


# B)
imgEc=cv.equalizeHist(imgOrig)
cv.imshow("resultado ecualizado", imgEc)
histEq = cv.calcHist(imgEc, [0], None, [256], [0,256])
plt.plot(histEq)
plt.show()
# La ecualización intenta hacer que los pixeles cambien su nivel de gris de forma que la probabilidad sea similar entre todos los niveles de grises.



# El contraste ha aumentado significativamente luego de hacer la potencia sin embargo ha habido un gran aumento en los tonos intermedios por lo tanto, aunque ciertamente
# el contraste ha aumentado sigue sin ser ideal ya que ignora ligeramente los tonos más claros y más oscuros.
# Una vez realizado la ecualización se ha podido comprobar como el contraste ha aumentado al maximo y la imagen se ve nitidamente desde los tonos mas oscuros a los más claros
# sin perdida de calidad.