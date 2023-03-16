import cv2
import numpy as np

# Chargement de la vidéo
video = cv2.VideoCapture(0)

# Obtenir les propriétés de la vidéo
largeur = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
hauteur = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
freq = int(video.get(cv2.CAP_PROP_FPS))

# Définir les couleurs de la plage de couleurs à détecter
rouge_clair = np.array([136, 87, 111])
rouge_fonce = np.array([180, 255, 255])

# Boucle sur chaque trame de la vidéo
while True:
    # Lire la trame vidéo
    ret, image = video.read()
    if not ret:
        break

    # Convertir la trame vidéo en HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Appliquer le masque pour détecter les pixels rouges
    masque = cv2.inRange(hsv, rouge_clair, rouge_fonce)

    # Trouver les contours des objets dans l'image
    contours, hierarchie = cv2.findContours(masque, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Dessiner des contours jaunes autour des objets détectés
    for contour in contours:
        cv2.drawContours(image, [contour], 0, (255, 255, 0), 2)

    # Afficher la trame courante avec les contours dans une fenêtre de sortie
    cv2.imshow("Video", image)

    # Attendre 1 milliseconde pour que la fenêtre s'affiche
    # Si l'utilisateur appuie sur la touche "q", sortir de la boucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Fermer la fenêtre de sortie et l'objet VideoCapture
cv2.destroyAllWindows()
video.release()
