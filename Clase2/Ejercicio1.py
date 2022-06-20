
from matplotlib import pyplot as plt
import numpy as np
import cv2 as cv

imgOrig = cv.imread('../img/playa-sur-barcelona11.jpg')

imgGray=cv.cvtColor(imgOrig.astype('uint8'), cv.COLOR_RGB2GRAY)

cv.imshow('img', imgGray)

hist=cv.calcHist(imgGray, [0], None, [256], [0,256])
#hist[0:10]=0 ; para eliminar parte del histograma

plt.plot(hist, color='gray')
plt.xlabel('intensidad de iluminacion')
plt.ylabel('cantidad de pixeles')
plt.show()

cv.waitKey(0)

# A) Como en el histograma todos los grises estan en una pequeña franja nos dice que es una imagen de poco contraste

# B) En mi imagen casi todos los colores se acumiulan en los medios tonos por lo tanto no mejoraria en ninguno de los casos.
