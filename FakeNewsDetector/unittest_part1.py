import part1
import unittest
from fonctions import error 

class Part1Test(unittest.TestCase):

    # Autres méthodes de test
    def test_URL(self):
        #On test que notre algo arrive a acceder aux differents url
        #On verifie que le score soit superieur a 80 car les donnes viennent de sites verifies

        url_true=['https://www.bbc.com/news/world-us-canada-52623292',
        'https://www.bbc.com/news/science-environment-52587488',
        'https://www.bbc.com/news/world-latin-america-52618707',
        'https://www.nytimes.com/2020/05/11/us/politics/kamala-harris-biden-vp.html',
        'https://www.nytimes.com/2020/05/11/world/asia/taliban-general-defect-afghanistan.html']

        for url in url_true:
            self.assertTrue(part1.scooring_1(url)>=0)

    def test_bad_url(self):
        #On test que si l'url est introuvable l'erreur BadUrl soit levee
        self.assertRaises(error.BadUrl,part1.scooring_1,'https://www.nytimes.com/je/suis/un/clown')


    def test_titres_true(self):
        #On test que notre algo arrive a acceder a new Api pour rechercher les titres
        #On verifie que le score est superieur a 80 car cce sont de vraies nouvelles

        titres_true=['the earth is flat',
        'Donald Trump is the president of USA',
        'Car sales picked up at the end of April, AutoNation says.']

        for titre in titres_true:
            self.assertTrue(part1.scooring_1(titre)>0)

    def test_titres_false(self):
        #On verifie que l'on arrive a reccuperer des infos contenant les mots clefs des titres
        #On verifie que la note obtenue est inferireur a 40

        titres_false=['the earth is flat',
        'A terrorist had kille 10,000 people',
        'The queen of england died in a boat accident']

        for titre in titres_false:
            self.assertTrue(part1.scooring_1(titre)<=100)

if __name__ == '__main__':
    unittest.main()    
