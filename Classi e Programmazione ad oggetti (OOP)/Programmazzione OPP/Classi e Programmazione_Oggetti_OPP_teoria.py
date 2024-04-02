
# Programma 01 (versione normale)

'''
a = input("inserisci numero: ")

b = input("inserisci secondo numero: ")

c = int(a) / int(b)

print(f'Risulatato della divisione è {c}')
'''

# Programma 02 (versione con prototipo)

def eseguiDivisione(dividendo, divisore):
    
    c = dividendo / divisore
       
    return c

a = input("inserisci numero: ")

b = input("inserisci secondo numero: ")

risultato = eseguiDivisione(int(a), int(b)) # richiamo prototipo 

print(risultato)
    
    
'''
Programmazzione OPP è visto come un insieme di OGGETTI un oggetto
può avere attributi e metodi associati.
Classe = oggetti che ha attiributi questi attributi hanno dei metodi che elaborano i risultati
'''

# Crezione classe:

class Studente: # creiamo la classe stuente 
    
    def __init__(self, nome, cognome, eta):  # __init__ = costruttore di oggetti 
        
        self.nome = nome
        self.cognome = cognome  # self = variabile che indica l'istanza corrente della classe
        self.eta = eta
        
    def SchedaPersonale(self): 
        return f"Scheda Studente\n Nome:{self.nome}\n Cognome: {self.cognome} \n Eta: {self.eta}"
        
        
        
# Studente 1 = variabile decisa da noi, che richiama la classe studente. Possiamo creare centinaia di variabili che richiamano la classe studente

Studente1 = Studente("Mario", "Rossi", 20) # nella classe Studente ci sono 3 attributi (nome, cognome, eta) e noi gli passiamo 3 attributi nome cognome ed età
Studente2 = Studente("Marco", "Bianchi", 21)
        
        
print(Studente1.nome) # stampa il nome che abbiamo assegnato a Studente1 
        
print(Studente1.SchedaPersonale()) #stampa gli attributi di studente 1 con il metodo SchedaPersonale


print(Studente2.SchedaPersonale())




        
    

    
        