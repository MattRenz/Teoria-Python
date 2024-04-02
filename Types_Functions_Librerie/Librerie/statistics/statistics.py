
import statistics
''' 
Modulo statistico che si può usare per calcolare statistiche matematiche di dati numeri
'''

# statistics.harmonic_mean() / Calcola la media armonica. Media armonica = il reciproco della media aritmetica () dei reciproco dei dati
#(a, b, c, d) media armonica = nm. elementi / (1/a + 1/b + 1/c + 1/d)

print(statistics.harmonic_mean([10, 5, 20]))
# calcolo: 3÷((1÷10)+(1÷5)+(1÷20))
# <8,571428571>

# statistics.mean() / Calcola la media dei dati
print(statistics.mean([6, 7, 5.50])) # <6.16>

# statistics.median() / Calcola la mediana (valore medio) del dato, ordinare i dati in ordine crescente prima di calcolare la mediana
# calcolo mediana = somma di tutti i valori / il numero di valori

# Se il numero dei valori è dispari
print(statistics.median([3, 8, 10, 13, 17])) 
# calcolo: (3 + 8 + 10 + 13 + 17) / 5 = 10.2
# print = <10> Arrotonda da 10.2 a 10

# Se il numero dei valori è pari
print(statistics.median([4, 9, 22, 35]))
# calcolo: (9 + 22) / 2   Prende la media dei 2 numeri centrali 9 e 22
# print = <15.5>


# statistics.median_high() / Calcola la mediana alta del set.
# Se il numero dei valori è dispari
print(statistics.median_high([1, 3, 5, 7, 9, 11, 13]))
# calcola la media dei numeri. print <7>

#Se il numero dei valori è pari
print(statistics.median_high([1, 3, 5, 7, 9, 11]))
# Se è pari calcola il maggiore dei due valori intermedi


# statistics.median_low() / Calcola la mediana bassa del set.
# Se il numero dei valori è dispari
print(statistics.median_low([1, 3, 5, 7, 9, 11, 13]))
# calcola la media dei numeri. print <7>

#Se il numero dei valori è pari
print(statistics.median_low([1, 3, 5, 7, 9, 11]))
# Se è pari calcola il minore dei due valori intermedi


# statistics.mode() / Calcola la 'moda', la (tendenza centrale)
print(statistics.mode([2, 5, 6, 7, 2, 6, 10, 12, 2, 5, 29, 30, 2]))
# <2>, 2 Perchè nell'insieme di dati il numero che viene ripetuto più volte è 2

# statistics.pstdev() / Calcola la deviazione standard da un'intera popolazione.
# la deviazione standard è la radice quadrata della varianza campionaria .

# statistics.stdev() / Calcola la deviazione standard da un campione di dati.
# la deviazione standard è la radice quadrata della varianza campionaria .
