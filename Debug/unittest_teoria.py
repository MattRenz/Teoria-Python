import unittest 

unittest.TestCase() # E' una classe che definisce metodi per confrontare tra di loro gli argomenti

# assertEqual() = Confronta il primo argomento con il secondo argomento se sono uguali CONTINUA altrimenti solleva un'eccezione

# assertNotEqual() = Confronta il primo argomento con il secondo se NON sono uguali CONTINUA altrimenti solleva un'eccezzione

# assertTrue() = Verifica se l'istruzione data è vera e solleva un Errore se l'istruzione data è falsa

# assertFalse() = Verifica se l'istruzione data è falsa e solleva un Errore se l'istruzione data è vera


# TEST assertTrue()
class Test(unittest.TestCase):
    
    def test_assertTrue(self):
        x = 5
        self.assertTrue(x  < 10, "ERROR: L'istruzione dovrebbe essere vera")
        
#TEST assertFalse()

    def test_assertFalse(self):
        x = 5
        self.assertFalse(x > 1, "ERROR L'istruzione dovrebbe essere falsa")
        
#TEST assertEqual()

    def test_assertEqual(self):
        
        x, y = 5, 5
        somma = x + y
        self.assertEqual(somma, 10, "ERROR: Dovrebbe essere 10")
            
#TEST assertNotEqual()

    def test_assertNotEqual(self):
        x,y = 5, 5
        somma = x + y
        self.assertNotEqual(somma, 11, "ERROR: Non deve venire 10")
        

    def funzione(self):
        x = 5
        self.assertTrue(x == 10, "Error")
            


if __name__ == '__main__':
    unittest.main()         # per eseguire i test