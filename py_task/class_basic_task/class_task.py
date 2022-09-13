import math

class Area:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def squre(self):
        return self.x * self.y
    
    def triangle(self):
        return (self.x * self.y) / 2
    
    def circle(self):
        return math.pi * ((self.x / 2) ** 2)

class Calc():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def plus(self):
        return self.num1 + self.num2
    
    def minus(self):
        return self.num - self.num2
    
    def multiple(self):
        return self.num * self.num2
    
    def divide(self):
        return self.num / self.num2

class Profile:
    def __init__(self):
       pass

    def set_profile(self, profile):
        self.name = profile['name']
        self.gender = profile['gender']
        self.birthday = profile['birthday']
        self.age = profile['age']
        self.phone = profile['phone']
        self.email = profile['email']
    
    def get_name(self):
        return self.name
    
    def get_gender(self):
        return self.gender
    
    def get_birthday(self):
        return self.birthday
    
    def get_age(self):
        return self.age
    
    def get_phone(self):
        return self.phone
    
    def get_email(self):
        return self.email
    
test = Profile()
test.set_profile({
    "name": "lee",
    "gender": "man",
    "birthday": "01/01",
    "age": 32,
    "phone": "01012341234",
    "email": "python@sparta.com",
})

print(test.get_name())
print(test.get_gender())
print(test.get_birthday())
print(test.get_age())
print(test.get_phone())
print(test.get_email())