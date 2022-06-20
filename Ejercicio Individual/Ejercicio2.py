import cv2 as cv
import numpy as np

#PREGUNTA 2
#
#1. Carga una imagen en escala de grises, introduce ruido impulsivo blanco en dicha imagen de manera que la probabilidad de que un píxel no se vea alterado sea del 85%.
#2. Razona, según el tipo de ruido introducido, qué filtro es el más apropiado para eliminarlo y aplícalo con distintos tamaños de ventana.
#3. Usa alguna medida numérica del error (con respecto a la imagen original) para ver cuál es el que mejor ha funcionado.

#1

#Creamos la imagen de ruido blanco utilizando el código de salt and pepper pero le hemos eliminado la opción del pepper
def sp_noise(image, prob):
    '''
    Add salt and pepper noise to image
    prob: Probability of the noise
    '''
    output = image.copy()
    if len(image.shape) == 2:
        white = 255
    else:
        colorspace = image.shape[2]
        if colorspace == 3:  # RGB
            white = np.array([255, 255, 255], dtype='uint8')
        else:  # RGBA
            white = np.array([255, 255, 255, 255], dtype='uint8')
    probs = np.random.random(output.shape[:2])
    output[probs > 1 - (prob / 2)] = white
    return output
imgOrig = cv.imread('../img/playa-sur-barcelona11.jpg', 0)
imgNoise=sp_noise(imgOrig, 0.15) # si no se modifica el 85% significa que tendremos que añadir un ruido del 15%

#2
# La mejor forma de eliminar el ruido impulsivo blanco es utilizando el median blur o un algoritmo parecido dado que al haber espacios entre diferentes puntos no se creará ningun
# punto blanco enorme que imposibilite que se elimine. Esto nos deja con una imagen limpia ya que el medianblur convierte los pixeles al color de la media del entorno.
# La Apertura hace una operacion similar al median blur cuando se usa en imagenes que no son binarias (con opencv) creando un filtro muy parecido al de medinablur con la forma del kernel y aplicandolo posteriormente sbre la imagen
# entonces si la imagen tiene contornos que se extienden en su mayoría horizontalmente podremos mejorar el blur haciendo un kernel en horizontal o viceversa

#Apertura
m2=np.array([[1, 1, 1, 1, 1]]) #kernel
ero2=cv.erode(imgNoise, m2, 1) #erosion
dil2=cv.dilate(ero2,m2, 1) #dilatacion

# Con [[1, 1, 1, 1, 1, 1]] se elimina completamente el ruido pero si tuviese un 1 de menos, es decir, [[1, 1, 1, 1, 1]] (la actual), tendría la posibilidad de que continuasen algunos puntos pero
# se reduciría el error enormemente, si tuviese más 1's simplemente aumentaría el error y se distorcioaría la imagen aun más ya que los puntos se habrían eliminado con el kernel actual.

#medianblur
medianblur= cv.medianBlur(imgNoise, 5) #medianblur
# Con 3 siguen apareciendo los puntos blancos
# Con 5 siguen apareciendo los puntos blancos en los contornos cuando hay un cambio drástico de tonos de grises
# más haya de 5 no hay un cambio significativo en la imagen y sigue sucediendo el error que sucede con 5.

#imprimimos las diferentes versiones de las imagenes
cv.imshow("Imagen original", imgOrig)
cv.imshow("Imagen con ruido blanco", imgNoise)
cv.imshow("resultado blur", medianblur)
cv.imshow("resultado Apertura", dil2)

#3 calculamos el error cuadrático de las imagenes
mse=np.divide(np.sum(np.square(np.subtract(medianblur, imgOrig))), np.shape(imgOrig)[0]*np.shape(imgOrig)[1])
print("error blur "+str(mse))
mse=np.divide(np.sum(np.square(np.subtract(dil2, imgOrig))), np.shape(imgOrig)[0]*np.shape(imgOrig)[1])
print("error Apertura "+str(mse))


cv.waitKey(0)