#LISTE - TUPLE
lista = []
lista2 = []
print(lista[2]) #richiama secondo elemento della lista

print([lista[2:]]) #esclude i primi 2

print(lista[:3]) #esclude gli ultimi 2

print(lista[2:4]) #richiamo intervallo preciso escluso ultimo

print(lista in lista2) #controllo liste elementi uguali 

print(lista not in lista2) #controllo liste differenti

print("Mela" in lista) #controllo singolo elemento nella lista

print(len(lista)) #lunnghezza della lista)

print(min(lista)) #il più piccolo elemento della lista

print(max(lista)) #il più gande elemento della lista

list(nomeVariabile) #inserisce i singoli caratteri di una frase all'interno di una lista      

print(a.split()) #restituisce una lista di stringhe

print(a.rsplit()) #stessa cosa dello split ma dalla parte destra

print("_".join(lista)) #restituisce una stringa sulla lista che dichiariamo, separato dall'elemento che abbiamo dichiarato


#METODI LISTA 
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

# Sostituire un elemento in una lista
lista = ["Test", "Prova", "Python"]
lista[1] = "CIAO"
print(lista) # <["Test", "CIAO", "Python"]>

# Sostituire un range di elmenti in una lista
lista = ["Test", "Prova", "Python", "Ciao"]
lista [1:3] = "PROVA", "ELEMENTO"   
print(lista) # <["Testo", "PROVA", "ELEMENTO", "Ciao"]>

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

# extend() / Aggiungee gli elementi dell'elenco specificati alla fine dell'elenco corrente
lista = ["Banana", "Mela", "Pera"]
lista2 = ["Fragola, Arancia", "Mango"]
lista.extend(lista2)
print(lista) # <['Banana', 'Mela', 'Pera', 'Fragola, Arancia', 'Mango']>

# sort() / Ordina l'elenco in ordine crescente (per impostazione predefinita)
lista = [5, 7, 9, 3, 1]
lista.sort()
print(lista) # <[1, 3, 5, 7, 9]>


#TUPLE
tuple = ("Ciao", True, 55) #tuple uguale alle liste ma non modificabili

del tuple #la parola del elimina complletamente la tupla

auto = ("MBW" "Porsche", "Supra")
(M5, TurboS, Mk5) = auto        #Possiamo assegnare i valori di una tupla a delle variabili
print(TurboS)                   #print <Porsche> 

tuple3 = tuple1 + tuple2 #si possono unire più tuple con l'operatore +

enumerate(x)  # Prende una collezione per (es. tupla) e la restiuisce come in un esemio numerato

#METODI TUPLE 

#count() / Restituisce il numero di volte in cui un valore specificato appare nella tupla
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x) # <2>

# index() / Restituisce la prima occorenza del valre specificato
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x) #<3> 

#enumerate() / prende una collezione per (es. tupla) e la restiuisce coeìme un esempio numerato
x = ("Porsche", "Supra", "BMW")
y = enumerate(x)
print(list(y))

# iter() e next() # itera un elenco per esmpio una tupla

tupla = ("BMW", "Porsche", "Audi")

MyIter = iter(tupla)

print(next(MyIter)) # <BMW>
print(next(MyIter)) # <Porsche>
print(next(MyIter)) # <Audi>