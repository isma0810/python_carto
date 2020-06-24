import requests


api='&appid=41277c201c7b5fa059cf3787111966c8'
base_url='http://api.openweathermap.org/data/2.5/weather?'+api+"&units=metric"
# tout ca c'est sympa mais autant le sortir du fichier :


def get_location():
    lonlat=open(r'C:\Users\Therese\Desktop\lonlatonly.txt', 'r')
    geocode=[]  #création du tableau vide
    for line in lonlat:
        lat,lon=line.split(",")  #séparation des infos dans la ligne
        coord={"lng":lon.strip(),
        "ltt": lat
                }
                # le .strip pour supprimer ('ce qui nous interesse)
        geocode.append(coord)     # fonction append qui permet d'ajouter au tableau
    print(geocode)
    return(geocode) # = voici le resultat, python nous renvoie ça


def get_weather(c):      #creation de la fonction
    lat = c['ltt']
    long = c['lng']
    url=base_url+"&lat="+lat+"&lon="+long
    data=requests.get(url).json()
    return(data)
#NOS FONCTIONS SONT DEFINIS
coords=get_location()    #"coords" est le resultat du tableau
w=get_weather(coords[0])
print(w)