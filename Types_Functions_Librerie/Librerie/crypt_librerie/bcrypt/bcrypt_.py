import bcrypt

bcrypt.gensalt() # genera un salt casuale per aumentare la complessita dell'ashing

bcrypt.hashpw() # crea l'ashing della password

bcrypt.checkpw() # controlla se l'ashing della password (quello memorizzato) e l'input dell'utente coincidono. True se coincidono, False se non coincidono


# esempio e funzionamento bcrypt:

password = "matteorenzi123".encode() # La password deve essere convertita in formato bytes

salt = bcrypt.gensalt(rounds=12, prefix=b'2b') # Genera un salt casuale 

# il salt è una stringa causale utilizzata per aumentare la complessità dell'hashing della password. 

""" 
    rounds: 
specifica il costo del fattore di lavoro, ovvero il numero di iterazioni che l'algoritmo di hashing deve eseguire. 
Più alto è il valore di rounds, maggiore sarà il costo computazionale dell'hashing e maggiori saranno le difficoltà 
per un attaccante di indovinare la password originale. Tuttavia, un valore troppo alto può causare rallentamenti nelle operazioni di hashing.
rounds può accettare valori da 4 il più basso a 31 il più alto. 12 è il valore di defaul
    
    prefix: 
specifica il prefisso da utilizzare per il salt, che determina l'algoritmo di hashing utilizzato. Il prefisso predefinito è b'2b', 
che indica l'utilizzo dell'algoritmo di hashing bcrypt.

"""

hashed_password = bcrypt.hashpw(password, salt) # Crea l'hashing della password

"""
L'hashing di una password è utilizzato per proteggere la password in modo che non sia facilmente leggibile da terze parti in caso di acceesso non autorizzato ai dati.

bcrypt.hashpw() prende una password e un salt e restituisce l'hash della password, 
il salt è una stringa causale utilizzata per aumentare la complessità dell'hash della password.
"""

passwrod = print(f'Your password: {hashed_password}')

password_da_verificare = input("Password: ").encode() # La password da verificare deve essere convertita in formato bytes (UTF-8)

if bcrypt.checkpw(password_da_verificare, hashed_password): # prende la password in chiaro (input utente) e l'hash memorizzato. Restituisce True se coincidono, False se non concidono
    
    print("La password è corretta")
    
else:
    print("La password è sbagliata.")
    