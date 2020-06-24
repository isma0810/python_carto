 demandes d' importation
import  config  as conf
import  config

baseurl = 'http://api.openweathermap.org/data/2.5/weather?appid=' + conf . apikey  +  "& units = metric"
baseurl = 'http://api.openweathermap.org/data/2.5/weather?appid=' + config . apikey  +  "& units = metric"

def  get_locations ( nom de fichier ):
    # Identique à 01_carto.py
@@ -32,6 +32,14 @@ def get_area (emplacements):
        lat_max = max ( lat_max , emplacement [ 'lat' ])
        lon_min = min ( lon_min , emplacement [ 'lon' ])
        lon_max = max ( lon_max , emplacement [ 'lon' ])
    # ajout d'une bordure (10%):
    o_lat  = (( lat_max  -  lat_min ) / 100 ) * 10
    o_lon  = (( lon_max  -  lon_min ) / 100 ) * 10
    lat_min = lat_min - o_lat
    lat_max = lat_max + o_lat
    lon_min = lon_min - o_lat
    lon_max = lon_max + o_lat

    # enfin, retourner directement une liste
    return { 'lat_min' : lat_min , 'lat_max' : lat_max , 'lon_min' : lon_min , 'lon_max' : lon_max }

def  get_weather ( c ):
    # Identique à 01_carto.py
    url  =  baseurl  +  "& lon =" + c [ "lon" ] +  "& lat =" + c [ 'lat' ]
    météo = demandes . récupérez ( url ). json ()
    c [ "temp" ] = météo [ 'principale' ] [ 'temp' ]
    retour  c
def  main ():
    # 1 - Obtenez les emplacements du fichier:
    locations  =  get_locations ( 'lonlat.txt' )
    # 2 - ajoutez la météo pour chaque point:
    pour l'  emplacement  dans les  emplacements :
        location  =  get_weather ( emplacement )
    # 3 - Obtenez la limite de la zone:
    area  =  get_area ( emplacements )
    print_dict ( zone , "AREA" )
    # 4 - Obtenez la carte (selon les limites)
    # MAINTENANT, nous avons toutes les données dont nous avons besoin, plus de demande d'API!
    # 4 emplacements d'affichage (impression):
    nbligne = 0
    pour l'  emplacement  dans les  emplacements :
        nbligne = nbligne + 1
        sep  =  "LIGNE% d"   %  nbligne
        print_dict ( emplacement , sep )
si  __name__  ==  "__main__" :
    main ()