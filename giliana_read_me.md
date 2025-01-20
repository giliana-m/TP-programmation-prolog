# TP-programmation-logique-prolog MARKANDU.G

**INPUT** :  n = int(input("Combien d'étudiants souhaitez-vous saisir ? "))
input("...") : permet d'afficher un message à l'utilisateur et de récupérer ce qu'il saisit sous forme de texte (chaîne de caractères).
Et int(...) : La fonction input retourne toujours une chaîne de caractères, mais dans cet exo on a besoin d'un nombre entier pour savoir combien d'étudiants nous allons saisir. On convertit la valeur en entier avec int().


**F-STRING** : f"La moyenne de la classe est de {moyenne:.2f}."
f-string (chaîne de caractères formatée), qui permet d'incorporer des variables dans une chaîne de caractères. L'expression entre les accolades {} est évaluée et insérée dans la chaîne :
.2f est un format spécifiant comment la valeur de moyenne doit être affichée :
f signifie que nous voulons un format de nombre flottant ( un nombre avec des décimales).
.2 signifie que nous voulons 2 chiffres après la virgule.
