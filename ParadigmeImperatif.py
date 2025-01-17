# Partie 1 : Saisie des données
def saisir_donnees():
    n = int(input("Combien d'étudiants souhaitez-vous saisir ? "))  # nombre d'étudiants
    noms = []  # Liste noms des étudiants
    notes = []  # Liste notes des étudiants
    
    for i in range(n):
        nom = input(f"Nom de l’étudiant {i + 1} : ")  # nom de l'étudiant
        note = float(input(f"Note de {nom} : "))  # note de l'étudiant
        noms.append(nom)  # Ajoute nom à la liste
        notes.append(note)  # Ajoute note à la liste
    
    return noms, notes  # Retourne deux listes


# Partie 2 : Calcul de la moyenne
def calcul_moyenne(notes):
    return sum(notes) / len(notes) if len(notes) > 0 else 0  # Moyenne des notes

def main():
#partie 1
    noms, notes = saisir_donnees()
    print("Noms des étudiants :", noms)
    print("Notes des étudiants :", notes)

#partie 2
    moyenne = calcul_moyenne(notes)  # Calcul de la moyenne
    print(f"La moyenne de la classe est de {moyenne:.2f}.")  # Affiche Moyenne, f-string, variables dans une chaîne de caractères arrondit à 2 décimales

if __name__ == "__main__":
    main()
