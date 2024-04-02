""" 
Polimorfismo si intende il fatto che posso chiamare due metodi con lo stesso nome;
e questi due moetodi possono fare cose diverse, perché richimati in contesti  diversi e con parametri diversi
"""

class persona():
    
    def __init__(self, nome, cognome, dataDiNascita) -> None:
        
        
        self.__nome = nome
        self.__cognome = cognome
        self.__dataDiNasciata = dataDiNascita
        
        
    def SchedaPersonale(self):
            
        print(f'Nome: {self.__nome} \n Cognome: {self.__cognome} \n Data di nascita: {self.__dataDiNasciata}')
        
        
    
    
    
        