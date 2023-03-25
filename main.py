import sys
import velo

# verification si la version de python est inférieur à 3
if sys.version_info[0] < 3:
    print("""
          CE SCRIPT REQUIERT PYTHON 3.X.X

          AUTEUR  : Makan DIANKA
          CONTACT : www.makandianka.com#contact
          """
          )
    sys.exit()


# verification de système d'exploitation de l'utilisateur
if sys.platform != "linux":
    print("""
        Il semble que vous n'êtes pas sur linux.

        Certain syntax colorique risque de ne pas fonctionner sur votre système.
        """
        )
        
    print("souhaitez-vous continuer ?")
    q = input("(O) OUI, (N) NON. [O]> ")

    if q.lower() not in ['o', 'oui', '']:
        print("vous avez choisi de ne pas continuer.")
        sys.exit()



# information du script
print("\nCe script vous permet de faire une recherche de disponibilité des vélos par ville et autre. Voir les commands ci-après.")

# les commands valable dans la console
print("\nCommands : \n * (A) pour voir tout\n * (C) pour faire une recherche par ville \n * (P10) pour voir toutes les villes disposant plus de 10 vélos\n")

# recuperation de la saisi de l'utilisateur 
user_input = input('Command > ')


# verification si la command tapé par l'utilisateur est a
if user_input.lower()=="a":
    velo.get_all() # appel de la fonction get_all depuis le fichier velo

# verification si la command tapé par l'utilisateur est p10
elif user_input.lower()=="p10":
    velo.research_by_plus_10() # appel de la fonction research_by_plus_10 depuis le fichier velo

# verification si la command tapé par l'utilisateur est c
elif user_input.lower()=="c":

    # demander le nom d'une ville à l'utilisateur 
    city = input("Saisissez une ville > ")
    if city:
        # si l'utilisateur a saisi quelque chose la fonction research_by_city_name est appelé
        velo.research_by_city_name(city)
    else:
        print("Veuillez saisir le nom d'une ville")
else:
    print(f"La command que vous avez saisi n'existe pas : {user_input}")
    print("Taper uniquement les commands disponible ci-dessus")
