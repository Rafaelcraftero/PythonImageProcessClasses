from matplotlib import pyplot as plt
import numpy as np
import cv2 as cv


imgOrig = cv.imread('../img/jiraf kheasertio.jpeg', cv.IMREAD_GRAYSCALE)

imgEc=cv.equalizeHist(imgOrig)


histOrg = cv.calcHist(imgOrig, [0], None, [256], [0,256])
histEq = cv.calcHist(imgEc, [0], None, [256], [0,256])

plt.plot(histOrg)
plt.show()
plt.plot(histEq)
plt.show()

imgDif = np.abs(imgOrig-imgEc)
T,imgDifThr = cv.threshold(imgDif, 127, 255, cv.THRESH_TRUNC)

cv.imshow('imgOrginal', imgOrig)

cv.imshow('ecualizada', imgEc)

cv.imshow('Diferencia', imgDif)

cv.imshow('Humbral', imgDifThr)

cv.waitKey(0)

cv.destroyAllWindows()