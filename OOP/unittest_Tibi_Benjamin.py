import vivant
import unittest



class BadInput(unittest.TestCase) :
    def test_input_humain(self) : 
        """ les entree doivent etre correcter /une ou plusieurs sont mauvaise"""
        self.assertRaises(vivant.ErreurInitialisation, vivant.Humain,"1","1","1",1,1)

    def test_input_animal(self) : 
        """ les entree doivent etre correcter /une ou plusieurs sont mauvaise"""
        self.assertRaises(vivant.ErreurInitialisation, vivant.Animal,"1","1","1",1,1)

    def test_mauvais_demenagement(self) : 
        """un animal doit etre demenager dans un endroit air/terre/eau"""
        animal1 = vivant.Animal(1,1,1,"1","air")
        self.assertRaises(vivant.DemeagementInterdit, animal1.demenage,"1")

class OpeSurIndiv(unittest.TestCase) : 

    def test_manger(self) : 
        poid_ini = 10
        animal1 = vivant.Animal(1,1,poid_ini,"1","air")
        self.assertRaises(vivant.NegativeWeight, animal1.manger, -10)



        

if __name__ == '__main__':
    unittest.main()
