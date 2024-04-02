from cryptography.fernet import Fernet

""" 
cryptography fornisce funzionalità cittofrafiche, e altri strumenti come la firma digitale, autenticazione.
La libreria offere un API cryptography.fernet che offre un'implementazione del cifrario simmetrico di Fernet. 

Fernete è un algoritmo di cittografia simmetrico che consente di cittografare e decrittografare facilmente i dati  
utilizzando una chiave segreta (condivisa tra mittente e destinatario)
"""

Fernet.generate_key() #genera una chiave di cifratura casuale (restituisce una stringa di 44 caratteri che rappresentano la chiave casuale)

Fernet() # Crea un nuovo oggetto Fernet 

Fernet.encrypt() # Cifra la password (restituisce i dati come un oggetto bytes)

Fernet.decrypt() # Decifra la password 


# ESEMPIO DI CRYPT PASSWORD SENZA SALVARLO:

def CasualKey():
    
    key = Fernet.generate_key()
    
    return key

key = CasualKey()
fernet = Fernet(key)

def CryptPassword(password):
    
    encrypted_password = fernet.encrypt(password.encode()) # encode() da str() --> bytes
    
    return encrypted_password

def DecryptPassword():
    
    pswd_crypt = CryptPassword(pasword)
    
    decrypted_pswd = fernet.decrypt(bytes(pswd_crypt)).decode()
    
    return decrypted_pswd


# MAIN

pasword = input("Inserisci password: ")

crypt_pswd = CryptPassword(pasword)

print(f' La tua password cryptata è: {crypt_pswd}')

paswordControllo = input("Inserisci password: ")

if paswordControllo == DecryptPassword():
    print("Sei dentro")
else:
    print("Paassword sbagliata")
    



# ESEMPIO DI CRYP PASSWORD CON SALVATAGGIO FILE

import os

config_file_path = "/home/studente15/APP/MandaMail/key.data" # linux

def CasualKey(): # generazione e salvataggio chiave casuale
    
    key = Fernet.generate_key() # genera una chiave casuale
    
    with open(config_file_path, "wb") as file:
        file.write(key)

    return key # ritorna una chiave (in bytes)

def load_key(): # lettura chiave 
    
    if os.path.exists(config_file_path): # verifica se il file esiste 
    
        with open(config_file_path, "rb") as file: # se esiste legge la chiave dal file 
        
            key = file.read() # la chiave sarà quella che abbiamo salvato nel file 

    else: # se il file non essite ricrea la chiave

        key = CasualKey()

    return key # ritorna la chiave (a seconda se il file esiste o no)


def CryptPassword(password, filePath, key): # salvataggio password cryptata

    fernet = Fernet(key) # fernet = oggetto Fernet
    
    encrypted_password = fernet.encrypt(password.encode()) # encode() da str() --> bytes
    
    file = open(filePath, "wb") # wb = write bytes

    file.write(encrypted_password + b'\n') # scrive qui dentro la password cryptata e la salva in bytes
    file.close()
    
    return encrypted_password


def DecryptPassword(filePath, key): # decryptaggio password salvata
    
    fernet = Fernet(key)
    
    file = open(filePath, "rb") # rb = read byteas 
    
    pswd_crypt = file.read().rstrip(b'\r \n') # prende la password cryptata .rstrip() tolgie l'utlimo carattere di newline e di ritorno a capo per evitare errore iInvalidToken
    
    decrypted_pswd = fernet.decrypt(bytes(pswd_crypt)).decode()
    file.close()
    
    return decrypted_pswd


# MAIN

filePath = "/home/studente15/APP/MandaMail/pswd.data" 

key = load_key() # la chiave sarà quella che è salvata nel file


while(1):
    
    oper= input("1 Inserisci password, 2 Controllo password")
    
    if oper == "1":
        
        password = input("Inserisci la tua password: ")
        
        pswdCrypted = CryptPassword(password, filePath, key)
        print(f'\n La tua password Cryptata è: {pswdCrypted}')
        
    if oper == "2":
        
        while(1):
            
            print("\n Controlla la tua password")
            
            password = input("\n Inserisci la tua password: ")
            
            passwordDecryped = DecryptPassword(filePath, key)
            
            if password == passwordDecryped:
                
                print("\n Password Corretta")
                break
            else: 
                print("\n Password sbagliata riprova")
                

                
