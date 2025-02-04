#Exo 1.1
def create_carré():
    return lambda x: x ** 2 #prend un paramètre x et retourne le carré de x

carré = create_carré()

print(carré(5)) #affiche 25


#Exo 1.2
def create_carré():
    return lambda x: x ** 2

#Liste  
numbers = [1, 2, 3, 4, 5]

#map pour appliquer la fonction carré à chaque élément
carré = create_carré()
squares = list(map(carré, numbers))

print(squares)  #résultat sera : [1, 4, 9, 16, 25]


#Exo 1.3 Somme
somme = lambda a, b: a + b
print(somme(2, 6))  #résultat : 8


#Exo 1.4
from functools import reduce

#Expression lambda pour additionner deux nombres
somme = lambda a, b: a + b

#Liste
numbers = [1, 2, 3, 4, 5]

#reduce pour réduire la liste en somme totale
total = reduce(somme, numbers)

print(total)  #résultat = 15


#exo 2.1

#Fonction create_multiplier
def create_multiplier(n):
    return lambda x: x * n

#Exo 2.2 fonctions pour calculer double et triple
double = create_multiplier(2)
triple = create_multiplier(3)

#Exo 2.3 Tests
print(double(2))  #résultat 4
print(double(4))  #résultat 8

print(triple(2))  #résultat 6
print(triple(4))  #résultat 12



