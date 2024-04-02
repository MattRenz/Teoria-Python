
import smtplib # libreria utilizzata per inviare email

email = smtplib.SMTP() # fornisce un interfaccia per inviare e-mail. Richiede 2 parametri il nome del server e la porta del server

email.ehlo() # inizia la comunicazione con il server di posta elettromnica 

email.starttls() # avvia uan negozziazzione di sicurezza con server (cittografa la connessione)

email.login() # si autentica con il server. Richiede due parametri, l'indirizzo email dell'account e la password

email.sendmail() # sendmail() invia un messaggio di posta elettronica. Richiede 3 parametri, l'indirizzo email del mittente, l'indirizzo email del destinatario, e il messaggio 

email.quit() # quit() chiude la connessione con il server di posta elettronica dopo aver completato l'invio di messaggi di posta elettronica 
