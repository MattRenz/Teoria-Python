""" 
Creare classe docente, attributi: Nome, Cognome, Idetnificativo, Lista Corsi insegnati. Con vari metodi calcola corsi insegnati

Con metodi inserisci docente, inserisci corso, calcola corsi insegnati
"""

import persona

class docente(persona.persona):

    profilo = "docente" 

    def __init__(self, nome, cognome, identificativo, mail, listaCorsiInsegnati = None):
        super().__init__(nome, cognome, mail)

        self.__identificativo = identificativo

        self.__nome = nome

        self.__cognome = cognome

        self.__mail = mail

        if listaCorsiInsegnati == None:

            self.__listaCorsiInsegnati = []

        else:
            self.__listaCorsiInsegnati = listaCorsiInsegnati


    def AggiungiCorso(self, corso):
        self.__listaCorsiInsegnati.append(corso)


    def CreaDatiDocente(self):

        stringaDocente = f'{self.__nome};{self.__cognome};{self.__identificativo};{self.__mail};'

        for voti in self.__listaCorsiInsegnati:

            stringaDocente = stringaDocente + str(voti) + ";"

        return stringaDocente


    def GetIdentificativo(self):

        return str(self.__identificativo)
    


