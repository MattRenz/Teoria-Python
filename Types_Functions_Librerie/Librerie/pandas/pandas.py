import pandas
import matplotlib.pyplot as plt

""" 
Pandas è una libreria per la manipolazione di dati in fomrato sequneziale o tabbellare. 

pandas.read_csv(file)
Permette di leggere file CSV e convertiri in un DataFrame (una struttura dati tabbellare bidimensionale)


Tramite questi dati possiamo usare la libreria matplotlib.pyplot per creare un grafico a Dispersione
che accetta due valori plt.scatter(x, y) dove x e y sono i punti che andrà a disegnare
"""

file = ""
data = pandas.read_csv(file)

"""
Come caricare vari formati di dati in python
"""

# CSV
df = pandas.read_csv('data.csv')

# Excel
df = pandas.read_excel('data.xlsx')

# JSON
df = pandas.read_json('data.json')

# Normale file di testo
with open('data.txt', 'r') as f:
    data = f.read()

