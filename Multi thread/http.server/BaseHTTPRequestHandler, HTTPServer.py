from http.server import BaseHTTPRequestHandler, HTTPServer
import http.server



http.server
""" 
http.server = modulo integrati per avviare un server web HTTP o HTTPS

il modulo http.server fornisce diverse classi d iserver HTTP, tra qui:
BaseHTTPRequestHandler e HTTPServer

"""

BaseHTTPRequestHandler 
""" 
Gestice le richieste di HTTP, è la classe base usata per la creazione di server HTTP, 
fornise diversi metodi per il ciclo di vita di una richiesa HTTP:
"""

class MyHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_Get(self): # metodo chiamato quando il server riceve una richiesta HTTP Get (recupero informazioni da un server web)
        
        self.send_response() # invia una risposta HTTP al client
        # All'interno specifichiamo il codice di risposta
        
        self.send_header() # invia una intestazione HTTP al client
        # intestazione = informazione aggiuntiva sulla richiesta o sulla risposta, qui gli diciamo il tipo di dato della risposta, quindi se una foto un video un formato html e così via
        
        self.end_headers() # termina la scrittura di intestazione HTTP
         
        self.wfile.write() # invia i dati di risposta dal HTTP al client.
        # All'interno specifichiami il messaggio che costituirà il corpo della risposta
        
    def do_Post(): # metodo chiamato quando il server riceve una richiesa HTTP Post (invio dati da un client a un serer web)
        pass
    

"""
In send_header() specifichiamo l'intestazione, "Content-type" indica il contenuto della risposta, i formati oltre quelo visto sono:

application/json: per i dati in formato JSON

application/xml: per i dati in formato XML

image/png: per le immagini in formato PNG

audio/mpeg: per i file audio in formato MP3

video/mp4: per i file video in formato MP4

"""
    
HTTPServer 
""" 
Rappresenta un sever HTTP ha diverse funzionalità come la gestione delle richieste HTTP, l'ascolto su porte specifiche. 

E' usata in combinazione con BaseHTTPRequestHandler

In particolare passiamo un'istanza della classe al costruttore ddella classe per specificare il gestore delle richieste HTTP:
"""

httpd = HTTPServer("server_address",MyHTTPRequestHandler) # ogg HTTPServer, che ha come parametri, l'indirizzo del server, a appunto la nostra clsse, che gestisce le richieste HTTP

httpd.serve_forever() # Avvia il server HTTP e lo fa rimanere sempre in esecuzione (ascolto)



    
