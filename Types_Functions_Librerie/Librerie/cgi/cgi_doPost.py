from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi

""" 
Libreria di scripting per la creazione di pagine web dinamiche. 
Consente l'elaborazione di dati inviati dal browser web all'applicazione web attraverso forum HTML

In particolare cgi.FieldStorage analizza i dati inviati dal forum HTML tramite il metodo HTTP Post o Get. 
Analizza la richiesta HTTP inviata dal browser al server web e recupera i dati dal form HTML. 
"""


class MyServer(BaseHTTPRequestHandler):

    def do_POST(self):
        
        
        form = cgi.FieldStorage( 
                            
            fp=self.rfile, # corpo richiesta inviata al server
             
            headers=self.headers, # specifica gli headers della richiesta HTTP
           
           
          # environ = ambiente dove viene eseguito lo scrypt python  
          
            environ={'REQUEST_METHOD':'POST', # definisce il metodo di richiesta in questo caso POST 
                     
                     'CONTENT_TYPE':self.headers['Content-Type'], # il tipo di contenuto della richiesta (ricavato dagli headers)
                
                     })


        # ora usiamo l'oggetto form per definire con getValue() quali elementi vogliamo che si vedano sulla pagina HTML 
        name = form.getvalue("name")
        cognome = form.getvalue("cognome") 
        email = form.getvalue("email")

        self.send_response(200)
    
        self.send_header('Content-type','text/html') # il contenuto della risposta sarà in formato HTML
        self.end_headers()

        message = f"Hello {name} {cognome}! <hr> <br>Your email is: {email}" # questa è la risposta con gli input forniti nel forum dall'utente
        
        self.wfile.write(bytes(message, "utf8"))
        return
    
    def run():
        
        server_address = ('127.0.0.1', 8080)
        httpd = HTTPServer(server_address, MyServer)
        
        print('running server...')
        httpd.serve_forever()