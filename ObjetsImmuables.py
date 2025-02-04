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


#Exercice 2 : Question 1
from dataclasses import dataclass

@dataclass(frozen=True)
class Personne:
    nom: str
    age: int


#Question 2
#anniversaire qui augmente l'âge
def anniversaire(personnes):
    return [Personne(personne.nom, personne.age + 1) for personne in personnes]

#Liste personnes
personnes = [Personne("A", 15), Personne("B", 20)]

#Applique fonction anniversaire
personnes_mise_a_jour = anniversaire(personnes)

#Résultats
for p in personnes_mise_a_jour:
    print(f"{p.nom} : {p.age} ans")

# résultat = Original list: [1, 2, 3, 4, 5] ; New list: [4, 5, 6, 7, 8] ; A : 16 ans ; B : 21 ans
