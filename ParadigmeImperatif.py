# Partie 1 : Saisie des données
def saisir_donnees():
    n = int(input("Combien d'étudiants souhaitez-vous saisir ? "))  # pose la question sur le nombre étudiants
    noms = []  # Liste noms des étudiants
    notes = []  # Liste notes des étudiants
    
    for i in range(n):
        nom = input(f"Nom de l’étudiant {i + 1} : ")  # nom de l'étudiant
        note = float(input(f"Note de {nom} : "))  # note de l'étudiant
        noms.append(nom)  # Ajoute nom à la liste
        notes.append(note)  # Ajoute note à la liste
    
    return noms, notes  # Retourne deux listes

noms, notes = saisir_donnees()
print("Noms des étudiants :", noms)
print("Notes des étudiants :", notes)
