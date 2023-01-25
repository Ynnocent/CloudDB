import firebasePythonCon

QUIT = False

while not QUIT:
    print("""
    ==========================
    Select your options:
       ->[Add Users]<-

      ->[Delete Users]<-
        
       ->[Get User]<-
       
      ->[Update User]<-
      
       ->[End]<-
    ==========================
    """)
    endUserInput = str(input("What would you like to do: "))

    if endUserInput.lower() == "Add Users".lower():
        firebasePythonCon.fbAddUser()

    elif endUserInput.lower() == "Delete Users".lower():
        firebasePythonCon.fbDelUser()

    elif endUserInput.lower() == "Get User".lower():
        firebasePythonCon.fbGetUser()
    
    elif endUserInput.lower() == "Update User".lower():
        firebasePythonCon.fbUpdateUser()

    elif endUserInput.lower() == "End".lower():
        print("===============")
        print("\nThank you for using the App")
        QUIT = True