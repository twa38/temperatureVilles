# coding: UTF-8
# Imports
import mysql.connector
import requests
import time

# Fonctions
def get_temperature(ville):
    url = "http://api.openweathermap.org/data/2.5/weather?q="+ville+",fr&units=metric&lang=fr&appid=0a73790ec47f53b9e1f2e33088a0f7d0"
    return float(requests.get(url).json()['main']['temp'])

def get_pression(ville):
    url = "http://api.openweathermap.org/data/2.5/weather?q="+ville+",fr&units=metric&lang=fr&appid=0a73790ec47f53b9e1f2e33088a0f7d0"
    return float(requests.get(url).json()['main']['pressure'])

def set_temperature_bdd(temperature, pression, ville):
    cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='bdd_temperaturevilles')
    cursor = cnx.cursor()
    update_temperature = ("UPDATE temperaturevilles SET temperature = (%s), pression = (%s) WHERE ville = (%s)")
    data_temperature = (temperature, pression, ville)

    cursor.execute(update_temperature, data_temperature)

    cnx.commit()
    cursor.close()
    cnx.close()

# Programme principal
def main():
    time.sleep(1)
    listeVilles = ['grenoble', 'meylan', 'lyon']
    for ville in listeVilles:
        temperature = get_temperature(ville)
        pression = get_pression(ville)
        print('A', ville, ' Température = ', temperature, '° et Pression =  ', pression, 'hpa.')
        set_temperature_bdd(temperature, pression, ville)
if __name__ == '__main__':
    main()
# Fin
