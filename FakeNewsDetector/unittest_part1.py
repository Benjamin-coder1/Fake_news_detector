import part1
import unittest

class RandomTest(unittest.TestCase):

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
            self.assertTrue(part1.scooring_1(url)>=80)

    def test_titres(self):
        #On test que notre algo arrive a acceder a new Api pour rechercher les titres
        #On verifie que le score est superieur a 80 car cce sont de vraies nouvelles

        titres_true=['the earth is flat',
        'Donald Trump is the president of USA',
        'Car sales picked up at the end of April, AutoNation says.']

        for titre in titres_true:
            self.assertTrue(part1.scooring_1(titre)>=80)
            
if __name__ == '__main__':
    unittest.main()    
