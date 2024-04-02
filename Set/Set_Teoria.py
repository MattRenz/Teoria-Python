#SET
set = a = {3, 4, 5, 7,} #è una raccolta non ordinata, immutabile, gli elementi non sono modificabili ma si possono rimuovere e aggiungere altri elementi
a = {"Ciao", "Prova", "Test"}
b = {3, 4, 5, 6}

frozenset('NomeLista') #restituisce un oggetto immutabile (è come un set solo che immutabile)


#METODI SET

# s1 | s2 = unione di due insiemi, se  un elemento è presente in tutti e due insiemi, non lo inserisce
# s1 & s2 = prende SOLO gli elementii in comune tra due insiemei 
# s1 - s2 = toglie dal primo insieme tutti gli elementi in comune al secondo
# s1 ^ s2 = unisce gli elementi del primo con il secondo, ma toglie quelli in comune 
 
# add() / Aggiunge un elemento all'insieme
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits) # <{'orange', 'apple', 'cherry', 'banana'}>

# clear() / Rimuove tutti gli elementiin un set

# copy() / Copia il set

# difference() / Resstituisce un set che contiene la differenza tra due set, molto simile al s1 - s2
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

# intersection() / Restituisce un insieme che contiene gli elementi uguali tra due insiemi, molto simile a s1 & s2
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
