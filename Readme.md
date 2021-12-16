# Harjoitustyö

Ohjelmoinnin perusteet-kurssin (TTC2030) harjoitustyöni on kysymys&vastaus-peli. 

### Kuvaus

Peli on rakennettu pääohjelma-aliohjelma ajatuksella. Eli pääohjelman sisällä starttaa aliohjelma, jonka sisällä
kännistyy toinen aliohjelma jne. Ohjelma on kysy&vastaa-peli, joka kysyy alussa käyttäjän nimeä ja tervehtii häntä 
annetulla nimellä. Tämän jälkeen siirrytään aliohjelmaan, jossa kysytään käyttäjältä haluaako hän ottaa kysymyskortin 
vai ei. Jos vastaus on kielteinen, peli päättyy. Jos taas käyttäjä päättää ottaa kortin, käynnistyvä aliohjelma 
pyytää häntä valitsemaan numeron 1-30 väliltä. Numeron perusteella ohjelma avaa tekstitiedoston ja hakee numeroa 
vastaavalta riviltä kysymyksen tulostaen sen käyttäjälle. Seuraavaksi ohjelma arpoo toisesta tekstitiedostosta 
satunnaisen vastauksen kysymykselle käyttäen random-moduulia. Tämän jälkeen ohjelma palaa takaisin edelliseen aliohjelmaan
eli käyttäjällä on jälleen edessä valinta; ottaako uuden kysymyksen vai lopettaako pelin. Ohjelma siirtyy viimeiseen 
aliohjelmaan käyttäjän lopulta halutessa lopettaa pelin käyttämisen. Valitut kysymykset ja arvotut vastaukset ohjautuvat 
kumpikin omiin listoihinsa, jotka näytetään allekkain ohjelman päättyessä. Lopuksi toivotellaan: "Nähdään taas!". 

Peliin jäi vielä kehitettävää. Jos käyttäjä vastaa ensimmäiseen kysymykseen kielteisesti eikä ota yhtään korttia,
tulostuu loppuyhteenvedoksi 'Kysymyksesi olivat:' ja 'Vastaukset olivat:' luonnonllisesti ilman listoja. Ajan 
rajallisuuden vuoksi, jäi ratkaisematta kuinka koodi olisi pitänyt kirjoittaa, jotta nuo otsikkot olisi voinut välttää.

### Käytetyt menetelmät

Ohjelmassa on käytetty laajasti kurssilla opittuja asioita mm.
* muuttujat
* vuorovaikutus loppukäyttäjän kanssa (input)
* kokoelmien käyttö (lista)
* ohjausrakenteet (while, for, if-elif-else)
* funktiot ja niiden kutsuminen 
* poikkeusten käsittely (try - except)
* tiedostojen käyttö 
* Python-kirjastojen käyttö (random, time)
* koodin kommentointi

### Harjoityöhön liittyvät tiedostot:

* kysymyspeli.py
* kysymykset.txt
* vastaukset.txt
