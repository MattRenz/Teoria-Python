import numpy
import matplotlib.pyplot as plt


# PREGRESSIONE POLIMIALE & R-QUADRATO

"""  
Se i punti del nostro grafico non si adattano a una progressione lineare possimao usare una progressione polimiale
"""

x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22] # ora di passaggio al casello

y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100] #velocità registrata 


# Creiamo un modello polimoniale tramite numPy
mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

# Specifichiamo come verrà viuslizzata la linea, in questo caso dal 1 (primo elemento della lista X) a 22 (ulitmo elemenot della lista X)
myline = numpy.linspace(1, 22, 100)

plt.scatter(x, y)
plt.plot(myline, mymodel(myline)) # per visualizzare grafico polinomiale
plt.show()

    # R-QUADRATO
    
""" 
Come visto nella regressione lineare se non c'è relazione tra le variabili non si può prevedere nulla
Nella regressione polimoniale per vedere quanta relazione c'è tra i valori dell'asse X e Y misuriamo la r-quadrato

r-quadrato può assumere valore 0 = nesssuna relazione / 1 = relazione 100% 
"""

from sklearn.metrics import r2_score

mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

print(r2_score(y, mymodel(x))) # <0.96> in questo caso molto vicino a 1


# PREVISIONE VALORI FUTURI 

# ora possiamo prederre la velocità di un'auto che passa al casello intorno alle 17:00

speed = mymodel(17)

print(speed)








