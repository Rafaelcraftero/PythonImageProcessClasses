import numpy as np
import cv2 as cv

# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


img1 = cv.imread('../img/descargar.jfif') #img1 chica
img2 = cv.imread('../img/playa-sur-barcelona11.jpg') #img2 grande

img1Gray=cv.cvtColor(img1, cv.COLOR_RGB2GRAY)
img2Gray=cv.cvtColor(img2, cv.COLOR_RGB2GRAY)

img1Gray= np.append(img1Gray, np.zeros([img2.shape[0] - img1.shape[0], img1.shape[1]]), 0)
img1Gray= np.append(img1Gray, np.zeros([img2.shape[0], img2.shape[1] - img1.shape[1]]), 1)



#cv.imshow('suma', img1Gray.astype('uint8')+ img2Gray.astype('uint8'))

#cv.imshow('suma2', cv.add(np.round(img1Gray/2).astype('uint8'), np.round(img2Gray/2).astype('uint8')))

cv.imshow('suma3',  cv.add(np.round(img1Gray/2).astype('uint8'), np.round(img2Gray/2).astype('uint8')))

# ¿se han truncado todos los valores mayores de 255?
# Si se han truncado
# ¿Se han rescalado? A la vista de las respuestas anteriores ¿se ha perdido mucha información? Si
# No lo hemos tenido que reescalar, en to-do caso, lo hemos redimensionado a mano para que las imagenes se puedan sumar
# ¿cómo se podría mejorar el resultado para que en la superposición se vean lo mejor posible las dos imágenes?
# Se podria oscurecer la imagen dividiendole las capas entre 2 y luego hacerle un techo y sumandola posteriormente, otra forma sería aumentarle la profundidad a uint16

cv.waitKey(0)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/