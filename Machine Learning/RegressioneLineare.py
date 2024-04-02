import numpy
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from scipy import stats

# REGRESSIONE LINEARE & COEFFICENTE DI RELAZIONE (R)

""" 
La regressione lineare utilizza la relazione che c'è tra i punti dati (presenti nel grafico) per tracciare una linea retta
attraverso tutti loro

la regressione infatti è proprio quando si tenta di trovare una RELAZIONE tra le variabili 

Nel machine lerning questa relazione viene usata per prevenire l'avvenimento di eventi futuri


esempio: 

ho due liste una contenente l'eta di un auto e una contenente la velocità

x = [10, 13, 5, 2]

y = [85, 82, 100, 150]


Notiamo che le auto più grandi vanno più lente, le auto più giovani vanno meno lente. 

Qui possiamo trovare una relazione e "predirre" che la prossima auto che passerà se avvrà sopra una determinata età avrà anche una certa velocità

Questo perché c'è una relazione, in caso questa relazione non ci fosse non era presente nemmeno la regressione lineare (come vedremo dopo con l'elemento r)

"""

from scipy import stats

x = [5,7,8,7,2,17,2,9,4,11,12,9,6] # età auto 
y = [99,86,87,88,111,86,103,87,94,78,77,85,86] # veloctià auto


slope, intercept, r, p, std_err = stats.linregress(x, y)

# Metodo che resituisce alcuni importanti valori chiave della regressione lineare 


# _______________________

# Ora creiamo una funzione che tuilizzi i valori SLOPE e INTERCEPT per resituire un nuovo valore, 
# questo nuovo valore rapresenta dove l'asse Y verrà posizionata al valore X corrispondente

def myFunc(x):
    
    return slope * x + intercept
# eseguiamo questa funzione per ogni elemento dell'asse X tramite la funzione map() funzione che si comporta come un iterabile, passandoli una funzionee un valore eseguira quel valore (se è una lista per tutti i valori della lista) con la funzione. 


# __________________________

myModel = list(map(myFunc, x)) # (X è la lsita contenente l'età delle auto) 

# quindi ora avremmo una nuova lista contenente nuovi valori per l'asse Y

plt.scatter(x,y) # grafico a disperiosne originale 

plt.plot(x, myModel) # grafico a regressione lineare

plt.show()

     
    #COEFFICENTE DI RELAZIONE (R)
    
""" 
Come abbiamo detto prima la regressione lineare avvine se c'è una relazione tra le variabili. Se non ci sono relazione tra le variabili la regressione lineare non può prevedere nulla

Il coefficente di relazione è chiamato R, può assumere i seguenti valori: 

0 = nessuna relazione 

-1 a 1 = 100% correlato

più si avvicina a zero, più c'è una pessima relazione 
più si avvicina a -1 o a 1 più c'è una possibile relazione

"""

# usiamo il metodo dell'esempio precedente (dell'età e della velcoità delle auto)

slope, intercept, r, p, std_err = stats.linregress(x, y)

print(r) # <-0.758591524376155> / c'è relazione anche se non perfetta

    # CATTIVA RELAZIONE
    

""" 
sempre riferito all'esempio precedente, se passiamo due liste, dove non c'è relazione: 

x = [89,43,36,36,95,10,66,34,38,20,26,29,48,64,6,5,36,66,72,40]
y = [21,46,3,35,67,95,53,72,58,10,26,34,90,33,38,20,56,2,47,15]

il coefficente r sarà: 0,013 molto basso, proprio a significare che non c'è relazione tra loro

"""

# PREVEDERE I VALORI FUTURI 

# Riferito sempre all'esempio precedente dell'auto, proviamo a prevedere a che velocità andrà un auto che ha 10 anni


def myFunc(x):
    
    return slope * x + intercept


speed = myFunc(10) # non gli passiamo più la lista dell'età delle auto, ma un singolo valore 10 anni

print(speed) # <85.59308314937454>

""" 
La velocità è intorno a 85 perché abbiamo detto che più l'auto e "vecchia" più la velocità sarà bassa

Quindi ora lui sta predicendo che la velocità di un auto che ha 10 anni potrebbe essere intorno a 85
"""
