class NotEnoughtMoney(Exception) : pass
class NotRealMoney(Exception) : pass
class LimitePlafond(Exception) : pass
class ErrorType(Exception) : pass
class BadInput(Exception) : pass

class CompteBancaireLCL :
    nombre_de_compte = 0

    def __init__(self, Nom, Prenom, Age, Solde, Statut) : 
        if (type(Nom) is str) and (type(Prenom) is str) and (type(Age) is int) and (type(Statut) is str) : 
            self.nom = Nom
            self.prenom = Prenom
            self.age = Age
            self.banque = "LCL"
            self.solde = Solde
            self.statut = Statut
            CompteBancaireLCL.nombre_de_compte += 1
        else : 
            raise BadInput

    def add_money(self, money) : 
        """helllllo"""
        if money >= 0 : 
            self.solde += money
            print("New solde : {} €".format(self.solde))
        else : 
            raise NotRealMoney

    def remove_money(self, money) : 
        if self.solde >= money : 
            self.solde -= money
            print("New solde : {} €".format(self.solde))
        else : 
            raise NotEnoughtMoney 


class CompteSalarie(CompteBancaireLCL) : 

    def __init__(self,Nom, Prenom, Age, Solde) : 
        """"compte special avec un plafond de retrait de 2000€  max"""
        self.plafond = 2000
        if Solde > self.plafond : 
            raise LimitePlafond
        CompteBancaireLCL.__init__(self,Nom, Prenom, Age, Solde,"salarie")
        

    def add_money_Salarie(self, money) :
        if (money + self.solde) > self.plafond : 
            raise LimitePlafond 
        else : 
            CompteBancaireLCL.add_money(self,money)


class ComptePatron(CompteBancaireLCL) : 

    def __init__(self,Nom, Prenom, Age, Solde) : 
        """"compte special sans plafon de retrait enorme qui ne verse de l'argent qu'aux salariés"""
        CompteBancaireLCL.__init__(self,Nom, Prenom, Age,Solde,"Patron")
        self.plafond = 20000

    def add_money_Salarie(self, money, salarie) :
        if type(salarie) is CompteSalarie : 
            CompteSalarie.add_money_Salarie(salarie,money)
        else :
            raise ErrorType

        




