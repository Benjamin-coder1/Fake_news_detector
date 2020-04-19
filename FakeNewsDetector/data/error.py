import color as c  
class ErrorColor(Exception) : 
    def __init__(self) : 
        print(c.Color("Color certainly doesn't exist !!","r"))
class BadDictio(Exception) : 
    def __init__(self) : 
        print(c.Color("Bad type of input","r"))
class FaillureRecupData(Exception) : 
    def __init__(self) : 
        print(c.Color("The recover of data had fail","r"))



