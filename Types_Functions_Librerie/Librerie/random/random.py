import random 

print(random.random()) # restituisce un numero casuale tra 0 e 0.1

print(random.randrange(1, 50)) # restituisce un range casuale tra 1 e 59

random.shuffle() # rioridina in modo causale gli argomenti di una lista

random.choice() # restiuisce in modo casuale un elemento da una sequenza (tupla.lista.stringa ecc)

myList = ["Bmw", "Audi", "Toyota", "Porsche"]
print(random.sample(myList, 4)) # restituisce un elenco con una selezione casuale degli elementi specifiati, e restituisce gli elementi casuali per un numero di volte specificato
