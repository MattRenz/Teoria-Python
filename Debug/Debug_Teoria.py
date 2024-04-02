
# 5 METODI DEBUG


# 1 Le print


# 2 il Debuger
""" 
COMANI DEBUG 

Debugger start = F5 

Pausa = F6

Step Over (Scavalcare) F10

Step Into (Entrare) F11

Step Out (Uscire) SHIFT + F11

Restart CTRL + SHIFT + F5

Stop SHIFT + F5
"""


# 3 Il File di LOG
"""
FILE DI LOG 
 
è un file prodotto dal programma che scrive tutte le opezaione che il programma fa.
Questo puo avvenire in modo piu o meno dettalgiato 

Un file di log dettagliato ci da informazione dettagliate su cio che il nosre pogramma 
fa ma di contro consuma tempo e risorse se hai più utenti che lavorano in contemporanea rischi di mandare in tilt il sistema

i file log sono circolari e an certo punto sovrascrive, e dovrebbero essere il più dettagliati possibille

crare un ambiente di test (mirror) dove si possono effetuare test, e porvare la macchina. 
"""


# 4 unttest
""" 
Per eseguire una serie di test preliminari, dei test/controlli prima dell'avvio del programma
usiamo la libreria unittest. 

il piano di test deve avere una sturttura: un outuput binario
Il programma permettere di riflettere sul ciclo di vita di un programma: 
Proettazione / Preparazione(scrittura) / Test / Verifica periodica o per eventi
"""

# unittest.TestCase() = E' una classe che definisce metodi per confrontare tra di loro gli argomenti, come assertEqual()

# es assertEqual(): 
import unittest

class test_unittest(unittest.TestCase):
    def test_unittest(self):
        self.assertEqual(sum([5,5,5]), 15, "ERRORE: Dovrebbe essere 15")
    
if __name__ == "__name__":
    unittest.main()  #per eseguirlo 



# 5 try e except  

""" 
try e except vengono utilizzate per gestire le eccezzioni, errori che si verificano durante l'esecuzione di un programma
Il blocco try contiene il codice che PUO' sollevare un'eccezione
Il blocco except contiene il codice che VERRA' eseguito se viene sollevata un'eccezione
"""


try: # consente di verificare la presenza di errori 
    pass
except: # consente di gestire l'errore
    pass
else: # esegue il codice indipendentemente dal risultato dei blocchi try
    pass
finally: # eseguirà il processo indipendetemente dal fatto che sia stata sollevata un'eccezione o no 
    pass