#VARIABILE

#Assegnazione variabile
a = 5 
b = "Cinque"
a = True 
a = a + b                           #somma di più vaariabili
x, y, z = "Mela" "Pera" "Banana"    #assegnazione di più variabili in una riga
x, y, z = "Variabili"               #Assegnazione dello stesso valore a più variabili

auto = ["Supra", "Ford", "Opel"]
x, y, z = auto                      #print(x) = "Supra"

#le variabili all'interno delle funzioni fanno riferimento SOLO alla funzione es: 
x = 5 # x = 5 
def Funzione():
    global x    #con global dichiariamo una variabile globale 
    x = 6       # x = 6 
    
print()  #stampa a video 

print(type(a))  #il tipo di variabile 

a = input("Scrivi una frase")  #asssegna una risposta a una variabile 


#FUNZIONI

#def funzione():  dichiarazione di una funzione 


#ESEMPIO Procedure 
def Somma(a,b): # prende in input due numeri
    
    c = a + b 
    
    return c # da in output la somma dei due numeri


def RichiestaTessera(sNome,sCognome,sCodiceFiscale):
    
    
    return #iNumTessera 

# ESEMPIO richiamo procedure
RichiestaTessera("Matteo", "Renzi", "CF")



# Richiamo funzione
def funzione(nome, cognome):
    print(nome + " " + cognome)
nome = input(" ")
cognome = input(" ")
funzione(nome, cognome)

# Argomento
def funzione(nome):
    print("Ciao" + nome)
funzione("Matteo")

# Più argomenti 
def studente(nome, cognome):
    print("Studente: " + nome + " " + cognome)
studente("Matteo", "Renzi")

def funzione(nome, cognome):
    frase = nome + " " + cognome 
    print(frase)
studente1 = funzione("Matteo", "Renzi") 
stundente2 = funzione("Davide", "Renzi")

#Argomento arbitrario
def studente(nome, eta, *voti: int): # con * indichiamo che l'argomento, non è fisso ma variabile, cioè che può essere "richiamato" più di una volta. Va inserito solamente alla fine. 
    pass

# Importare una funzione
# per importare una funzione serveno che siano nella stessa cartella 
def funzione1(): 
    pass


import funzione_prova as proc # con questo importiamo la funzione (che è su un altro file) nella nostra funzione

# proc.funzione_prova(numero) con questo richiamiamo la funzione inerente alla variabile presente nell'altra funzione, 


# GENERIC PROGRAMMING

""" 
Il generic programming è la capacitò di scrivere un codice che possa essere utilizzato per ogni tipologia di dati, 
senza la necessità di scrivere il codice per ogni dato. 

Ad aiutarci a fare ciò possiamo usare la funzione type() che riconosce qualsiasi tipo di dato gli stiamo passando, 
e una volta riconosciuto possiamo regolarci di coneguenza. 
""" 

sommaDatiStr = "59,44,26,29"
sommaDatiInt = [24,64,87,49]
sommaDatiDict = {"chiave1": 54, "chiave2": 94, "chiave3": 39, "chiave4":42}

def SommaDati(data):

    if type(data) == str: # se è di tipo srtinga esegui la funzione per le stringhe

        return sommaDatiStr(data)
        
    if type(data) == list: # se è di tipo lista esegui la funzione per le liste, e così via.

        return sommaDatiInt(data)
    
    if type(data) == dict:

        return sommaDatiDict(data)
    
    









#OPERATORI
#somma: + / sottrazione: - / moltiplicazione: * / divisione: / / Modulo (resto della divisione): % / Divisione senza resto: // 
# + nelle stringhe è una concatenazione 
# * esponenziale delle stringhe  
# Uguale a: == / Diverso da: != / not / and / ora / is not / is
