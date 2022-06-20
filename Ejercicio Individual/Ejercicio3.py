import cv2


#Toma una imagen fotográfica en la que aparezca  un objeto sobre un fondo más o menos homogéneo. Cárgala en escala de grises.
#Trataremos de obtener los bordes del objeto en la imagen. Para ello probamos de dos formas:
#a) Método básico:
    #a. Suavizado Gaussiano;
    #b. Operadores Sobel para calcular el módulo del gradiente;
    #c. Umbralización.
#b) Método de Canny
#Compara los resultados y explica por qué el método de Canny da mejores resultados. Experimenta con los distintos parámetros implicados en en las funciones usadas en cada apartado (explicando qué significa cada uno).

imgOrig = cv2.imread('../img/depositphotos.jpg', 0)

#a)
    #a. Suavizado Gaussiano;
gauImage = cv2.GaussianBlur(imgOrig, (5,5),0)
#Aumentar el kernel resulta en una la eliminación de los bordes mas pequeños
    # b. Operadores Sobel para calcular el módulo del gradiente;
sobel_x=cv2.Sobel(gauImage,cv2.CV_64F,1,0)
sobel_y=cv2.Sobel(gauImage,cv2.CV_64F,0,1)
cv2.convertScaleAbs(sobel_x)
cv2.convertScaleAbs(sobel_y)
imgW=cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)
    # c. Umbralización.
T, imgresult= cv2.threshold(imgW, 40, 150, type=cv2.THRESH_BINARY)
#Cambiar el thresh y el maxval hace que los bordes se perfilen o agranden
cv2.imshow("resultado tradicional", imgresult)
cv2.waitKey(0)

#b)
imgCanny= cv2.Canny(imgOrig,150, 255)
#Cambiar el threshold1 y el 2, es decir los 2 valores numericos del canny hacen algo parecido al threshold del metodo simple pero en este caso elimina informacion de los bordes que se notan menos
cv2.imshow("resultado Canny", imgCanny)
cv2.waitKey(0)

#El método de canny da muchos mejores resultados dado que en el metodo tradicional, el suavizado hace que se pierda mucha información acerca de la localización exacta de los bordes al contrario que el metodo de canny
# que obtiene todos los cambios de tono correctamente y por tanto consigue todos los bordes de forma precisa lo que hace que los bordes sean muy grandes en algunos casos y desaparezcan en otros.