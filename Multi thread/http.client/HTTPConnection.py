import http.client

""" 
http.client è un libreria che fornisce interfaccie per le richieste e per le risposte HTTP 

http.client implementa un client HTTP personalizzato che può inviare richieste HTTP a un server e
gestire le risposte del server

In particolare la libreria che vedremo è HTTPConnection che rappresenta una connessione a un server HTTP 
"""

class MyHttpClient():
    
    def __init__(self, nomeHost, porta) -> None:

        self.__nomeHost = nomeHost
        self.__porta = porta


    def SendHTTPData(self, url, data):

        connection = http.client.HTTPConnection(self.__nomeHost,self.__porta,timeout=10) # qui creiamo l'ogetto HTTPConnection, specificando il nome dell'host e la porta
        
        connection.request("GET", url + "?" + data) # con l'oggetto HTTPConnection usiamo il metodo request()
        # request() invia un richiesta HTTP di tipo "GET" al url specficiato
        """
        GET = metodo HTTP utilizzaato
        url = url a cui inviare la richiesta nel formato specifico
        data = i dati passsati alla funzione che nel nostro caso sono il l'accoppiamento di parametro e valore
        
        quindi l'unione di url e data porterà a questo percorso:
        
            /SalvaStudente?Nome=Matteo&Cognome=Renzi&Matricola=2345&Email=mattrenz9@gmail.com
            
            ? = separa url dai parametri
            & separa i parametri tra loro
        """ 
    
        response = connection.getresponse() # getresponse() ottenie la risposta dal server 
        """
        Cioè quando al server arriverà la richiesta /SalvaStudente.... lui eseguira il comando 
        """

