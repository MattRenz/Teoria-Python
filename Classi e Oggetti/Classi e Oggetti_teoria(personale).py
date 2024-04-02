#CLASSI 

#Una classe è come un costruttore di oggetti o un "progetto" per la creazione di oggeti
class MyClass: 
    x = 5
print(MyClass)    #<5>

#Creazione oggetto
class  MyClass:
    x = 5
p1 = MyClass    #oggetto P1
print(p1.x)

#FUNZIONE __init__()  assegna dei valori. esempio: 
class Persona:                              #creazione classe Persona
  def __init__(self, nome, cognome, eta):   # __init__() assegnazioni i valori alle proprietà dell'oggetto (nome, cognome, ecc)
    
    self.nome = nome
    self.cognome = cognome                  #richiamo dei valori assegnati creazione ogg.
    self.eta = eta

p1 = Persona("Matteo", "Renzi", 20)         # ora possiamo creare quanti oggetti Persona vogliamo
p2 = Persona("Davide", "Renzi", 15)         


print(f'{p1.nome}, {p1.cognome}, {p1.eta}')
print(f'{p2.nome}, {p2.cognome}, {p2.eta}')  

#FUNZIONE __str__()  controlla cosa deve essere restituito quando l'ogetto della classe è rappresentato con una stringa, esempio: 
class Persona: 
    def __init__(self, nome, cognome, eta):
        
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        
    def __str__(self):
        return f"Nome e Cognome: {self.nome} {self.cognome}" #ora richiamando l'oggetto, p1 o p2 o qualsiasi altro oggetto ci stampera SOLO nome e cognome
    
p1 = Persona("Matteo", "Renzi", 20)
p2 = Persona("Davide", "Renzi", 15)

print(p1) #print <Matteo Renzi>
print(p2) #print <Davide Renzi>
print(p2.nome, p2.cognome, p2.eta) #print <Completo p2>


#METODO OGGETTO gli oggetti possono contenere metodi, esempio: 
class Persona:
  def __init__(self, nome, cognome, eta) -> None:
    self.nome = nome
    self.cognome = cognome
    self.eta = eta
    
  def funzione(self): 
    
    '''creazione funzione(), il parametro SELF è un riferimento all'istanza 
    corrente della classe e viene utilizzato per accedere alle variabili che appetengono alla classe'''
    
    print("Ciao il mio nome è " + self.nome)  
    
p1 = Persona("Matteo", "Renzi", 20)
p2 = Persona("Davide", "Renzi", 15)

#p1.funzione() stampa  l'oggetto p1(le sue variabili) con la funzione() cioè la stringa con la variabile self.nome

p1.funzione() #print <Ciao il mio nome è Matteo>
p2.funzione() #print <Ciao il mio nome è Davide>

#SELF 
#Viene utilizzato per accedere alle variabili che appartengono alla classe, non siamo obbligati a chiamarlo self

#Modifica oggetto:
p1.eta = 40     #imposta l'età su 40

#Elimina proprietà oggetto
del p1.age      #elimina la proprietà dell'oggetto p1

#Elimina oggetto
del p1          #elimina p1

#Classe FIGLIO per creare una classe che EREDITI le funzionalità di un'altra classe, inseriamo la classe genitore come parametro durante la creazione della classe figlia, esempio:

class Alunni:
    def __init__(self, nome, congome, eta) -> None:
        self.nome = nome
        self.cognome = congome
        self.eta = eta
        
    def Stampa(self):
        print(f'Nome: {self.nome}, Cognome: {self.cognome}, Età: {self.eta}')

class Professori(Alunni):   #Classe professori eredita le stesse proprietà della classe Alunni
    pass

Alunni01 = Alunni("Mario", "Rossi", 19)
Alunni02 = Alunni("Giulo", "Figaro", 19)

Professori01 = Professori("Antonio", "Carpato", 56)

Alunni01.Stampa()
Alunni02.Stampa()   #esegue la funzione stampa() che stampa nome, cognome, e eta degli oggetti che noi impostiamo
Professori01.Stampa()

# .super()
class Professori(Alunni):
    def __init__(self, nome, congome, eta) -> None:
        super().__init__(nome, congome, eta)
        #super farà ereditaree alla classe figlia tutti i metodi dal suo genitore
   
#Aggiungi proprietà 
class Professori(Alunni):
    def __init__(self, nome, congome, eta) -> None:
        super().__init__(nome, congome, eta)
        
        self.aggiunta = 0   #Aggiunge una proprietà alla classe PROFESSORI
        

#ITERAZIONE #iter()metodo che viene utilizzato per ottenere un iteratore:
Tupla = ("BMW", "Porsche", "Supra")

MyIter = iter(Tupla)  #iterizza la tupla

print(next(MyIter)) #<MBW>
print(next(MyIter)) #<Porsche>
print(next(MyIter)) #<Supra>
#CLASSI 
