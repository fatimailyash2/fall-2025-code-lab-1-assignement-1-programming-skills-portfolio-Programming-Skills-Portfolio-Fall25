question = str(input("What is the capital of France? ")) #the user is supposed to answer this question by providing an input.

if question == "Paris": #if the user output equals to every variation of the word "Paris", the answer is correct and the output message will be provided.
    print("Correct!")
elif question == "paris":
    print("Correct!")  
elif question == "pAris":
    print("Correct!")
elif question == "paRis":
    print("Correct!")
elif question == "parIs":
    print("Correct!")
elif question == "pariS":
    print("Correct!")
elif question == "PARIS":
    print("Correct!")                      
else:
    print("Incorrect, the capital of France is Paris.") #otherwise, the output message for the wrong answer, which is anything apart from the variations of the word "Paris", will be provided.   

question1 = str(input("What is the capital of Italy?" )) #the user is asked another question, which they will provide an input for.  

if question1 in ["Rome","rome","ROME","rOme","roMe","romE"]: #this is another, easier way, which uses a list to look for possible answers.
    print("Correct!")
else:
    print("Incorrect, the capital of Italy is Rome.")    

question2 = str(input("What is the capital of Germany? "))    

if question2.lower() == "berlin":
    print("Correct!")
else:
    print("Incorrect, the capital of Germany is Berlin.")
