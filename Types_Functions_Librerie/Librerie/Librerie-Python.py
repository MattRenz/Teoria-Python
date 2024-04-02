# dir() elenca tutti i nomi definiti appartenenti al modulo della piattaforma
import datetime
x = dir(datetime)

import subprocess # Consente di scrviere sul terminale tramite Pytonh

# fornisce un'interfaccia per creare e gestire processi secondari (child process) 
# all'interno di un programma Python. Consente di eseguire comandi di sistema, 
# programmi esterni e comunicare con essi attraverso i flussi di input/output.

    # Scrivere sul terminale da python 
    
output = subprocess.check_output(["ls", "-l"]) # comando 
print(output.decode("utf-8"))  # Decodifica l'output byte in una stringa UTF-8 e stampa

try:
    output = subprocess.check_output(["command_does_not_exist"]) # Risposta comando
except subprocess.CalledProcessError as e:
    print("Errore durante l'esecuzione del comando:")
    print("Codice di uscita:", e.returncode) 
    print("Output di errore:", e.output.decode("utf-8")) # Risposta erroe comando

    




import pyperclip # Consente di copiare il contenuto di una stringa in memoira

pyperclip.copy("Testo da copiare")

# Ottieni il contenuto dalla clipboard e assegnalo a una variabile
contenuto = pyperclip.paste()

print(contenuto)


import requests 
'''
Consente di inviare richieste HTTP utilizzando Python, 
'''

x = requests.get('https://w3schools.com/python/demopage.htm')
print(x.text)

 
import math #operazioni matematiche 

math.sqrt() # radice quadrata di un numero


import csv # per leggere e scrivere file CSV

# LETTURA FILE CSV con reader() e next()

fileProva = "fileTest.csv"

with open(fileProva, "r") as file:
    
    reader = csv.reader(file) # con csv.reader() leggiamo un file CSV
    
    primariga = next(reader) # con next() andaimo avanti la riga del file
    secondariga = next(reader)



import unittest # definisce una classe che permette di inserire un insieme di procedure di test da eseguire prima dell'avvio del programma

unittest.TestCase() # unittest.TestCase = E' una classe che fornisce un modo per definire test, fornisce alcuni metodi:

#assertEqual() = Confronta il primo argomento con il secondo argomento se sono uguali CONTINUA altrimenti solleva un'eccezione

# assertNotEqual() = Confronta il primo argomento con il secondo se NON sono uguali CONTINUA altrimenti solleva un'eccezzione

# assertTrue() = Verifica se l'istruzione data è vera e solleva un Errore se l'istruzione data è falsa

# assertFalse() = Verifica se l'istruzione data è falsa e solleva un Errore se l'istruzione data è vera



import scipy # per funzioni scinetifiche e matematiche derivate da NumPy 

from scipy import stats 
stats.linregress(x, y) #  metodo che resituisce alcuni importanti valori chiave della regressione lineare 


import pendulum 
"""  
simile a datetime gestisce date e orari rendendo più faciel fare codifiche più complesse, gestisce in automatico i fusorari
"""


from colorama import Fore # colora le stringhe con il colore che gli passiamo (i colori disponibili sono solo qeuelli elnecati qui sotto)

print(Fore.RED + "Ciao")
print(Fore.BLUE + "Ciao")
print(Fore.GREEN + "Ciao")
print(Fore.WHITE + "Ciao")
print(Fore.BLACK + "Ciao")
print(Fore.CYAN + "Ciao")
print(Fore.YELLOW + "Ciao")
print(Fore.MAGENTA + "Ciao")


import getpass

""" 
E' una libreria che permette di ottenere in modo sicuro e riservato l'input dell'utente, come per esempio la password
"""

def crypt_input(pswd):
    
    return getpass.getpass(prompt=pswd, stream=None) # nasconde l'input dell'utetne e lo restituisce come stringa

    #prompt = specifica la strnga di testo che deve essere mostrato all'utente 
    
    
    


from sklearn.datasets import load_

"""  
La libreria contiene diversi dataset di esempio, come il dataset Iris, il dataset delle cifre scritte a mano (MNIST), 
il dataset delle facce Olivetti, il dataset dei prezzi delle case di Boston, il dataset delle recensioni di film IMDB e molti altri 

La libreria sklearn.datasets è utile per gli sviluppatori di apprendimento automatico in quanto consente loro di testare e sviluppare 
algoritmi di apprendimento automatico su dataset di esempio senza la necessità di acquisire o creare i propri dati 

"""


import seaborn 

""" 
La  libreria seaborn è una libreria di visualizzazione dei dati Python, che si integra con Pandas e matpolib 
crea grafici, e diagrammi di rappresenttazione
"""

seaborn.load_dataset() 
# permette agli utenti di caricare rapidamente un dataset di esempio dalla libreria e utilizzarlo per analisi e visualizzazione di dati

seaborn.pairplot() 
# funzione che permette di creare facilmente un grafico a matrice di scatterplot per esplorare i dati e individuare eventuali correlazioni tra le variabili

seaborn.heatmap() 
# funzione che permette di creare rapidamente una mappa di calore a due dimensioni per visualizzare i dati e analizzare la correlazione tra le varaibili in un dataframe di Pandas.

seaborn.pairplot()
# Crea grafici a griglia a dispersione che mostrano la relazione bivariata tra coppie di varaibli, si possono individare eventualii correlazioni tra le variabili.


