# Getter Setter in Java Style
class Student:
    def __init__(self, fname, lname, blood):
        self.fname = fname
        self.lname = lname
        self.blood = blood

    def __str__(self):
        return "{} {}, blood group {}".format(self.fname, self.lname, self.blood)

class Person:
    def __init__(self, fname, lname, blood):
        self.fname = fname
        self.lname = lname
        self.setBlood(blood)
    
    # Getter Function
    def getBlood(self):
        return self.__blood

    # Setter Function
    def setBlood(self, blood):
        if blood.upper() in ["A", "B", "AB", "O"]:
            self.__blood = blood.upper()
        else:
            raise ValueError("invalid blood group")

    def __str__(self):
        return "{} {}, blood group {}".format(self.fname, self.lname, self.__blood)


if __name__ == '__main__':
    s1 = Student("Perm", "Chumpae", "B")
    s1.blood = "Y"
    print(s1)

    s2 = Person("Perm", "Chumpae", "B")
    print(s2)
