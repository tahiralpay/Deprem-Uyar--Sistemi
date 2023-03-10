import requests
from bs4 import BeautifulSoup
import pywhatkit as kit
import datetime
import time

url = "http://www.koeri.boun.edu.tr/scripts/lst0.asp"
an = datetime.datetime.now()
saat = an.hour
dakika = an.minute
i = 0
son_deprem = 0

while True:
    response = requests.get(url)
    content = response.content

    soup = BeautifulSoup(content, "html.parser")

    pre = soup.find("pre")
    text = pre.text
    liste = text.split("\n")

    deprem = liste[10][60:63]
    deprem_zamani = liste[10][0:19]
    konum = liste[10][71:118]

    message = "Depremin Buyuklugu: ", deprem, "Deprem Saati: ", deprem_zamani, "Depremin konumu: ", konum

    if(son_deprem == deprem) and (i == 1):
        i = 0

    if (son_deprem != deprem) and (i == 0):
        son_deprem = deprem
        i = 1
        print("  ")
        print(deprem_zamani)
        print(deprem) 
        print(konum) 

    if(float(son_deprem) >= 3.0 and (i == 1)):
        kit.sendwhatmsg("+905431464431", str(message), saat,(dakika+1))
        print("UYARI GONDERILDI !!!")
        son = deprem
        i = 0

    time.sleep(10)
