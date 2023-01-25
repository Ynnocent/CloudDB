from firebase import Firebase
from configClass import Config
from userInput import User

class firebaseProcess(Config, User):
    
    firebaseConfig = Config.config
    firebase = Firebase(firebaseConfig)

    db = firebase.database()

    users = db.child("users").get()



def addUsers(new_user:dict):
    new_user = {
        "name": new_user["name"],
        "age": new_user["age"],
        "major": new_user["major"]
    } 
    firebaseProcess.db.child("users").push(new_user)
