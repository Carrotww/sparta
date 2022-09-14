from pprint import pprint

class Calc():
    def __init__(self):
        try:
            print('실행')
            self.num1 = int(input())
            self.num2 = int(input())
        except:
            print('input only numbers')
            
    
    def plus(self):
        return self.num1 + self.num2
    
    def minus(self):
        return self.num - self.num2
    
    def multiple(self):
        return self.num * self.num2
    
    def divide(self):
        try:
            return self.num1 / self.num2
        except ZeroDivisionError:
            return print('Can\'t Division for Zero')

class Profile:
    def __init__(self, people):
        self.people = people
    
    def Profile_filter(self):
        return [x for x in filter(lambda x: x[2] >= 20, self.people)]
    

people = [
    ("Blake Howell", "Jamaica", 18, "aw@jul.bw"),
    ("Peter Bowen", "Burundi", 30, "vinaf@rilkov.il"),
    ("Winnie Hall", "Palestinian Territories", 22, "moci@pacivhe.net"),
    ("Alfred Schwartz", "Syria", 29, "ic@tolseuc.pr"),
    ("Carrie Palmer", "Mauritius", 28, "fenlofi@tor.aq"),
    ("Rose Tyler", "Martinique", 17, "as@forebjab.et"),
    ("Katharine Little", "Anguilla", 29, "am@kifez.et"),
    ("Brent Peterson", "Svalbard & Jan Mayen", 22, "le@wekciga.lr"),
    ("Lydia Thornton", "Puerto Rico", 19, "lefvoru@itbewuk.at"),
    ("Richard Newton", "Pitcairn Islands", 17, "da@lasowiwa.su"),
    ("Eric Townsend", "Svalbard & Jan Mayen", 22, "jijer@cipzo.gp"),
    ("Trevor Hines", "Dominican Republic", 15, "ev@hivew.tm"),
    ("Inez Little", "Namibia", 26, "meewi@mirha.ye"),
    ("Lloyd Aguilar", "Swaziland", 16, "oza@emneme.bb"),
    ("Erik Lane", "Turkey", 30, "efumazza@va.hn"),
]
test = Profile(people)
pprint(test.Profile_filter())


# test = Calc()
# print(test.plus())
