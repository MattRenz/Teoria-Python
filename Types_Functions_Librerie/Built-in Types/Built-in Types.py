#STRING METHODS

#a.lower() /Restituisce una stringa in minuscolo
testo = "Testo PROVA"
x = testo.lower()
print(x) #<testo prova>

#a.upper() / Restituisce una stringa in maiuscolo
testo = "Testo PROVA"
x = testo.upper()
print(x) #  <TESTO PROVA>

#a.capitalize() / Restituisce la prima lettera maiuscola in tutte le parole
testo = "Testo PROVA"
x = testo.capitalize()
print(x) #<Testo prova>

#a.title() / Restituisce la prima lettera maiuscola alla prima parola
testo = "Testo PROVA"
x = testo.title()
print(x) #<Testo Prova>

#a.swapcase() / inverte maiuscole con minuscoletesto = "Testo PROVA"
testo = "Testo PROVA"
x = testo.swapcase()
print(x) #<tESTO prova>

# center() / centra una stringa , e li si può passare un parametro
testo = "Testo PROVA"
x = testo.center(20, "_")
print(x) # <_______Testo PROVA_____>

# count() / ritorna il numero di volte di un carattere specificato 
testo = "TestO PROVA"
x = testo.count("O")
print(x) # <2>

# encode() / codifica la stringa, utilizzando la codifica specificata, se non viene specificata alcuna codifica, verrà utilzzato UTF-8

# encode() converte da str() a bytes
txt = "My name is Ståle"
x = txt.encode()
print(x) # <b'My name is St\xc3\xe5le'>

# decode() / converte da bytes a str()
txt = "My name is Ståle"
x = txt.decode()

# txt.endswith() / Restituisce True se la stringa termina con il valore specificato, altrimenti False
txt = "Hello, welcome to my world."
x = txt.endswith(".")
print(x) # <True>

# expandtabs() / imposta la dimensione della scheda sul numero speificato di spazi binachi
txt = "H\te\tl\tl\to"
x =  txt.expandtabs(2)
print(x) # <H e l l o>

# find() / trova la prima occorrenza del valore specificato. Restituisce -1 se il valore non viene trovato.
txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x) # <7>

# format() / formatta i valori specificati e li inserisce all'interno del segnaposto della stringa.
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49)) #  <For only 49.00 dollars!>

# index() / Metodo trova la prima occorrenza del valore specificato.
txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x) # <7> settimo carattere

# isalnum() / restituisce se tutti icaratteri sono alfanumerici, ovvero lettere dall'alfabeto (az) e numeri (0-9)
txt = "Company12"
x = txt.isalnum()
print(x) # <True>

# isalpha() / restituisce True se tutti i caratteri sono lettere dell'alfabeto (az)
txt = "Company12$"
x = txt.isalpha()
print(x) # <False>

# isaascii() / restiuisce True se  tutti icaratteri sono caratteri ascii (az)
txt = "Company123"
x = txt.isascii()
print(x) # <True>

# isdecimal() / restituisce True se tutti i caratteri sono decimali (0-9)
txt = "\u0033" #unicode for 3
x = txt.isdecimal()
print(x) # <True>

# isdigit() / Restituisce True se tutti i caratteri sono cifre altrimenti False
txt = "5809A"
x = txt.isdigit()
print(x) # <False>

# isidentifier() / Restituisce True se la stringa è un identificatore valido, altrimenti False.
''' 
Una stringa è considerata un identificatore valido se contiene solo lettere alfanumeriche (az) e (0-9) 
o caratteri di sottolineatura (_). Un identificatore valido non può iniziare con un numero o contenere spazi.
'''
txt = "Demo"
x = txt.isidentifier()
print(x) # <True>

# islower() / Restituisce True se tutti i caratteri sono in minuscolo, altrimenti False.
txt = "hello world!"
x = txt.islower()
print(x) # <True>

# isnumeric() / Restituisce True se tutti i caratteri sono numerici (0-9), altrimenti False.
txt = "565543"
x = txt.isnumeric()
print(x) # <True>

# isprintable() / Restituisce True se tutti i caratteri sono stampabili, altrimenti False.
txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x) # <True>

# isspace() / Restituisce True se tutti i caratteri in una stringa sono spazi bianchi, altrimenti False.
txt = "   "
x = txt.isspace()
print(x) # <True>

# istitle() / restituisce True se tutte le parole in un testo iniziano con una lettera maiuscola E il resto della parola è costituito da lettere minuscole, altrimenti False.
txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x) # <True>

# isupper() / Restituisce True se tutti i caratteri sono maiuscoli, altrimenti False.
txt = "THIS IS NOW!"
x = txt.isupper()
print(x) # <True>

# join() / Prende tutti gli elementi in un iterabile e li unisce in una stringa, è necessario specificare una stringa come separatore
a =("Matteo", "Mario", "Luca")
x = "_".join(a)
print(x) # <Matteo_Mario_Luca>

# ljust() / allinierà a sinistra la stringa, utilizzando un carattere specificato
txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.") # <banana              is my favorite fruit.>

# lower() / Restituisce una stringa in cui tutti i caratteri sono minuscoli.
txt = "Hello my FRIENDS"
x = txt.lower()
print(x) # <hello my friends>

# lstrip() / Rimuove tutti i caratteri iniziali 
txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite") # <of all fruits banana     is my favorite>

# maketrans() / Restiuisce una tabella di mapping che può essere utilizzata con il metodo per sostiuire i caratteri specificati. translate()
a = "Ciao Sam"
x = a.maketrans("S", "P") # sostiuisci "S" con "P"
print(a.translate(x)) # <Ciao Pam>

# partition() / cerca una stringa specificata e divide la stringa in una tupla contenente tre elementi, 1) la parte prima della stringa, 2) la stringa specificata, 3) la parte dopo della stringa
testo = "Mi chiamo Matteo e  ho 20 anni"
x = testo.partition("Matteo")
print(x) # <('Mi chiamo ', 'Matteo', ' e  ho 20 anni')>

# replace() / Sostituisce una frase specificata con un'altra frase specificata.
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x) # <I like apples>

# rfind() / Trova l'ultima occorrenza del valore specificato.
txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x) # <12>

# rjust() / Allinea a destra la stringa, utilizzando un carattere specificato
txt = "banana"
x = txt.rjust(20)
print(x, "is my favorite fruit.") # <              banana is my favorite fruit.>

# rstrip() / Rimuove tutti i caratteri finali
txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite") # <of all fruits     banana is my favorite>

# split() / suddicide una stringa in un elenco
txt = "welcome to the jungle"
x = txt.split()
print(x) # <['welcome', 'to', 'the', 'jungle']>

# splitlines() / Suddivide un stringa in un elenco. La divisione viene eseguita in corrispondenza delle istruzione di riga
txt = "Ciao mi chiamo matteo\nHo 20 anni "
x = txt.splitlines()
print(x) # <['Ciao mi chiamo matteo', 'Ho 20 anni ']>

# startswith() / Restituisce True se la stringa inizia con il valore specificato, altrimenti False.
txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x) # <True>

# strip()metodo rimuove tutti i caratteri iniziali (spazi all'inizio) e finali (spazi alla fine) 
txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite") # <of all fruits banana is my favorite>

# translate() / Reestituisce una strnga in cui alcuni caratteri specificati venogno sotituiti con il carattere descritto in un dizionario o in unaa tabella di mapping
dizionario = {83:  80}
testo = "Hello Sam!"
print(testo.translate(dizionario))  # <Hello Pam!>

# zfill()/ Aggiunge zeri (0) all'inizio della stringa, finché non raggiunge la lunghezza specificata.
txt = "50"
x = txt.zfill(10)
print(x) # <0000000050>


# LIST/ARRAY METHODS

# append() / Aggiunge un elemento alla lista a fine elenco
lista = ["Mela", "Pera", "Banana"]
lista.append("Fragola")
print(lista) # <['Mela', 'Pera', 'Banan', 'Fragola']>

# clear() / Rimuovi gli elementi all'interno di una lista
lista = ["Mela", "Pera", "Banana"]
lista.clear()
print(lista) # <[]>

# copy() / Restituisce una copia dell'elenco specificato
lista = ["Mela", "Pera", "Banana"]
x = lista.copy
print(x) # <["Mela", "Pera", "Banana"]>

# count() / Restituisce il numero di elementi con il valore specificato
lista = ["Mela", "Pera", "Banana", "Mela"]
x = lista.count("Mela")
print(x) # <2>

# extend() / Aggiungee gli elementi dell'elenco specificati alla fine dell'elenco corrente
lista = ["Banana", "Mela", "Pera"]
lista2 = ["Fragola, Arancia", "Mango"]
lista.extend(lista2)
print(lista) # <['Banana', 'Mela', 'Pera', 'Fragola, Arancia', 'Mango']>

# index() / Restituisce la posizione alal prima occorenza del valore specificato
lista = ["Mela", "Pera", "Banana"]
x = lista.index("Banana")
print(x) # <2>

# insert () / Inserisce il valore specificato nella posizione specificata
lista = ["Mela", "Banana"]
lista.insert(1, "Pera")
print(lista) # <["Mela", "Pera", "Banana"]>

# pop() / Restituisce e rimuove l'elemento nella posizione specificata
lista = ["Mela", "Pera", "Banana"]
lista.pop(1)
print(lista) # <["Mela", "Banana"]>

# remove() / Rimuove l'elemento del valore specificato
lista = ["Mela", "Pera", "Banana"]
lista.remove(1)
print(lista) # <["Mela", "Banana"]>

# reverse() / Inverte l'ordinamento degli elementi
lista = ["Mela", "Pera", "Banana"]
lista.reverse
print(lista) # >["Banana", "Pera", "Mela"]>

# sort() / Ordina l'elenco in ordine crescente (per impostazione predefinita)
lista = [5, 7, 9, 3, 1]
lista.sort()
print(lista) # <[1, 3, 5, 7, 9]>

enumerate(x)  # Prende una collezione per (es. tupla) e la restiuisce come in un esemio numerato

# DIZIONARI METHODS

# clear() / Rimuove tutti gli elementi da un dizionario
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()
print(car) # <{}>

# copy() / Restiuisce una copia del dizionario

# fromkeys() / Restituisce un dizionario con le chiavi specificate e il valore specificato
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict) # <{'key1': 0, 'key2': 0, 'key3': 0}>

# ordina un elenco dizionario in base al valore "anno"
def funzione(e):
    return e["Anno"]

cars = [
    {"car": "Ford", "Anno": 2005},
    {"car": "BMW", "Anno": 2019},
    {"car": "Mitsubishi", "Anno": 2000}
]
cars.sort(key=funzione)
print(cars) # <[{'car': 'Mitsubishi', 'Anno': 2000}, {'car': 'Ford', 'Anno': 2005}, {'car': 'BMW', 'Anno': 2019}]>

# get() / Restituisce il valore dell'elemento con la chiava specificata
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.get("model")
print(x) # <"Mustang">

# items() / Restiuisce un oggetto vista. L'oggetto di visualizzazione contiente le copie chiave-valore del dizionario, come tuple in un elenco
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.items()
print(x) # <dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])>

# keys() / Restiuisce le chiavi di un dizionario sotto forma di elenco
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.keys()
print(x) # <dict_keys(['brand', 'model', 'year'])>

# pop() / Restituisce e rimuove l'elemento specificato dal dizionario
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
print(car) # <{'brand': 'Ford', 'year': 1964}>

# popitem() / Rimuove l'elemento che è stato inserito per ultimo nel dizionario 

# setdefault() / Restituisce il valore dell'elemento con la chiave specificata, se la chiave non esiste, inserire la chiave, con il valore specificato.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("color", "white")
print(x) # <White>

# update() / Inserisce gli elementi specificati nel dizionario
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.update({"color": "White"})
print(car) # <{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'White'}>

# values() / Restiuisce un oggetto vista. L'oggeto continene i valori, chiave elemento del dizionario come un elenco


#TUPLE METHODS

#count() / Restituisce il numero di volte in cui un valore specificato appare nella tupla
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x) # <2>

# index() / Restituisce la prima occorenza del valre specificato
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x) #<3> 

#SET METHODS 

# s1 | s2 = unione di due insiemi

# s1 & s2 = prende gli elementii in comune tra due insiemei 

# si - s2 = toglie dal primo insieme tutti gli elementi in comune al secondo

# s1 ^ s2 = restituisce tutti gli elementi dell'altro ma non comuni
 
# add() / Aggiunge un elemento all'insieme
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits) # <{'orange', 'apple', 'cherry', 'banana'}>

# update () / Aggiunge gli elementi di s2 ad d s1 
si.update(s2)

# clear() / Rimuove tutti gli elementiin un set

# copy() / Copia il set

# difference() / Resstituisce un set che contiene la differenza tra due set
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y) 
print(z) #  <{'banana', 'cherry'}>

# dfference_update() / Rimuove gli elementi originali che esistono in entrambi i set
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y) # rimuove "apple" perché è presente in entrambi i set
print(x) # <{'cherry', 'banana'}> 

# discard() / Rimuove l'elemento specificato dal set
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits) # {"Apple", "Cherry"}

# intersection() / Restituisce un insieme che contiene gli elementi uguali tra due insiemi
x = {"Mela", "Pera", "Banana"}
y = {"Fragola", "Mango", "Banana", "Pera"}
z = x.intersection(y)
print(z) # <{'Pera', 'Banana'}>

# intersection_update() / Rimuove gli elementi che non sono presenti in entrambi gli insiemi
x = {"Mela", "Pera", "Banana"}
y = {"Fragola", "Mango", "Banana", "Pera"}
x.intersection_update(y)
print(x) #<{'Pera', 'Banana'}> è diverso da intersecton() perchè qui lui rimuove completamente gli elementi

# isdisjoint() / Restituisce True se nessuno degli elementi è presente in entrambi gli insiemi, altrimenti restiuisce False
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z) # <True> tutti elementi diversi

# issubset() / Resstituisce True se tutti gli elementi del set esistono nel set specificato, altrimenti restituisce False
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y) 
print(z) # <True> perché tutti gli elementi di x sono presenti in y

# pop() / Restiuisce e rimuove un elemento casuale dall'insieme
fruits.pop()

# remove() / Rimuove l'elemento specificato dal set
fruits.remove("banana")

# symmetric_difference() / Restiuisce un set che contiene tutti gli elementi di entrambi i ser, tranne gli elementi presenti in entrambi i set, i copioni.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z) # {'google', 'banana', 'microsoft', 'cherry'}> "apple" non presente perché è in entrambe i set

# union() / Restituisce un set che contiene tutti gli elementi del set originale. Se un oggetto è presente in più di un set, il risultato conterrà solo un aspetto di questo oggetto.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y)
print(z) # <{'microsoft', 'cherry', 'google', 'apple', 'banana'}>


# shuffle() / Prende una sequenza, come un elenco, e riorganizza l'ordine degli elementi.
import random

mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)

print(mylist) # <['banana', 'apple', 'cherry'] >

