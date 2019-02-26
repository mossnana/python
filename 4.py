# Getter Setter in Python Style
class Person:
    def __init__(self, fname, lname, blood):
        self.fname = fname
        self.lname = lname
        self.blood = blood
    # Blood Property
    @property
    def blood(self):
        return self.__blood
    @blood.setter
    def blood(self, blood):
        if blood.upper() in ["A", "B", "AB", "O"]:
            self.__blood = blood.upper()
        else:
            raise ValueError("invalid blood group")

    # First Name Property
    @property
    def fname(self):
        return self.__fname

    @fname.setter
    def fname(self, fname):
        self.__fname = fname.strip().title()

    # Class Return Format
    def __str__(self):
        return "{} {}, blood group {}".format(self.fname, self.lname, self.blood)

# Main
if __name__ == '__main__':
    p1 = Person(" perm         ", "Chumpae", "B")
    print(p1)
    p1.blood = ("A")
    print(p1.blood)
