#METODI STRINGHE 
# .find() = Trova la posizione di un carattere dentro una stringa, se non è presente ristituisce -1
a = "Ciao"
print(a.find("i")) #<1>

# index() = restituisce la prima posizione del valore specificato
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x) # <2>

# .count() = conta QUANTI caratteri sono presenti in una stringa
a = "Ciao"
print(a.count("a")) #<1>

# .center(width[, fillchar] = crea uno spazio della grandezza che abbiamo dato
a = "Ciao"
print(a.center(80, "_")) # <___________Ciao__________>

# .strip([Chars]) = toglie gli spazi ai lati 
a = "          Ciao"
print(a.strip()) #<Ciao>

# .replace(old, new[count]) = cambio di caratteri 
a = "ciao"
print(a.replace("c", "C")) # <Ciao>

# .endswith(stringa) restituisce Ture se la stringa finisce con il valore specificato
a = "Ciao"
print(a.endswith("o")) # <True>

# .format()
# a = 3
b = 5
print("Il numero a vale {0} e il numero b vale {1}".format(a,b))



a.lower() #Restituisce una stringa in minuscolo

a.upper() #Restituisce una stringa in maiuscolo

a.capitalize() #Restituisce la prima lettera maiuscola in tutte le parole

a.title() #Restituisce la prima lettera maiuscola alla prima parola

a.swapcase() #inverte maiuscole con minuscole

x = chr(97)  #Ottieni il carattere che rappresenta l'unicode 97:
print(x)

x = ord("a")
print(x)   #Restituisce l'intero che rappresenta il carattere "a": 
