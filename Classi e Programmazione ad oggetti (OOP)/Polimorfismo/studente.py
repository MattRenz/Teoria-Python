
import persona


class studente(persona.persona):
    
    def __init__(self, nome, cognome, dataDiNascita, aula) -> None:
        super().__init__(nome, cognome, dataDiNascita)
        
        self.__aula = aula
        
        
    def mostraStudente(self):
        
        persona.persona.SchedaPersonale()
        print(f'Aula: {self.__aula}')
        
studente1 = studente("Matteo", "Renzi", "23/12/2002", "5AT")

studente1.mostraStudente()



class insegnante(persona.persona):
    
    def __init__(self, nome, cognome, dataDiNascita, matricola):
        super().__init__(nome, cognome, dataDiNascita)
        
        self.__matricola = matricola
        
        
    def mostraInsegnante(self):
        
        persona.persona.SchedaPersonale()
        print(f'Matricola: {self.__matricola}')
        
insegnante1 = insegnante("Marco", "Rossi", "23/12/1980", 2345)

insegnante1.mostraInsegnante()       
        

        
        
        
        
        
    
        
        