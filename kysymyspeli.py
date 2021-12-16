#Harjoitustyö - Kysy&vastaa-peli

#Tuodaan time ja random moduulit.
import random  
import time 

#Esitellään tyhjät listat
kysymykset = []
vastaukset = []

#Määritellään funktio heippa() - aliohjelma alkaa
def heippa():
    print()
    print("Kysymyksesi olivat: ")     
    for i in kysymykset:    #Tulostetaan valitut kysymykset allekkain konsoliin
        print(i, end="")
    print()
    print("Vastaukset olivat: ")            
    for i in vastaukset:
        print(i, end="")
    print()     
    print()     
    print("Nähdään taas!")
    return None
# Koko ohjelma päättyy

#Määritellään funktio numero() - aliohjelma alkaa
def numero():
    while True:        
        try:    #Aloitetaan poikkeuksen käsittely
            kortti = int(input("Valitse kysymysnumero (1-30): "))
            print()
            if kortti >= 0 and kortti <= 30:                
                tiedosto = open("kysymykset.txt", "r", encoding='utf-8')  #Avataan vastaukset.txt tiedosto lukemista varten ja määritellään käytettäväksi UTF8–koodausta               
                while (True):                   
                    rivi = tiedosto.readlines()  #Luetaan kaikki rivit - lopetetaan, kun tyhjä rivi tulee vastaan
                    if len(rivi) == 0:
                        break                    
                    kysymyskortti = rivi[kortti-1]  #Valitaan kysymyskortti indeksin mukaan
                    print(kysymyskortti)                
                    kysymykset.append(kysymyskortti)    #Lisätään kysymys listaan                                                    
                tiedosto.close()    #Suljetaan tiedosto 
                time.sleep(1)
                print("*********")
                print()
                time.sleep(1)
                tiedosto = open("vastaukset.txt", "r", encoding='utf-8')                
                while (True):
                    rivi = tiedosto.readlines()                
                    if len(rivi) == 0:
                        break                    
                    vastauskortti= random.choice(rivi) #Arvotaan vastauskortti tiedoston answers.txt riveistä
                    print(vastauskortti)
                    vastaukset.append(vastauskortti)                       
                tiedosto.close()
                time.sleep(2)                        
                break            
            else:
                print("Numero ei ollut oikealla välillä")
                continue          
        except (ValueError):    #Vääräntyyppinen syöte - käsitellään poikkeus 
            print("Valintasi ei ollut numero")
            continue
    return None
#Aliohjelma loppuu

#Aliohjelma alkaa - kysytään käyttäjältä haluaako hän kortin 
def kortti():    
    while True: #Jatketaan niin kauan kunnes tulee break
        kysymys = input("Haluatko ottaa kysymys-kortin? (k = kyllä / e = lopettaa pelin) ")
        if kysymys == "k":            
            numero()    #kutsutaan funktiota numero()
        elif kysymys != "e":
            print("Näppäilyvirhe. Vastaisitko uudestaan.")
            continue
        else:            
            heippa()    #Kutsutaan funktiota heippa()
            break
    return None

#Ohjelma alkaa - määritellään funktio 
def tervehdys():    
    print() #Lisätään tyhjä rivi luettavuuden vuoksi 
    print("Hei! Tämä on hauska Kysy&vastaa-peli. :)") 
    print()    
    time.sleep(1)   #Funktio sleep() lisää viiveen, joka on suluissa osoitettu numero sekunteina              
    name = input("Mikä sinun nimesi on? ") #Pyydetään syöte käyttäjältä 
    print()    
    print(f"Moikka {name}! Eiköhän aloiteta!")  #Käytetään f-merkkijonoa tulostukseen
    time.sleep(1)
    print()    
    kortti()    #Kutsutaan aliohjelmaa kortti()
    return None

#Kutsutaan pääohjelmaa
tervehdys()