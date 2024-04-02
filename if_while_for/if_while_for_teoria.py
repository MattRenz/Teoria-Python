#IF ELIF ELSE
''' if condizione istruzione: 
    elif condizione istruzione: 
    else istruzione finale:
'''

a = input("Inserisci un numero")
b = input("Inserisci un numero")
c = input("Inserisci un numero")

if b > c:
    print("B maggiore di A")
elif b < c:
    print("B minore di A")
else: print("B uguale ad A")

if a > b and a > c:     #and combina istruzione
#verifica se a è maggiore di b, AND se a è maggiore di C
    pass
if a > b or a > c:      #or combina istruzioni
#verifica se a è maggiore di b OPPURE se a  maggiorde di c   
    pass


#WHILE
'''
    while condizione(finchè è vera): 
        istruzione 
        istruzione
    else: stampa un messaggio qunado il ciclo non è più vero o è terminaro
'''

i = 1

while i < 6: #finchè i è minore di 6 stampa i e aggiungi 1 ad ogni passaggio 
    print(i)
    i +=1
    
while i < 6:    
    print(i)
    if i == 3:  #quando i è uguale a 3 interrompi il ciclo
        break   #ferma il ciclo
    i +=1

while i < 6:
    i += 1
    if i == 3: #quando i è uguale a 3 continua, interrompe l'iterazione corrente e passa alla successiva
        continue #continua con l'istruzione successiva
    print(i)


#FOR
'''
    for elemento in sequenza:
        istruzione
        istruzione
    else: stampa un messaggio quando il ciclo è terminato
'''

for n1 in range (1, 4):
    for n2 in range (1, 4):     #ciclo nidificato
        print(n1, n2)
        
#stampa due range da 1 a 3, e prennde il corrisposttivo di ogni numero
#in tutte le combinazioni, e inserisce tutte e due dentro la lista


