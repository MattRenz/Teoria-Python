import msvcrt # disponibile solo su Windows permette di interagie con la console (finestra di linea di comando)


msvcrt.getch() #consente di leggere un singolo carattere della tastiera senza che l'utetna prema invio

msvcrt.kbhit() # verifica se un tasto della tasteira è stato premuto

msvcrt.putch() # scrvie un singolo carattere sulla console 


# "\r" = tasto di invio

# "\b" = tasto di "backspace" 

char = ""
char.isprintable() # controlla se tutti i caratteri all'interno di una stringa sono stampabili. 

# Esempio msvcrt CRYPT INPUT UTENTE (*)

def asterisk_input():
        
    password = ""
    
    while(1):
        
        char = msvcrt.getch().decode("utf-8") # legge il carattere inserito sulla tastiera (come una stringa di byte)

        # 1) L'utente preme invio
        if char == "\r": # se l'utente preme il tasto invio 
            
            print("")  # Stampa un newline alla fine dell'input
            return password
        
        # 2) L'utente preme il "backspace"
        elif char == "\b": # controlla se il carattere inserito è il "backspace"
            
            if password: # password (l'input dell'utente diventa)
                
                password = password[:-1] # Elimina l'ultimo carattere inserito
                
                print("\b \b", end="", flush=True)
                
        # 3) L'utente preme un carattere stampabile, 
        elif char.isprintable(): # controlla se il carattere inserito corrisponde a un carattere stampabile se si
            
            password += char # Aggiunge il carattere alla password e stampa un asterisco sul terimnale
            
            print("*", end="", flush=True)
            
            # end = viene utilizzato per controllare il modo in cui la funzione print() gestisce la fine della striga, se è vuoto significa che non verrrà inserito nessun carattere alla fine della stringa
            
            # flusch = chiede esplicitamente al sistema di svuotare il buffer di output, in modo da garantire che la stringa di output venga immediatamente visualizzata a schermo
    
    
        # alla fine del cilo avremo la password,e quando l'utente premerà invio gli ritornerà la password
              
pswd = asterisk_input()
print(pswd)