# INCAPSULAMENTO 

'''
Gli attributi hanno una visibilità, l'utilizzatore non accede direttamente a gli attriuti 
ma vi accede attraverso dei metodi
'''
class Facciata:

    def __init__(self):

        self.__colore = "verde" # con __ rendiamo l'attributo privato


    def MostraColoreFacciata(self):
        print(f'La facciata è di colore {self.__colore}')

    def ImpostaColoreFacciata(self, variante):

        self.__colore = variante


# istanza classe 

ColoreFacciata = Facciata() # non prende parametri perché è gia impostato un colore "verde"
#ColoreFacciata.MostraColoreFacciata() # <"verde"> richiamiamo la classe facciata, e gli passiamo il metodo MostraColoreFacciata

# modifica colore 
ColoreFacciata.__colore = "rosso" # qui definiamo la variabile "variante" dentro il metodo ImpostaColoreFacciata


ColoreFacciata.ImpostaColoreFacciata("rosso")

ColoreFacciata.MostraColoreFacciata() # qui richiamando sempre la classe Facciata gli passiamo il metodo ImpostaColoreFacciata, 
# E siccome prima gli abbiamo passato che la variante è rossa, stampera che il colore è rosso