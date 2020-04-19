import error

class Color : 
    """ cette classe va servir a rendre le travail plus lisible en ajoutant des couleurs un peu partout
    syntaxe : print(color(mot, 'n'/'r'/'v'/'o'/'b'/'v'/'t']))"""
    def __init__(self,msg,color) : 
        color_value = { 'n':30, 'r':31, 'g':32, 'o':33,'b':34,'v':35,'t':36}
        if (type(msg) != str) or (type(color) != str) or (color not in ['n','r','g','o','b','v','t']) : 
            raise error.ErrorColor
        self.msg = msg
        self.num_color = color_value[color]

    def __str__(self) : 
        color_value = { 'n':30, 'r':31, 'g':32, 'o':33,'b':34,'v':35,'t':36}
        return "\033[" + str(self.num_color) + "m" + self.msg + "\033[0m"



