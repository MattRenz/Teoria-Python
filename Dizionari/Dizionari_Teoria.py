#DIZIONARI

dizionario = {  #il diionario permette di memorizzare i valori dei dati in coppie chiave:valore, mappando degli oggetti con qualunque tipo di indice
    "Auto": "Supra",
    "Modello": "MK4",
    "Anno": "1998"
}

print(dizionario["Anno"])
#<1998>

dizionario["Modello"] = "MK5"   #cambia valore di un elemento in un dizionario

dizionario["Cavalli"] = 325     #aggiunta elemento al dizionario

dizionario = {
    "dizionario1" : {

    },                     #Un dizionario può contenere altri dizionari, si ciamano dizionari nidificati
    
    "dizionario2" : {
        
    }
    
}

#dict() è possibile usare questo costruttore per costruire un dizionario
dizionario = dict(name = "Matteo", eta = 20, Citta = "Pomezia")


#METODI DIZIONARI

x = dizionario.keys() #restituisce tutte le chiavi presenti nel dizionario
#print (x) <['Auto', 'Modello', 'Anno'] 

x = dizionario.values() #restituisce tutti i valori all'interno del dizionario
#print(x) <['Supra', 'MK4', 1998]>

dizionario.clear()              #svuota il dizionario

del dizionario                  #elimina il dizionario

dizionario.copy()               #Restiuisce una copia del dizionario

# fromkeys() / Restituisce un dizionario con le chiavi specificate e il valore specificato
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict) # <{'key1': 0, 'key2': 0, 'key3': 0}>

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