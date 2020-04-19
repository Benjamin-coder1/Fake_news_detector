
class BadDictio(Exception) : pass
class FaillureRecupData(Exception) : 
    def __init__(self) : 
        print("The recover of data had fail")


