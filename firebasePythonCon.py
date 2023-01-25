from userInput import User
import userInput
from firebaseClass import firebaseProcess
import firebaseClass

firebaseProcess.firebase

def fbAddUser():
    user = userInput.createNewUser()
    firebaseClass.addUsers(user.userinfo)
    print(f"{user.getName()} has been added to the database.")

def fbDelUser():
    name = str(input("Enter name you want to delete: "))
    userdb = firebaseProcess.db.child("users").get()

    for i in userdb.each():
        if (i.val()["name"] == name):
            key = i.key()
    
    firebaseProcess.db.child("users").child(key).remove()
    print(f"{name} has been remove from the database.")

def fbUpdateUser():
    name = str(input("Enter user's name to update: "))
    print("Choose: Name, Age, Major")
    update_field = str(input("What would you like to update: "))
    userdb = firebaseProcess.db.child("users").get()
    for i in userdb.each():
        print(i.val())
        print(i.key())
        if (i.val()["name"] == name):
            key = i.key()
    
    if update_field.lower() == "Name".lower():
        name_change = str(input("Enter new name: "))
        firebaseProcess.db.child("users").child(key).update({"name":name_change})
    
    elif update_field.lower() == "Age".lower():
        age_change = int(input("Enter new age: "))
        firebaseProcess.db.child("users").child(key).update({"age": age_change})
    
    elif update_field.lower() == "Major".lower():
        major_change = str(input("Enter new major: "))
        firebaseProcess.db.child("users").child(key).update({"major": major_change})

def fbGetUser():
    name = str(input("Enter existing user name: "))
    userdb = firebaseProcess.db.child("users").get()
    for i in userdb.each():
        if (i.val()["name"] == name):
            key = i.key()
    user_info = firebaseProcess.db.child("users").child(key).get()

    for i in user_info.each():
        print(i.val())