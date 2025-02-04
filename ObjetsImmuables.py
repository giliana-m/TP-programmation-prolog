#Exercice 1 

#Question 1

def addToEach(n, list):
    return [x + n for x in list]
original_list = [1, 2, 3, 4, 5]
new_list = addToEach(3, original_list)

print("Original list:", original_list) #résultat [1, 2, 3, 4, 5]
print("New list:", new_list) #résultat [4, 5, 6, 7, 8]


#Question 2
def removeDuplicates(lst):
    return list(dict.fromkeys(lst))

original_list = [1, 2, 2, 3, 4, 4]
new_list = removeDuplicates(original_list)

print("Original list:", original_list)  #résultats = [1, 2, 2, 3, 4, 4]
print("New list:", new_list)            #résultat = [1, 2, 3, 4]







#Exercice 2 
import asyncio
import random
from dataclasses import dataclass

#Question 1 :Personne
@dataclass(frozen=True)
class Personne:
    nom: str
    age: int

#Question 2 :Fonction anniversaire
def anniversaire(personnes):
    return [Personne(personne.nom, personne.age + 1) for personne in personnes]

#QUestion 3 : promesse getRandomNumber
async def getRandomNumber():
     #Délai de 1 seconde
    await asyncio.sleep(1)
    return random.randint(1, 100)

#getRandomNumber pour générer deux nombres aléatoires
async def main():
    number1 = await getRandomNumber()
    number2 = await getRandomNumber()
    print(f"Premier nombre aléatoire : {number1}")
    print(f"Deuxième nombre aléatoire : {number2}")

#Exemple 
personnes = [Personne("A", 15), Personne("B", 20)]
personnes_mise_a_jour = anniversaire(personnes)

#résultats après l'anniversaire
for p in personnes_mise_a_jour:
    print(f"{p.nom} : {p.age} ans")

#Exécution
asyncio.run(main())  #résultat = Original list: [1, 2, 3, 4, 5] ;New list: [4, 5, 6, 7, 8] ;A : 16 ans ; B : 21 ans ; Premier nombre aléatoire : 48 ;Deuxième nombre aléatoire : 92
