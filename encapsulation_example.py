#Object Oriented Programming

#1.Encapsulation: Combining Data and Functions into a class
#2.Abstraction: Hiding Backgroung Data (Through Methods)
#3.Inheritance: Property of aquiring data and methods of Parent class by child class
#4.Polymorphism: Overloading: Methods with same name but different params
#                Overrididng: Methods with same name but present in diffrent class(usually in Parent-Child)

#Class and Object example (Encapsulation)

class User():
    def __init__(self,isuser):              #isuser is a attribute
        self.isuser=isuser
    def login(self):                            #login is method
        if self.isuser==True:
            print('You are Logged in')
        else:
            print('You are not a user')

user1 = User(True)
print(user1.isuser)
user1.login()

user2 = User(False)
user2.login()
