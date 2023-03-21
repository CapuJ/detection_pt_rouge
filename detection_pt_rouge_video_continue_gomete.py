import cv2
import numpy as np

# Chargement de l'image "gomete"
gomete = cv2.imread('test.jpg')

# Extraire les valeurs minimale et maximale de rouge dans l'image "gomete"
hsv_gomete = cv2.cvtColor(gomete, cv2.COLOR_BGR2HSV)
min_h, max_h, _, _ = cv2.minMaxLoc(hsv_gomete[:,:,0])
min_s, max_s, _, _ = cv2.minMaxLoc(hsv_gomete[:,:,1])
min_v, max_v, _, _ = cv2.minMaxLoc(hsv_gomete[:,:,2])
# Définir les couleurs de la plage de couleurs à détecter à partir de l'image "gomete"
rouge_clair = np.array([min_h, min_s, min_v])
rouge_fonce = np.array([max_h, max_v, max_v])

# Chargement de la vidéo
video = cv2.VideoCapture(1)

# Obtenir les propriétés de la vidéo
largeur = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
hauteur = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
freq = int(video.get(cv2.CAP_PROP_FPS))

# Boucle sur chaque trame de la vidéo
while True:
    # Lire la trame vidéo
    res, image = video.read() #ret est un bollean qui verifie si la video a pu etre lu image est le nombre de frame
    if not res:  
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
