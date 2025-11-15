password = "12345" #the correct password is set.

userinput = str(input("Please enter your password: ")) #asks the user for the password.

while userinput != password: #everytime the user enters a value that is not the correct password, display the error message stated below.
    userinput = str(input("Incorrect, please try again: "))

print("Access granted.") #displayed once the user enters the correct password.
    
