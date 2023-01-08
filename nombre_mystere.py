import random

essais = 5
nombre_mystere = random.randint(1,100)

print("Bienvenu dans le jeu du nombre mystére : ")
print("Vous avez 5 essais pour trouver un chiffre compris entre 1 et 100 ! Bonne chance !")


while True:
    user_choice = input("Choississez un chiffre : ")
    if not user_choice.isdigit():
        print("Veuillez entrer un nombre valide")
        continue

    user_choice = int(user_choice)


    if 1 < essais <= 5:
        if user_choice == nombre_mystere:
            print("Bravo ! Vous avez trouvé le nombre mystére.")
            break

        elif user_choice < nombre_mystere :
            essais -= 1
            print("Le nombre mystére est plus grand")
            print(f"Il vous reste {essais} essais pour trouver le nombre mystére")
            print(essais)

        elif user_choice > nombre_mystere :
            essais -= 1
            print("Le nombre mystére est plus petit")
            print(f"Il vous reste {essais} essais pour trouver le nombre mystére")
            print(essais)

    else:
        print(f"C'est perdu ! Le nombre mystére etait {nombre_mystere}")
        break

