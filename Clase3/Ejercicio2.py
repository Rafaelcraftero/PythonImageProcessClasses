import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../img/blurry_moonSINSAL.png', cv2.IMREAD_GRAYSCALE)

#Crea el kernel

kernel = np.ones((5,5),np.float32)/25
for i in np.arange(kernel.shape[0]):
    if i%2==0:
        kernel[i]=0;


kernel=np.array([[0,1,0],[1,4,1],[0,1,0]])
#Filtra la imagen utilizando el kernel anterior
#dst = cv2.filter2D(img,-1,kernel, borderType=cv2.BORDER_REFLECT)
#Con borderType=cv2.BORDER_REFLECT se arregla los bordes
dst = cv2.Laplacian(img, cv2.CV_16S, ksize=3)
dst = cv2.convertScaleAbs(dst)
print(dst)
cv2.imshow("dst",dst)

Final=img+dst
cv2.imshow("Final",Final)

print(np.min(dst))
print(np.max(dst))
#Si esta dentro de los margenes

cv2.waitKey(0)