''' 
def create_carré():
    return lambda x: x ** 2 #prend un paramètre x et retourne le carré de x

carré = create_carré()

print(carré(5)) #affiche 25
'''


def create_carré():
    return lambda x: x ** 2

#Liste  
numbers = [1, 2, 3, 4, 5]

#map pour appliquer la fonction carré à chaque élément
carré = create_carré()
squares = list(map(carré, numbers))

print(squares)  #résultat sera : [1, 4, 9, 16, 25]

