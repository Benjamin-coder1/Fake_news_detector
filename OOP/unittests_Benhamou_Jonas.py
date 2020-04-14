import unittest
from comptebancaire import CompteBancaireLCL,NotEnoughtMoney,CompteSalarie,NotRealMoney,LimitePlafond,BadInput

class KnownValues(unittest.TestCase):
    known_values = (
        (
            CompteSalarie("Benhamou","Jonas",20,100),
            1000,
            1100
        ),
        (
            CompteSalarie("Benhamou","Jonas",20,-700),
            300,
            -400
        ),
        (
            CompteSalarie("Benhamou","Jonas",20,600),
            100,
            700
        )
    )

    def test_add_money(self):
        #On verifie que le compte a bien le bon solde apres virement
        for compte,virement,known in self.known_values:
            compte.add_money_Salarie(virement)
            self.assertEqual(known, compte.solde)


class CompteBadInput(unittest.TestCase):

    def test_limite_plafond(self):
        #On verifie que le plafond du salarie ne peut pas etre depasse
        cs=CompteSalarie("Benhamou","Jonas",21,100)
        self.assertRaises(LimitePlafond,cs.add_money_Salarie,5000)

    def test_init(self):
        #On verifie que l'initialisation est possible
        self.assertRaises(BadInput,CompteSalarie,"Benhamou","Jonas","vingt et un ans",100)
        self.assertRaises(BadInput,CompteSalarie,565,"Jonas",21,889)

    def test_solde_insufisant(self):
        #Pas de virment possible si le solde est insufisant
        cs=CompteSalarie("Benhamou","Jonas",21,100)
        self.assertRaises(NotEnoughtMoney,cs.remove_money,200)

if __name__ == "__main__":
    unittest.main()
