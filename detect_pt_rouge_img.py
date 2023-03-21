import cv2
from matplotlib import pyplot as plt
import numpy as np

#Configuration du port série pour le robot

#Chargement de l'image
Image=cv2.imread('gomete.jpg')
Image2 = cv2.cvtColor(Image, cv2.COLOR_BGR2RGB)

plt.figure() # ouvre une nouvelle figure
plt.imshow(Image2) # affichage de l'image I en niveau de gris
plt.show()

#Definition des couleurs  a détecter
rouge_clair=np.array([0, 50, 50])
rouge_fonce=np.array([10, 255, 255])

#Detection des pixels rouges dans l'image
hsv = cv2.cvtColor(Image, cv2.COLOR_BGR2HSV)
masque=cv2.inRange(hsv,rouge_clair, rouge_fonce )

# Appliquer le masque à l'image d'entrée
resultat = cv2.bitwise_and(Image, Image, mask=masque)

# Trouver les contours des objets dans l'image
contours, hierarchie = cv2.findContours(masque, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Dessiner des contours jaunes autour des objets détectés
for contour in contours:
    cv2.drawContours(Image, [contour], 0, (255, 255, 0), 2)

# Enregistrer l'image avec le contour
cv2.imwrite('image_contour.png', Image)

# Afficher l'image avec le contour
plt.imshow( cv2.cvtColor(Image, cv2.COLOR_BGR2RGB))
plt.show()
