class User:
    
    def __init__(self, name:str, age:int, major:str):
        
        self.name = name
        self.age = age
        self.major = major

        self.userinfo = {
            "name": self.name,
            "age": self.age,
            "major": self.major
        }
    def createUser( name, age, major):
        return User(name, age, major)

    def getName(self):
        return str(self.name)
    
    def getAge(self):
        return int(self.age)
    
    def getMajor(self):
        return str(self.major)
    
    def getUserDict(self):
        return dict(self.userinfo)

def createNewUser():
    name : str = str(input("Enter Name: "))
    age : int = int(input("Enter Age: "))
    major : str = str(input("Enter Major: "))
    if name and age and major:
        newUser = User.createUser(name, age, major)
    else:
        print("Error")
    return newUser

