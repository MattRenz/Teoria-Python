import numpy

"""  
Media: valore medio 

Mediana: valore del punto medio

Moda:  valore più comune

"""


# MEDIA 

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = numpy.mean(speed) # media di speed 89.77


# MEDIANA 
# il valore al centro dopo aver ordinato tutti i valori

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86] 

x = numpy.median(speed) # 86.5


# MODA 
# il valore più comune 
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86] 

x = stats.mode(speed)

print(x)


# DEVIZIONE STANDARD 

""" 
Deviazione standard numero che descrive quanto sono distribuiti i valori
Una deviazione bassa indica che la maggir parte deinumeri è vicina al valore medio (media)
Una deviazione alta indica che sono distibuiti su un intervallo più alto
"""

speed =  [86,87,88,86,87,85,86]

x = numpy.std(speed)

print(x)


# PERCENTILI 

""" 
Vengono utilizzati per fornire un numero che descrive il valore di cui una determinata percentuale è inferiore
"""

ages = [5,31,43,48,50,41,7,11,15,39,80,82,32,2,8,6,25,36,27,61,31]

"""
Qual è il 75° percentile ? Risposta: 43

Cioè il 75% delle persone ha 43 anni o meno. Per  fare ciò utilizziamo il modulo NumPy
"""

x = numpy.percentile(ages, 75)

    
    


