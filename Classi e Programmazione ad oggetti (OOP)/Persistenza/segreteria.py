import os
import docente as doc
import sys

lListaStudentiUniversita = []

pathWindowsDocentiUniversita = "C:\\Users\\Matteo\\OneDrive/Desktop\\Data Scientist\\Python\\Teoria e appunti\\Classi e Programmazione ad oggetti (OOP)\\Persistenza\\DB_Segreteria"
 
def SalvaDocenti(csDocente):

    sNomeFile = pathWindowsDocentiUniversita + "/" + csDocente.GetIdentificativo() + ".csv" # GetIdentificativo = 38

   #sNomeFile = C:\\Users\\Matteo\\OneDrive/Desktop\\Data Scientist\\Python\\SD3_Python\\L1\\Persistenza\\segreteira_studente_versione2\\DB_Segreteria\38.csv" 

    StirngaDocente = doc.docente.CreaDatiDocente(csDocente) # 'Matteo;Renzi;38;mattrenz9@gmail.com'
    
    # Possiamo richiamarci il metodo CreaDatiDocente() (che è all'interno della classe docente) perchè nel parametro csDocente è presente l'istanza della classe docente, e quindi eredita tutti gli attributi e i suoi metodi
    
    file = open(sNomeFile, "w") # crea un file con nome 38.csv e scrivici dentro

    file.write(StirngaDocente) # scrivi 'Matteo;Renzi;38;mattrenz9@gmail.com'

    file.close() # chiudiamo il file 


def leggistudente(sFileDocenti):

    sNomeFile = pathWindowsDocentiUniversita + "/" + sFileDocenti # C:/Desktop/Python/DB_Segreteria/32.csv

    file = open(sNomeFile, "r") # apri il file

    SringaDocente_DalFile = file.readline() # ["Matteo;Renzi;32;mattrenz9@gmail.com;]

    file.close() 

    SringaDocente_DalFile_split = SringaDocente_DalFile.split(";") # ["Matteo" ,"Renzi", 32, "mattrenz9@gmail.com", ]

    if SringaDocente_DalFile_split[len(SringaDocente_DalFile_split) -1] == '': # ["Matteo" ,"Renzi", 32, "mattrenz9@gmail.com", ]

        SringaDocente_DalFile_split = SringaDocente_DalFile_split[0:len(SringaDocente_DalFile_split)-1] # ["Matteo" ,"Renzi", 32, "mattrenz9@gmail.com",]

    nome = SringaDocente_DalFile_split[0] # Matteo
    cognome = SringaDocente_DalFile_split[1] # Renzi
    Idetnificativo = int(SringaDocente_DalFile_split[2]) # 38
    mail = SringaDocente_DalFile_split[3] # mattrenz9@gmail.com

    listaVotiVuota = []
    
    if len(SringaDocente_DalFile_split) > 4: # ["Matteo" ,"Renzi", 32, "mattrenz9@gmail.com",]


        for corso in SringaDocente_DalFile_split[4:]: # ["Matteo" ,"Renzi", 32, "mattrenz9@gmail.com", "corso"]
            
            listaVotiVuota.append(corso)

            csDocente = doc.docente(nome,cognome,Idetnificativo,mail,listaVotiVuota)  # # ["Matteo" ,"Renzi", 32, "mattrenz9@gmail.com", "corso"]
    
    else:
        csDocente = doc.docente(nome, cognome, Idetnificativo, mail) # # ["Matteo" ,"Renzi", 32, "mattrenz9@gmail.com", "corso"]

    return csDocente


# SEGRETERIA

print("Segreteria studenti".center(80, "_"))

while(1): 
    Oper = input("\n 1 Sezione Docente, 2 Sezione Studente, 3 Uscita: ")
    
    if Oper == "3":
        sys.exit()   

    
# DOCENTI
    lNuovoDocente = [] # lista di OGGETTI
    
    if Oper == "1":
        
        while(1):        
            sOperDoce = input("\n Operazione (1 Aggiungi Docente, 2 inserisci corso)")
    
    
# (1) STAMPA DOCENTE

            if sOperDoce == "1":
                
                sNome = input("\n Inserisci nome docente: ")
                sCognome = input("\n Inserisci cognome docente: ")
                sIdetnificativo = input("\n Inserisci Identificativo docente: ")
                mail = input(f'\n Mail: ')

                sNuovoDocente = doc.docente(sNome, sCognome, sIdetnificativo, mail) # qui richiamo la classe studente e gli assegno gli input dell'utente che per lui corrispondono a gli attibuti della classe 
    
                lNuovoDocente.append(sNuovoDocente)

                SalvaDocenti(sNuovoDocente) # Come parametro della funzione gli passo "sNuovoDocente" dove all'interno è preente l'istanza della classe docente
                
# (2) AGGIUNGI CORSO
    
            if sOperDoce == "2": 
                
                sIdetnificativo = input(f'\n Inserisci identificativo: ') # 32 
                corso = input(f'\n Aggiungi corso: ') # "corso"

                listaDocentiUniversita = os.listdir(pathWindowsDocentiUniversita) # = ["380.csv", "456.csv", "634.csv"]
                # lista di nomi di file presenti dentro il path 
                
                trovaDocente = 0
                for curfile in listaDocentiUniversita: 
                    
                    # curfile nome del singolo file dnetro al path ["380.csv"] poi [456.csv]
                    
                    if curfile == sIdetnificativo + ".csv": # 32.csv
                      
                        Nuovo_Docente = leggistudente(curfile) # passo come parametro della funzione leggistudente() currfile, che non è altro il nome del file (quindi l'identificativo) al quale l'utente vuole aggiunge un corso
                        
                        Nuovo_Docente.AggiungiCorso(corso) # questo metodo è presente dentro la classe docente, ora noi possiamo usarlo perché nella variabile docente è presente la funzione leggistudente dove all'interno è istanziata la classe docente, e quindi eredità tutti i suoi metodi

                        SalvaDocenti(Nuovo_Docente) # salviamo il docente dopo aver aggiunto il corso
                        
                        trovaDocente = 1
                        
                if trovaDocente == 0:
                    print(f'\n Docente non trovato. \n identificativo: {sIdetnificativo} non riconosciuto')
    
                else:
                    print("\n Corso aggiunto correttamente")
