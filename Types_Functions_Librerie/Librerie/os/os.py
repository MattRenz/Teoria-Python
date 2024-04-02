import datetime
import os # continee funzioni per far integrare il progrmama con il sistema operativo del computer (Windows, Linux, Mac OS)

os.listdir() # restituisce una cartella (directory) specificata

os.remove("Nomefile") # rimuovi file

os.getlogin() # restitusice l'user che sta usando il pc

os.path.isfile() # restitusice True se il file che gli passiamo esiste. Restituisce False se l file che gli passiamo non esiste

os.path.exists() #restituisce True se il file che gli passiamo eesiste. 

os.rmdir("NomeCartella") # rimuovi cartella (vuota)

os.name # restituisce il nome del siastema operativo
"nt" # se un sistema operativo Windows 
"posix" # se un sistema operativo Unix-like, come Linux o macOs

file = "path"
os.path.getctime(file) # restituisce la data di creazione del file che gli passiamo, la restituisce in formato Unix (valore numerico)

datetime.datetime.fromtimestamp() # converte il valore Unix in un valore data più leggibile

nome_cartella = "nome_cartella"
os.mkdir(nome_cartella) # crea una nuova cartella di nome "nuova cartella" nella directory corrente del programma

os.getcwd() #restituisce il percorso corrente dell'utente

"""
Se da terminale andiamo a effetuare il comando "set" possiamo vedere i vari percorsi e dati del nostro pc, utili per richiamarli da python, esempio:

io voglio ottenre l'username del pc corrente posso fare os.getenv('USERNAME')

"""

os.getenv() # andando a inserire i nomi delle variabili (presenti sul terminale con il comando set) possiamo ottenere il corrispettivo della variabile

os.path.realpath(__file__) # percorso assoluto del file corrente

file_path = ""
os.path.dirname(file_path) # percorso assoluto di una cartella in cui si trova un file specifico

os.chdir(file_path) # Camia la directory corrente, cambia l'ambiente di lavoro del terminale 

 