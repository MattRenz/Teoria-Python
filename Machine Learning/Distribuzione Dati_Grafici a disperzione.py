import numpy
import matplotlib as plt

# DISTIBUZIONE DEI DATI CASUALE

"per creare una grande quantita di dati utilizziamo il modulo NumPy che può creare set di dati casuali di qualsiasi dmensione"

x = numpy.random.uniform(0.0, 5.0, 250)


# ISTOGRAMMA    
    
"""
Per visualizzare il seti di dati possiamo disegnare un istogramma con i dati raccolti
Useremo Matplotlib una libreria che permette la creazione di grafici. 
"""

import matplotlib.pyplot as plt 

x = numpy.random.uniform(0.0, 5.0, 250) 

# 0.0 - 5.0 sono il numero di colonne che creiamo

# 250 è il valore che verrà distribuito (in maniera) causale sulle colonne

plt.hist(x, 5) # 5 è la suddivisione del valore sulle colonne
plt.show()



# DISTRIBUZIONE NORMALE DEI DATI (INTORNO A UN VALORE SPECIFICO)

x = numpy.random.normal(5.0, 1.0, 100000) # 100000 valori

# 5.0 è il valore medio, ovvero dove i dati devono essere concentrati (inotrno al 5)

#  1.0 è dove i dati devono tenersi lontani

plt.hist(x, 100) # 100 righe 
plt.show()



# GRAFICI A DISEPRSIONE 

""" 
I grafici a dispersione sono grafici dove ongi punto corrisponde a un dato valore nel set

servono 2 set per i grafici a dispersione, 1 set per l'asse delle X e un set per l'asse delle Y
"""

x = [5,13,2] # età auto
y = [95,83,107] # velocità auto

plt.scatter(x,y)
plt.show()

""" 
Vedendo il grafico notiamo che l'auto che ha 5 anni avrà una velocità di 95, l'uato che ha 13 anni ha una  velocità di 83, ecc..
"""


# GRAFICI A DISPERSIONE CASUALE

"""
Per creare più dati su un algoritmo e testare un grafico a dispersione con valori casuali possiamo usare numpy come visto per la creazione di dati
""" 


x = numpy.random.normal(5.0, 1.0, 1000) # creiamo 1000 valori sull'asse X, saranno concentrati su 5 e "lontani" da 1.0 

y = numpy.random.normal(10.0, 2.0, 1000) # creiamo 1000 valori sull'asse Y, saranno concentrati su 10.00 e "lontani" da 2.0

plt.scatter(x, y)
plt.show() # avremo una cooncentrazione dei punti sull'asse X a 5, sull'asse Y a 10





