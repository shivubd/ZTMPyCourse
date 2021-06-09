#Abstraction

class User():
    def __init__(self,isuser):  
        self.isuser=isuser
    def login(self):                            
        if self.isuser==True:
            print('You are Logged in')
        else:
            print('You are not a user, Create one')

class Wizard(User):                 #Wizard class is inherited from User, i.e. User is parent class of Wizard
    def __init__(self,isuser,name,power):
        super().__init__(isuser)
        if self.isuser==True:
            self.name = name
            self.power = power
    def check_power(self):
        print(f'{self.name} has {self.power} power left.')

class Archer(User):                 #Archer class is inherited from User, i.e. User is parent class of Archer
    def __init__(self,isuser,name,arrows):
        super().__init__(isuser)
        if self.isuser==True:
            self.name = name
            self.arrows = arrows
    def check_arrows(self):
        print(f'{self.name} has {self.arrows} arrows left.')

user1 = Wizard(False,'Shivu',200)
user1.login()
user2 = Archer(True,'Akash',137)
user2.check_arrows()
    

