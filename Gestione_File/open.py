import os
import datetime

""" 
r = Lettura, errore se il file non esiste

a = Scrivi, crea il file se non esiste

x = Crea il file specificato, restituisce un errore se il file esiste

"""

# LETTURA FILE PYTHON

nomeFile = "TestLettura.txt"

f = open("TestLettura.txt", "r")

f = open("C:\home\desktop\myfiles\file.txt", "r") #nel caso dobbiamo specificare il percorso

f = open(nomeFile, "rb") # read binary, stiamo leggendo il file come una sequenza di byte, senza interpretarli come una stringa di testo

print(f.read()) # legge il file

print(f.readline()) # restituisce una riga

for x in f:
    print(x) # scorrendo le righe del file puoi leggere puoi leggere l'intero file riga per riga

f.close() # è buona nora chiudere il file una volta finito



# SCRITTURA FILE PYTHON 

# scrittura  
f = open("TestScrittura.txt", "a")

f.write("Sto scrivendo dentro il file python") # scrittura dentro il file Python
f.close()

f = open("TestScrittura.txt", "r")
print(f.read())

f.write(nomeFile, "wb") # write binary, scrive su file binari, e il contenuto del file sarà un contenuto binario. 

# sovrascrivere 
f = open("TestScrittura.txt", "w") # sovrascrivo il file, cancello ciò ceh sta dentro

f.write("Sovracrivo sopra il file")

f = open("TestScrittura.txt", "r")
print(f.read())


# CREA NUOVO FILE 

f = open("NuovoFile.txt", "x") # crea un nuovo file vuoto 


# ELIMINA FILE 

import os

os.remove("NomeFile.txt")

# ELIMNA CARTELLA 

os.rmdir("NomeCartella") # solo per cartelle vuote 


# DATA CREAZIONE FILE 

os.path.getctime(f) # restituisce la data di creazione del file che gli passiamo, la restituisce in formato Unix (valore numerico)

datetime.datetime.fromtimestamp() # converte il valore Unix in un valore data più leggibile


""" 
Un altro modo per aprire, leggere, o scrivere un file è il segeunte, 
Questo metodo chiudera in automatico il file alla fine dell'esecuzione
"""

# Scrittura FILE

with open(nomeFile, "w") as file:
    
    file.write("conetnutoFile")
    
# Lettura FILE 

with open(nomeFile, "r") as file:
    
    file.readline()
    

    
# TIPI FILE
    

""""
xml
csv
json

"""

# XML (obbiettivo rappresentare dei dataset)

""" 
<persona>

<nome>Mario</nome>
<cognome>Rossi</cognome>

<data_nascita>
<giorno>21</giorno>
<mese>12</mese>
<anno>2000</anno>
</data_nascita>

</persona>


XSD Affianca XML e obblia a dargli dei parametri, 
esempio data_nascita non è obbligatorio ma se lo inseriamo dobbiamo
inserire i parametri giorno, mese, anno

"""


# CSV

"""  

nome;cognome;data_nascita
Mario;Rossi;21/12/2000
Gianni;Rivera;12/07/1943

"""


# JSON (usato nei microservizi)

""" 

{"nome":"Mario","age":"30"}

"""