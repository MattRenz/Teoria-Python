
import re # una sequenza di caratteri che forma un modello di ricerca, può essere utilizzato per verifica se una strinnga continene il modello di ricerca che gli specifichiamo

testo = "Ciao sto usando python"
ricerca = re.search("^Ciao.*python$", testo) # ricerca se inizia (^) e se finisce (*parola$)

re.findall() # restituisce un elenco corrente di tutte le corrispondenze

re.search() # funzione cerca una corrispondenza nella stringa e restituisce un oggetto match se c'è una corrispondenza

# {} numero di occorenze

# ^ inizia con 

# \ mostra i caratteri speciali tipo \.

# % finisce con 

# \d cerca tutti i caratteri a cifra 

# parola|parola cerca se sono presenti due parole

# \Aciao controlla se la parola della stringa inizia con ciao

# r"\bain" controlla se una parola della stringa inizia con "ain"

# r"parola\b" controlla se una parola della stringa finisce con "ain"

# r"\Bain" controlla se nella stringa è presete la parola ain ma non all'inizio

# \D ritorna ogni singolo caratter della stringa che non sia un numero

# \s restituisce tutti gli spazi

# \S restituisce tutti i NON spazi della frase

# Fine\Z controlla se la stringa finisce con "Fine"

# [arn] se la stringa a un carattere tra a r n

# [a-n] se la stringa a dei caratteri tra a e n

# [^arn] tutti i caratteri esclusi arn

# [0123] se è presente almeno uno di questi numeri

# [0-9] se la stringa contiene un numero tra 0 e 9

# [05][0-9] controlla se la stringa contiene numeri da 00 a 59

# [azA-Z] controlla se sono presenti caratteri dell'alfabeto in maiuscolo o in minuscolo

# % controlla se la la stringa ha qualche carattere % (il carattere può essere qualsiasi)
 
 
