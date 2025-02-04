def create_carré():
    return lambda x: x ** 2 #prend un paramètre x et retourne le carré de x

carré = create_carré()

print(carré(5)) #affiche 25
