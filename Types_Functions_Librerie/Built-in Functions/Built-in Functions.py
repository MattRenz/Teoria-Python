# abs() / restituisce il valore assoluto di un numero
x = abs(- 7.25)
print(x) #<7.25>

# iter() / crea un oggetto iteratore e stampa gli elementi
x = iter(["BMW", "Audi", "Supra"])
print(next(x)) #<BMW>
print(next(x)) #<Audi>
print(next(x)) #<Supra>

# all() / restituisce True se tutti gli elementi in un iterabile sono veri, altrimenti restiuisce False
lista = [True, True, True]
x = all(lista)
print(x) #<True>
# può essere anche applicato alle tuple, dizionari, liste. 

# any() / restituisce Ture se qualsiasi elemento in un iterabile è vero. Altrimetni restiuisce False
lista = [False, True, False]
x = all(lista)
print(x) #<True>

# ascii() / sostiuisce tutti i caratteri non ascii con caratteri di escape
x = ascii("Ciao mi chiamo Ståle")
print(x) #<'Min chiamo St\e5le'>

# bin() / restituisce la versione binaria di un numero specificato, il risultato inizierà con il prefisso 0b
x = bin(36)
print(x) #<0b100100>

# bool() / restiuisce il valore booleano di un oggetto specifico 
x = bool(1)
print(x) #<True>

# bytearray() / restituisce un oggetto bytearry 
x = bytearray(4)
print(x) #<b'\x00\x00\x00\x00'> 

# byte() / restuisce un oggetto bytes
x = bytes(4)
print(x)

# callable() / restiuisce True se l'ogetto specificato è richiamabile
def x():
    a = 5  
print(callable(x)) #<True>

# chr() / restituisce il carattere che rappresenta l'unicode speficito
x = chr(97)
print(x) #<a>

# delattr() / elimina l'attributo specificato dall'oggetto specificato
class Persona: 
    nome = "Matteo"
    eta = 20
    paese = "Italia"
    
delattr(Persona, "paese") 

# dict() / costruttore per creare un dizionario
dizionario = dict(nome = "Matteo", eta = 20, paese = "Italia")
print(dizionario)

# divmod() / restituisce una tupla contenente il quoziente e il resto quando l'argomento1 (dividendo) viene diviso per l'argoemento2 (divisore)
x = divmod(5, 2)
print(x) #<(2, 1)>

#enumerate() / prende una colezione per (es. tupla) e la restiuisce coeìme un esemio numerato
x = ("Porsche", "Supra", "BMW")
y = enumerate(x)
print(list(y)) 

# eval() / valuta l'espressione specificata, se l'espressione è un'istruzione Python legale, verrà eseguita
x = 'print(55)'
eval(x)

#exec() / stesso principio di eval(), acceta però grandi blocchi di 


# filter() / restituisce un iteratore in cui gli elementi vengono filtrati attraverso una funzione per verificare se l'elemento è accettato o no. es: 
eta = [17, 15, 14, 18, 25, 13, 27]
def funzione(x):
    if x < 18:
        return False
    else: 
        return True 
adulti = filter(funzione, eta) #filtro, confronta chi è al di sotto dei 18 anni nella lista eta, e lo riprota in una nuova lista

for x in adulti:
    print(x)

# float() / converte il valore specificato in un numero a virgola mobile
x = float(3) #<3.0>

# format() / consente di formattare parti selezionate di una stringa, come, l'input dell'utente o un dato di un database, es:
prezzo = 49
testo = "Il prezzo è {}"
print(testo.format(prezzo)) #ora le parentesi graffe sono un segnaposto di 49, il prezzo.

#è possibile anche aggiunge parametri all'inerno delle parentesi graffe es: 
testo = "Il prezzo è {:.2f}" #formattare il testo per visualizzare come un numero con due decimali

# si possono usare anche più valori, basta aggiungerli nel metodo format(): 
prezzo = 50
sconto = 20
quantita = 3
testo = "Quantita {} con uno sconto di {}, e un prezzo di {:.2f}"
print(testo.format(quantita, sconto, prezzo))  #metterli nel ordine che vogliamo vengono visualizzati. 

# puoi utilizzare i numeri di indice per essere sicuri che i numeri siano posizionati nell segnaposto coretto:

testo = "Quantita {0} con uno sconto di {1}, e un prezzo di {2:.2f}" #<l'indice fa riferimento al format() di sotto>
print(testo.format(quantita, sconto, prezzo)) #<{0} = quantità, {1} = sconto, {2} = prezzo>

# frozenset() / restiuisce un oggetto immutabile come se fosse un ogetto set, solo che immutabile.
mylist = ['apple', 'banana', 'cherry']
x = frozenset(mylist) # print <frozenset({'apple', 'cherry', 'banana'})>

# getattr() / restituisce il valore dell'attributo specificato dall'oggetto specificato
class Persona: 
    nome = "Matteo"
    cognome = "Renzi"
    eta = 20  
      
x = getattr(Persona, "eta")
print(x) # <20>

# hesattr() / restituisce TRUE se l'oggetto specificato ha l'attributo specificato ha l'attributo specificato altrimenti Flase:
class Persona: 
    nome = "Matteo"
    eta = 20
    paese = "Italia"
    
x = hasattr(Persona, "eta") #controlla se dentro la classe Persona è presente l'attributo "eta"
print(x) # <True>


# hex() / converte il numero specficato in un valore esadecimale
x = hex(255)
print(x) #<0xff>

# id() / Restituisce un ID univoco per l'oggetto specificato. 
'''
Tutti gli oggetti in Python hanno il proprio ID univoco.
L'id viene assegnato all'oggetto quando viene creato.
L'id è l'indirizzo di memoria dell'oggetto e sarà diverso ogni volta che si esegue il programma. (ad eccezione di alcuni oggetti che hanno un ID univoco costante, come numeri interi da -5 a 256)
'''
x = ('apple', 'banana', 'cherry')
y = id(x)
print(y) # questo Id cambia a ogni esecuzione del programma

# input() / chiede all'utente un input, e non continua finchè l'utetne non fornisce un input
username = input("Enter username:")
print("Username is: " + username)

# int() / converte un valore specificato in un numero intero 
x = int(3.5)
print(x) #<3>

# isinstance() / restiuisce se l'oggetto specificato è del tipo specificato o no, True se è vero, False se non è vero.
x = isinstance(3.50, int)
print(x) #<False>

# issubclass() / restituisce True se l'oggetto specificato è una sottoclasse dell'oggeto specificato altrimenti False
class MiaEta:
    eta = 20
class MioOggetto(MiaEta):
    nome = "Matteo"
    eta = MiaEta
        
x = issubclass(MioOggetto, MiaEta) #controlla se la classe MioOggetto è una sottoclasse di MiaEta
print(x) # <True>

# len() / restiuisce il numero di elementi in un oggetto, quando l'oggetto è una stringa restituisce il numero di caratteri nella stringa
mylist = ["apple", "orange", "cherry"]
x = len(mylist)
print(x) #<3>

# list() / costruttore per creare una lista
LaMiaLista = list(("Mela", "Pera", "Banana"))
print(LaMiaLista) #<['Mela', 'Pera', 'Banana']>

#map() / Esegue una funzione specificata per ogni elemento in una iterabile. L'elemento viene inviato alla funzione come parametro

def myfunc(a):  
  return len(a)

x = map(myfunc, ('apple', 'banana', 'cherry'))  #calcola la lunghezza di ogni parola nella tupla

print(x)
print(list(x))

# max() / restituisce il numero più grande, o il valore più alto, o l'elemento con il valore più alto in un itenerabile
x = max(5, 20)
print(x) # <20>

# min() / restituisce il numero più piccole, o il valore più basso, o l'elemento con il valore più basso in un itenerabile
x = max(5, 20)
print(x) # <5>

# next() restiuisce l'elemento successivo in un iteratore 
mylist = iter(["apple", "banana", "cherry"])
x = next(mylist) #Apple
print(x)
x = next(mylist) #Banana
print(x)
x = next(mylist) #Cherry
print(x)

# oct() / converte un numero intero in una stringa ottale, le stringhe ottali in python hanno pefissio 0o
x = oct(12)
print(x) #<0o14>

# open() / apre un file e lo restiuisce come oggetto file.
f = open("demofile.txt", "r")
print(f.read()) #Apri un file e stampe il contenuto

# ord() / restiuisce l'intero che rappresenta il carattere h
x = ord("h")
print(x) #<104>

# pow() / restituisce il valore di x alla potenza di y (x, y)
x = pow(4, 3)
print(x) #<64> # 4 * 4 * 4 = 64

# print() / stampa il messaagio specificato sullo schermo, o su un altro dispositivo, di output standard. 
print("Ciao") #<Ciao>

# range() / restiutisce una sequenza di numeri a partire da 0 per impostare predefinit, e incrementa di 1 (per impostazione predefinita) e si ferma prima di un numero specificato

x = range(3, 6) #range di numeri tra 3 e 5
for n in x : #esegui l'elemento n in ciclo a l'elemento x, quindi passa su tutti i suoi valori
    print(n) #stampa ai valori del ciclo

# reverse() / inverte l'ordinamento degli elementi
lsita = ["Pera", "Mela", "Banana"]
lista.reverse()
print(lista) # <['Banana', 'Mela', 'Pera']>

# round() / arrotonda un numero in virgola mobile che è una versione arrotondata del numero specificato, con il numero specificato di decimali
x = round(5.756398, 2) #arrotonda il numero alla seconda cifra decimale.  
print(x) # <5.75> 

# set() / csotruttore per creare un set 
IlMioSet = set(("Audi", "Supra", "Porsche"))
print(IlMioSet) # <{'Porsche', 'Supra', 'Audi'}>

# seatttr() / imposta il valore dell'attributo specificato dall'oggetto specificato
class Persona: 
    nome = "Matteo"
    eta = 19
    
setattr(Persona, "eta", 20) #modifica il valore eta

x = getattr(Persona, "eta") #restituisce il valore del''attributo specificato
    
print(x) #<20>

# slice(2) / restituisce un oggetto slice 
''' 
Un oggetto slice viene utilizzato per specificare come suddividere una sequenza. 
È possibile specificare dove iniziare l'affettatura e dove terminare. 
Puoi anche specificare il passaggio, che ti consente, ad esempio, di affettare solo ogni altro elemento.
'''
a = ("a", "b", "c", "d", "e", "f")
x = slice(3) #prende solo i primi 3 valori
print(a[x]) # <['a', 'b', 'c']>

# sorted() / restiuisce un elenco ordinato dell'oggetto iterabile specificato 
a = ("b", "g", "a", "d", "f", "c", "h", "e") #non ordinato
x = sorted(a) 
print(x) # <['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']> IN ORDINE

# str() / converte il valore specificato in una stringa
x = str(3.5)
print(x) # <"3.5">

# sum() / reestituisce un numero, la somma di tutti i numeri gli elementi in un iterabile
a = (1, 1, 1)
x = sum(a)
print(x) # <3>

# tuple() / costruttore di tuple 
MiaTupla = tuple(("Bmw", "Audi", "Supra"))
print(MiaTupla) # <["Bmw", "Audi", "Supra"]>

# type() / restituisce il tipo dell'oggeeto specificato
x = 34
z = type(x)
print(z) # <class 'int'>

# zip() 
''' 
La zip()funzione restituisce un oggetto zip, che è un iteratore di tuple in cui il primo elemento
in ogni iteratore passato è accoppiato insieme, quindi il secondo elemento in ogni iteratore passato è accoppiato insieme ecc.

Se gli iteratori passati hanno lunghezze diverse, l'iteratore con il minor numero di elementi decide la lunghezza del nuovo iteratore.
'''
lista1 = ("Matteo", "Davide", "Sara")
lista2 = ("Renzi", "Rossi", "Toia")
x = zip(lista1, lista2) # unisce il primo elemento della lista1 con il primo della lista2
print(tuple(x))

# import / parola chiave viene utilizzata per importare i moduli

import datetime
x = datetime.datetime.now()
print(x) # <Ora attuale>



