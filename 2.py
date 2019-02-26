# @Property Decorator
class Student:
    def __init__(self, s_id, fname, lname):
        self.s_id = s_id
        self.fname = fname
        self.lname = lname
    def full_name(self):
        return "{} {}".format(self.fname, self.lname)

    @property
    def full_name2(self):
        return "{} {}".format(self.fname, self.lname)
    @property
    def join_yy(self):
        return self.s_id[:2]

    @property
    def degree(self):
        return self.s_id[2]

    @property
    def seq(self):
        return self.s_id[-3]

    @property
    def check_digit(self):
        return self.s_id[-2:]

if __name__ == '__main__':
    s = Student("550510425", "Permpoon", "Chao")
    print("Full Name: ", s.full_name2)
    print("Join Years: ", s.join_yy)
    print("Degree: ", s.degree)
    print("Sequence: ", s.seq)
    print("Signature Digit: ", s.check_digit)
