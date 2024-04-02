import json 

"""
Fornisce funzioni per codificare e decodificare i dati in formato JSON 

Es: 

Questo è un dato in formato JSON

data = {
    "nome": "Mario",
    "cognome": "Rossi",
    "eta": 30,
    "residenza": {
        "citta": "Roma",
        "via": "Via del Corso"
    }
      
"""

json.dumps()  # codificare un oggetto PYTHON in formato JSON

json.loads() # decodificare una stringa JSON in un oggetto PYTHON


# FILE

json.dump() #scrivere i dati JSON su un file 

json.load() # per leggere i dati JSON da un file


""" 

Possiamo anche leggere un singolo elemento di un file JSON es:

Pathfile: [{"nome": "Marco", "cognome": "Rossi", "facolta": "Economia"}]

with open(Pathfile, "r") as file:
    
    file_studente = json.load(file)
    
    print(file_studente["cognome"]) <Rossi>
    
"""
