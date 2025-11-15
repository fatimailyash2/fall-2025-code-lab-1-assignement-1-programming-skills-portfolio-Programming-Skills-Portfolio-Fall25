names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"] #a list of strings.

ask = str(input("Who are you searching for? ")) #asks the user for an input from the list of names.

if ask in names: #if the user input is in the list, print the statement showing that the value exists in the list, otherwise if the user enters another name that does not exist in the list, display the following message.
    print(f"{ask} found!")
else:
    print(f"{ask} does not exist in this list.")   
