""" 
Una classe può nascere da una specializzazione rispetto ad una classe padre
Qundo una classe è una classe "figlia" erdedita tutti gli attributi e i metodi principali della classe padre
"""

class Persone:
    
    def __init__(self, nome, cognome, eta, residenza) -> None:
        
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.residenza = residenza
        
    
    def scheda_personale(self):
        
        print(f'Nome: {self.nome} Cognome: {self.cognome} Eta: {self.eta} Residenza: {self.residenza}')       
    
    
    
    
    
    
        
