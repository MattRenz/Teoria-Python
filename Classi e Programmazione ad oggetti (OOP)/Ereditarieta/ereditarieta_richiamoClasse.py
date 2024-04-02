
import ereditarieta as ere # "ereditarieta" nome file

class insegnante(ere.Persone): # nome file + nome cdella classe padre dentro la classe dentro la classe figlio, per definirlo 
    
    profilo = "insegnante"
    
    def __init__(self, nome, cognome, eta, residenza, materie) -> None:
        super().__init__(nome, cognome, eta, residenza) # classe padre 
        
        if materie is None:
            
            self.materie = []
        else: 
            self.materie = materie
            
            
    def MostraInsegnante(self):
        
        ere.Persone.scheda_personale()
        print(self.materie)


insegnante1 = ere.Persone("Mario", "Rossi", 20, "Via giuolo 30")           

insegnante1.scheda_personale()
            
""" 
La classe insegnante è filgia della classe persona.

Un oggetti di quella classe eredita attirbuti e i metodi della classe persona, ed in più ha i propri metodi e attributi tipici dell'insegnante
"""
            
        
        
    