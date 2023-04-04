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
cpt = 0

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

    if cpt % 100 == 0: #Si cpt est un multiple de 100 alors on rentre dans la boucle. 
        # Trouver le plus grand contour (l'objet rouge entouré de bleu)
        surface_max=None #le contour ayant la plus grande surface dans l'image
        val_surface_max=0 #la valeur de la surface  maximale trouvée
        for contour in contours:
            surface_contour = cv2.contourArea(contour) #calcule la surface du contour courant 
            if surface_contour > val_surface_max:
                surface_max = contour #contiends le contour avec la plus grande surface
                val_surface_max = surface_contour #contiends la valeur de cette surface maximale
        
        #Si aucun contour n'a été détecté dans l'image, surface_max restera à None.

        # Si un objet rouge entouré de bleu a été détecté, récupérer sa position et la comparer avec le centre de l'image
        if np.all(surface_max) != None:
            # Récupérer les coordonnées du rectangle englobant du plus grand contour
            x, y, l, h = cv2.boundingRect(surface_max) #x et y sont les coordonnée en haut a gauche du rectangle. l et h sont la longueur et la hauteur du rectangle

            # Calculer la position de l'objet par rapport au centre de l'image

            centreX_video = largeur / 2
            centreY_video = hauteur / 2
            centreX_rect = x + l / 2
            centreY_rect = y + h / 2

            x= centreX_rect -centreX_video
            y=  centreY_rect -centreY_video
            #si x est positif, le robot doit tourner à droite
            
            print('')
            print(x)
            print('')
            

    cpt += 1


    # Attendre 1 milliseconde pour que la fenêtre s'affiche
    # Si l'utilisateur appuie sur la touche "échap", sortir de la boucle
    k = cv2.waitKey(1)
    if k == 27: 
        break





# Fermer la fenêtre de sortie et l'objet VideoCapture
cv2.destroyAllWindows()
video.release()
# video_finale.release()









# https://towardsdatascience.com/computer-vision-for-beginners-part-4-64a8d9856208#:~:text=around%20the%20object.-,The%20function%20cv2.,bounding%20box%20as%20shown%20below.&text=Note%20that%20this%20straight%20rectangle,area%20with%20the%20function%20cv2.
# https://docs.opencv.org/3.4/dd/d49/tutorial_py_contour_features.html