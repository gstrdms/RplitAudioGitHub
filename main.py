import requests

url = " https://files.freemusicarchive.org/storage-freemusicarchive-org/music/Oddio_Overplay/MIT_Concert_Choir/Carmina_Burana/MIT_Concert_Choir_-_01_-_O_Fortuna.mp3"

r = requests.get(url)
with open("o_fortuna.mp3", "wb") as f:
    f.write(r.content)