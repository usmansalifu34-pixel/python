print("Welcome to the voting system!")
age = int(input("Please enter your age: "))
isCitizen = input("are you a citizen of this country?(yes or no): ")
isCitizen = isCitizen.lower()
if age < 0:
    print("You haven't been born yet!!")
elif age < 18:
    print("you are not eligible to vote in this election.") 
else:
    if isCitizen == "yes":
        print("you are eligible to vote.")
    elif isCitizen == "no":
        print("you must be a citizen of this country to be eligible to vote")
    else:
        print("please enter yes or no.")

