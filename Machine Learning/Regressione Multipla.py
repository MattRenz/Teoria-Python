import pandas 


dif = pandas.read_csv("C:\\Users\\Matteo\\OneDrive\\Desktop\\Data Scientist\\Python\\Teoria e appunti\\Machine Learning\\data.csv")
# tramite il modulo pandas leggiamo il file csv

X = dif[["Weight", "Volume"]] 
# valori indipendenti del file csv (se aprimao il file data.csv, vedremo i valori Weight e Volume)

y = dif[["CO2"]] 
# valore dipendente 


from sklearn import linear_model
# da sklearn importiamo linear_model 

reger = linear_model.LinearRegression()
# useremo LinearRegression() metodo per creare un oggettto di REGRESSIONE LINEARE

reger.fit(X, y)
# l'oggetto precedente ha un metodo chiamato fit() che prende i valori indipendenti ("Weight", "Volume") e i valori dipendenti (CO2) come paramteri e riempe l'oggetoo di regressione con i dati che descrivono la relazione


# Ora abbiamo un oggetto di regressione pronto a prevedere i valori di C02 in base al peso e al volume di un'auto


predictedCO2 = reger.predict([[2300, 1300]]) 
# gli passiamo i valori:
# Peso: 2300 e Volume: 13000


print(predictedCO2) # <107.2087328>

# abbiamo un motore da 1,3 litri e un peso di 2300Kg che rilascia circa 107g di C02 per ogni chilometro













