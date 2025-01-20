#Projet_difference_entre_paradigmes_python : version impératif

#recettes et de leurs ingrédients
recettes = {
    "pizza": ["farine", "eau", "sel", "levure", "tomate", "fromage"],
    "pates_carbonara": ["pates", "creme", "lardons", "fromage", "sel", "poivre"],
    "omelette": ["oeufs", "sel", "poivre", "fromage", "herbes"],
    "sandwich": ["pain", "beurre", "jambon", "salade"]
}

#ingrédients disponibles et recettes 
def recettes_possibles(ingredients_disponibles):
    recettes_faites = []  # liste recettes 
    for recette, ingredients in recettes.items():
        if all(ingredient in ingredients_disponibles for ingredient in ingredients):
            recettes_faites.append(recette)  #ajout recette à la liste
    return recettes_faites

#pour tester
ingredients = ["farine", "eau", "sel", "levure", "tomate", "fromage"]
print("Recettes réalisables avec les ingrédients disponibles :", recettes_possibles(ingredients))  

ingredients = ["pates", "creme", "lardons", "fromage", "sel", "poivre"]
print("Recettes réalisables avec les ingrédients disponibles :", recettes_possibles(ingredients))

ingredients = ["oeufs", "sel", "poivre", "fromage", "herbes"]
print("Recettes réalisables avec les ingrédients disponibles :", recettes_possibles(ingredients))  

ingredients = ["pain", "beurre", "jambon", "salade"]
print("Recettes réalisables avec les ingrédients disponibles :", recettes_possibles(ingredients))  
