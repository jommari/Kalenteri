# Nyt harjoitellaan tkinterin käyttöä.

from tkinter import Tk, Canvas
from datetime import date, datetime

# Funktio noutaa tapahtumat tapahtumat.txt-tiedostosta ja palauttaa tapahtumat listana.
def get_events():
    list_events = [] # Luodaan lista-muuttuja tapahtumien listaamiseksi.
    with open('tapahtumat.txt') as file: # Avataan tiedosto turvallisesti muuttujaan file.
        for line in file: # Käydään tiedosto läpi rivi kerrallaan.
            line = line.rstrip('\n') # Poistetaan \n jokaisen rivin .lopusta.
            current_event = line.split(',') # Jaetaan rivin merkkijono pilkun kohdalta kahdeksi merkkijonoalkioksi jotka tallennetaan muuttujaan.
            event_date = datetime.strptime(current_event[1], '%d/%m/%y').date() # Muunnetaan current_event-muuttujan toinen alkio päivämäärätyyppiseksi ja tallennetaan se event_date-muuttujaan.
            current_event[1] = event_date # Lisätään event_date-muuttujan sisältö current_event-muuttujan toiseen alkioon.
            list_events.append(current_event) # Lisätään current_event-muuttujan sisältö list_events-listaan
    return list_events

def days_between_dates(date1, date2):
    time_between = str(date1 - date2) # datetime-moduuli suorittaan päivämäärien välisen erotuksen joka tallennetaan merkkijonona muuttujaan.
    number_of_days = time_between.split(' ') # Merkkijono jaetaan kolmeen alkioon välilyöntimerkkien kohdilta.
    return number_of_days[0]

# print(get_events()) # Tulostaa get_events-funktion palauttaman listan sisällön komentoriville.

# Ohjelmaruudun initialisointi
root = Tk()
c = Canvas(root, width=800, height=800, bg='black')
c.pack()
c.create_text(100, 50, anchor='w', fill='white', font='Arial 28 bold underline', text='Lähtölaskentakalenteri')

# Haetaan nykyinen päivämäärä


# Luodaan tärkeiden tapahtumien luettelo tekstitiedostosta


# Haetaan tapahtuma


# Lasketaan montako päivää tapahtumaan on jäljellä


# Näytetään tulos


# Tarkistetaan onko kaikki tapahtumat käsitelty, jos ei --> haetaan tapahtuma, muutoin lopetetaan
