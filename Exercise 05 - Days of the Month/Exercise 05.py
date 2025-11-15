months = {  #create a dictionary with the keys as the months, and the values as the number of days in that month.
    1 : 31,
    2 : 28,
    3 : 31,
    4 : 30,
    5 : 31,
    6 : 30,
    7 : 31,
    8 : 31,
    9 : 30,
    10 : 31,
    11 : 30,
    12 : 31
}

ask = int(input("Please input the number of the month you require: ")) #asks the user for their month.

if ask in months: #first if statement, if the user's input is in months,
    if ask == 2:  #second if statement, if the user's input is the second month, i.e February, 
        leap = (input("Is it a leap year? ")).lower() #ask the user if that February is a part of a leap year
        if leap == "Yes": #third if statement, if it is a leap year, print the following statement, otherwise print that the 2nd month has the amount of days as stated in the dictionary.
            print("Your month has 29 days.") 
        else:
            print(f"Your month has {months[ask]} days")
    else:
        print(f"Your month has {months[ask]} days") #second if statement, if the user has not input the 2nd month, display the amount of days from the month input by the user. 
else:
    print("Please enter a valid month number.") #first if statement, when the user inputs an invalid month number that is not in the dictionary.        
