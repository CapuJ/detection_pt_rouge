import cv2
import numpy as np

# Chargement de la vidéo
# video = cv2.VideoCapture('IMG_7239.mp4')
video = cv2.VideoCapture(0)

duree = 5  # duree de la video en secondes
temps_debut = cv2.getTickCount()

# Obtenir les propriétés de la vidéo
largeur = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
hauteur = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
freq = int(video.get(cv2.CAP_PROP_FPS))

# Créer un objet VideoWriter pour écrire la nouvelle vidéo avec les contours
format = cv2.VideoWriter_fourcc(*'mp4v') # Format de la nouvelle vidéo
video_finale = cv2.VideoWriter('video_contours.mp4', format, freq, (largeur, hauteur))

# Définir les couleurs de la plage de couleurs à détecter
rouge_clair=np.array([0, 50, 50])
rouge_fonce=np.array([10, 255, 255])

# np.array([11, 93, 53])


# Boucle sur chaque trame de la vidéo
while True:
    # Lire la trame vidéo
    ret, image = video.read()
    if not ret:
        break
    
    # Convertir la trame vidéo en HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Appliquer le masque pour détecter les pixels rouges
    masque=cv2.inRange(hsv,rouge_clair, rouge_fonce )

    # Trouver les contours des objets dans l'image
    contours, hierarchie = cv2.findContours(masque, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Dessiner des contours jaunes autour des objets détectés
    for contour in contours:
        cv2.drawContours(image, [contour], 0, (255, 255, 0), 2)

    # Écrire la nouvelle trame avec les contours dans la vidéo
    video_finale.write(image)

    # Check if the duration has been reached
    temps_ecoule = (cv2.getTickCount() - temps_debut) / cv2.getTickFrequency()
    if temps_ecoule >= duree:
        break


# Fermer les objets VideoCapture et VideoWriter
video.release()
video_finale.release()

