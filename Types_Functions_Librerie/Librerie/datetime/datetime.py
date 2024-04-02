
import datetime # per manipolare date e orari

todaynow = datetime.datetime.now() # giono mese anno ora secondo e millisecodno

giorno = todaynow.strftime("%A") # Mercoeldì

giornodelmese = todaynow.strftime("%d") # 31

mese = todaynow.strftime("%B") # Dicembre

anno = todaynow.strftime("%Y") # 2023

todaynow.strftime("%H") # 17 (ora)

todaynow.strftime("%M") # 41 (minuti)

todaynow.strftime("%S") # 3 (secondi)

today = datetime.date.today() # data odierna

anno = today.year() # anno 

mese = today.month() # mese

giorno = today.day() # giorno


from datetime import timedelta 
# timedelta è una libreria proveniente da datetime, può essere utilizzato per operazioni matematiche su date e orari

data1 = datetime.datetime.now()

data1 >= timedelta(days=5) # superiore di 5 giorni 

""" Valori accettati da timedelta()

days: specifica il numero di giorni nell'intervallo di tempo. Questo può essere un valore negativo o positivo. Il valore predefinito è 0.
        
seconds: specifica il numero di secondi nell'intervallo di tempo. Questo può essere un valore negativo o positivo. Il valore predefinito è 0.

microseconds: specifica il numero di microsecondi nell'intervallo di tempo. Questo può essere un valore negativo o positivo. Il valore predefinito è 0.

milliseconds: specifica il numero di millisecondi nell'intervallo di tempo. Questo può essere un valore negativo o positivo. Il valore predefinito è 0.

minutes: specifica il numero di minuti nell'intervallo di tempo. Questo può essere un valore negativo o positivo. Il valore predefinito è 0.

hours: specifica il numero di ore nell'intervallo di tempo. Questo può essere un valore negativo o positivo. Il valore predefinito è 0.

weeks: specifica il numero di settimane nell'intervallo di tempo. Questo può essere un valore negativo o positivo. Il valore predefinito è 0.
         
"""