import numpy as np
import cv2 as cv

# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

img = cv.imread('../img/descargar.jfif')

#r, g, b = cv.split(img)
#img2 = 0.299 * r + 0.587 * g + 0.114 * b
#

img3=cv.cvtColor(img, cv.COLOR_RGB2GRAY)


#imgGrayHSI=1/3*(r+g+b)



# Press the green button in the gutter to run the script.



cv.imshow('img2', img3.astype('uint8'))

cv.imwrite('../img/desc.jpg', img3)

cv.waitKey(0)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/