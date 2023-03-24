import requests
import dotenv
import os

# chargement de fichier .env contenant les variables d'environnement
dotenv.load_dotenv('.env')

# initialisation de session pour les requetes
session_start = requests.Session()

# url de l'api
url = "https://api.jcdecaux.com/vls/v1/stations"


def get_all():

    """
        Cette fonction fait une requete GET à l'api et 
        afficher toutes les info d'un vélo
    """

    # parametre à passer en url
    params = {'apiKey': os.getenv('API_KEY')}

    # faire une requete GET à url avec les parametre
    res = session_start.get(url, params=params)

    # la réponse GET est transformé en json. 
    data_json = res.json() #une liste de dictionnaire python

    # iteration de la liste puis afficher les info dans la console
    for i in data_json:
        try:
            # calcul de % de station de vélo disponible
            percent = round(int(i.get('available_bike_stands')) / int(i.get('bike_stands')) * 100, 2)
        except ZeroDivisionError:
            pass
        else:
            print(f"Ville................... {i.get('contract_name')}")
            print(f"Adresse................. {i.get('address')}")
            print(f"Station vélo............ {i.get('bike_stands')} - {percent}% disponible")
            print(f"Nom de station.......... {i.get('name')}")
            print(f"Vélo disponible......... {i.get('available_bikes')}")
            print(f"État.................... {i.get('status')}")
            print('--'*20)




#+++----------------| Recherche par nom de ville |---------------+++#

def research_by_city_name(city):

    """
        Cette fonction fait une requete GET à l'api et 
        affiche les info d'une ville spécifique
    """


    # parametre à passer en url
    params = {'contract': city, 'apiKey': os.getenv('API_KEY')}

    # faire une requete GET à url avec les parametre
    res = session_start.get(url, params=params)

    # la réponse GET est transformé en json. 
    data_json = res.json() #une liste de dictionnaire python

    # iteration de la liste puis afficher les info dans la console
    for i in data_json:
        try:
            # calcul de % de station de vélo disponible
            percent = round(int(i.get('available_bike_stands')) / int(i.get('bike_stands')) * 100, 2)
        except ZeroDivisionError:
            pass
        except AttributeError:
            print(f"\033[33mLa ville que vous avez saisi n'existe pas :\033[00m \033[41m{city}\033[00m")
        else:
            print(f"Ville................... {i.get('contract_name')}")
            print(f"Adresse................. {i.get('address')}")
            print(f"Station vélo............ {i.get('bike_stands')} - {percent}% disponible")
            print(f"Nom de station.......... {i.get('name')}")
            print(f"Vélo disponible......... {i.get('available_bikes')}")
            print(f"État.................... {i.get('status')}")
            print('--'*20)




#+++----------------| Rechercche >= 10 vélos |---------------+++#


def research_by_plus_10():

    """
    cette fonction
    Recherche les villes où il y a  plus ou égal 10 vélos disponible
    """

    # parametre à passer en url
    params = {'apiKey': os.getenv('API_KEY')}

    # faire une requete GET à url avec les parametre
    res = session_start.get(url, params=params)

    # la réponse GET est transformé en json. 
    data_json = res.json() #une liste de dictionnaire python

    # iteration de la liste puis afficher les info dans la console
    for i in data_json:
        try:
            # calcul de % de station de vélo disponible
            percent = round(int(i.get('available_bike_stands')) / int(i.get('bike_stands')) * 100, 2)
        except ZeroDivisionError:
            pass
        else:
            # verification si les vélos disponible sont >= 10
            if int(i.get('available_bikes')) >= 10:
                print(f"Ville................... {i.get('contract_name')}")
                print(f"Adresse................. {i.get('address')}")
                print(f"Station vélo............ {i.get('bike_stands')} - {percent}% disponible")
                print(f"Nom de station.......... {i.get('name')}")
                print(f"Vélo disponible......... {i.get('available_bikes')}")
                print(f"État.................... {i.get('status')}")
                print('--'*20)