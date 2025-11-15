def check(number):
    if number % 2 == 0:
        return "The number is even."
    else:                                 #the first function which evaluates whether the number is even or odd is defined.
        return "The number is odd."       #a simple if statement is used where if the number's remainder is 0 when divided by 2, it is an even number, otherwise it is an odd number.
    
def ask():
    num = int(input("Please enter a number: ")) 
    message = check(num)             #first, the user's input is taken, then the message variable calls the first function and asks it to evaluate the user's input and return the corressponding message, and finally, the print function prints the final statement.
    print(message)   

ask()    