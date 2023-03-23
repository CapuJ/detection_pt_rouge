
window.addEventListener("DOMContentLoader", function(){ 
   
   // Récupérer le canvas
    var canvas = document.getElementById('canvas');









    // // Créer un objet VideoCapture pour lire la vidéo en continu
    // const cap = new cv.VideoCapture(0); // utiliser 0 pour la webcam intégrée ou 1 pour une caméra externe

    // // Fonction pour afficher chaque trame vidéo sur le canvas
    // function processVideo() {
    //     cap.read(image); // Lire une trame vidéo

    //     // Convertir l'image en format de couleur HSV
    //     cv.cvtColor(image, hsv, cv.COLOR_BGR2HSV);

    //     // Appliquer le masque pour détecter les pixels rouges
    //     cv.inRange(hsv, rouge_clair, rouge_fonce, masque);

    //     // Trouver les contours des objets dans l'image
    //     cv.findContours(masque, contours, hierarchy, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE);

    //     // Dessiner des contours jaunes autour des objets détectés
    //     for (let i = 0; i < contours.size(); ++i) {
    //         cv.drawContours(image, contours, i, [255, 255, 0, 255], 2);
    //     }

    //     // Afficher l'image sur le canvas
    //     cv.imshow('canvas', image);

    //     // Attendre 30 millisecondes avant d'afficher la prochaine trame
    //     setTimeout(processVideo, 30);
    // }

    // // Lancer le traitement de la vidéo
    // processVideo();





    video = document.getElementById("video");

    errBack =function(error){
        console.log("video capture error:" , error.code);
    };


    if(navigator.getUseMedia){
        navigator.getUseMedia({video: true}, function(stream){
            video.src=stream;
            video.play();
        }, errBack);
    } else if(navigator.webkitGetUserMedia){
        navigator.webkitGetUserMedia({video: true}, function(stream){
            video.src=window.webkitURL.createObjectURL(stream);
            video.play();
        }, errBack);
    } else if(navigator.mozGetUserMedia){
        navigator.mozGetUserMedia({video: true}, function(stream){
            video.srcObject=stream;
            video.play();
        }, errBack);
    }

    
}, false);

