#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> bool:
    if values is None:
        # TODO: Demander les valeurs ici
        values = [input("Entrez ...") for _ in range(10)] # compréhension de liste

    return values == sorted(values)     # ou == values.sort()


def anagrams(words: list = None) -> bool:
    liste1, liste2 = [], []
    if words is None:
        chaine1 = input('Entrez le premier mot : ')
        chaine2 = input('Entrez le deuxième mot : ')
        liste1, liste2 = sorted(list(chaine1)), sorted(list(chaine2))

    return liste1 == liste2


def contains_doubles(items: list) -> bool:
    is_double = False
    for element in items:
        if items.count(element) > 0 :
            is_double = True
    return is_double


def best_grades(student_grades: dict) -> tuple:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    return nom, note


def histogram(sentence: str) -> tuple:
    # TODO: Créer l'histogramme a l'aide d'un dictionnaire
    #       Afficher l'histogramme et les lettres les plus fréquentes
    #       Retourner l'histogramme et le tableau de lettres

    return {}, []


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingrédients et enregistrer dans une structure de données 
    pass


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    pass


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    print(f'Les valeurs sont ordonnées : {order()}')

    print(f"On vérifie les anagrammes...")
    if anagrams() :
        print(f'Les deux mots sont des anagrammes.')
    else:
        print('Les deux mots ne sont pas des anagrammes.')

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    #grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    #name, result = best_grades(grades)
    #print(f"{name} a la meilleure moyenne: {result}")
    
    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
