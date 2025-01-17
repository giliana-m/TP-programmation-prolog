# Partie 1 : Saisie des données
def saisir_donnees():
    n = int(input("Combien d'étudiants souhaitez-vous saisir ? "))  #nombre d'étudiants
    noms = []  # Liste noms des étudiants
    notes = []  # Liste notes des étudiants
    
    for i in range(n):
        nom = input(f"Nom de l’étudiant {i + 1} : ")  # nom de l'étudiant
        note = float(input(f"Note de {nom} : "))  # note de l'étudiant
        noms.append(nom)  # nom à la liste
        notes.append(note)  # note à la liste
    
    return noms, notes  # Retourne deux listes

# Partie 2 : Calcul de la moyenne
def calculer_moyenne(notes):
    return sum(notes) / len(notes) if len(notes) > 0 else 0  # moyenne des notes

# Partie 4 : Meilleure note 
def trouver_meilleure_note(noms, notes):
    # l'étudiant avec la meilleure note
    meilleure_note_index = notes.index(max(notes))  # index de la meilleure note
    meilleur_etudiant = noms[meilleure_note_index]  # nom de l'étudiant avec la meilleure note
    meilleure_note = notes[meilleure_note_index]  # meilleure note
    return meilleur_etudiant, meilleure_note  # nom et la note de l'étudiant avec meilleure note



def main():
    #Partie 1 
    noms, notes = saisir_donnees()  # fonction de saisie
    
    #Partie 2 
    moyenne = calculer_moyenne(notes)  # Calcul de la moyenne
    print(f"La moyenne de la classe est de {moyenne:.2f}.")  # Affichage de la moyenne

    #Partie 4
    meilleur_etudiant, meilleure_note = trouver_meilleure_note(noms, notes)  # étudiant avec la meilleure note
    print(f"L’étudiant ayant la meilleure note est {meilleur_etudiant} avec {meilleure_note:.2f}.")  # Affichage étudiant avec meilleure note

if __name__ == "__main__":
    main()
