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


#Somme
somme = lambda a, b: a + b
print(somme(2, 6))  #résultat : 8


from functools import reduce

#Expression lambda pour additionner deux nombres
somme = lambda a, b: a + b

#Liste
numbers = [1, 2, 3, 4, 5]

#reduce pour réduire la liste en somme totale
total = reduce(somme, numbers)

print(total)  #résultat = 15
