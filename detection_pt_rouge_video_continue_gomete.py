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
# video = cv2.VideoCapture(0) #0 pour la cémra de l'ordi
video = cv2.VideoCapture(0) #1 pour la caméra externe relié au port usb

# Obtenir les propriétés de la vidéo
largeur = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
hauteur = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
freq = int(video.get(cv2.CAP_PROP_FPS)) #fréquence des images par secondes 

# Créer un objet VideoWriter pour écrire la nouvelle vidéo avec les contours
# format = cv2.VideoWriter_fourcc(*'mp4v') # Format de la nouvelle vidéo
# video_finale = cv2.VideoWriter('video_finale.mp4', format, freq, (largeur, hauteur))

# Boucle sur chaque trame de la vidéo
while True:
    # Lire la trame vidéo
    res, image = video.read() #res est un bollean qui verifie si la video a pu etre lu est image est une "capture de video"
    if res == False:  
        break

    # Convertir la trame vidéo en HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Appliquer le masque pour détecter les pixels rouges
    masque = cv2.inRange(hsv, rouge_clair, rouge_fonce)

    # Trouver les contours des objets dans l'image
    contours, hierarchie = cv2.findContours(masque, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Dessiner des contours bleus autour des objets détectés
    for contour in contours:
        cv2.drawContours(image, [contour], 0, (255, 255, 0), 2)

    # Afficher la trame courante avec les contours dans une fenêtre de sortie
    cv2.imshow("Video", image)
    # video_finale.write(image)

    # Attendre 1 milliseconde pour que la fenêtre s'affiche
    # Si l'utilisateur appuie sur la touche "échap", sortir de la boucle
    k = cv2.waitKey(1)
    if k == 27: 
        break


# Fermer la fenêtre de sortie et l'objet VideoCapture
cv2.destroyAllWindows()
video.release()
# video_finale.release()
