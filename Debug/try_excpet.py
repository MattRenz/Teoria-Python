try: # consente di verificare la presenza di errori SE CONOSCI L'ERRORE CHE SI VERIFICHERA'
    pass
except: # consente di gestire l'errore
    pass
else: # esegue il codice indipendentemente dal risultato dei blocchi try
    pass
finally: # eseguirà il processo indipendetemente dal fatto che sia stata sollevata un'eccezione o no 
    pass

# ES
x = input("Inserisci numero: ")

try: 
    x = int(x)
    if x > 10:
        print("Il tuo numero è maggiore di 10")
        
except:
    print("Attenzione inserire un numero valido")
    print("")
    print(f'{x} non valido')

