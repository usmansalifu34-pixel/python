
print("Welcome to the height conversion program\n")
system = input("Choose a measurement system(imperial or metric): ")
if (system.lower() == "imperial"):
    height = float(input("\nEnter your height in feet or inches: "))
    subsystem = input("\nIs the inputted height in feet or inches: ")
    if (subsystem.lower() == "feet"):
        convertto = input("\nwhat do you want to convert your height to?(inches or centimetres or metres) ")
        if (convertto.lower() == "inches"):
            height = height * 12
            print(f"\nYour height when converted from {subsystem} to {convertto} is {height}inches\n")
        elif (convertto.lower() == "centimetres"):
            height = height * 30.48
            print(f"\nYour height when converted from {subsystem} to {convertto} is {height}cm\n")
        elif(convertto.lower() == "metres"):
            height = height * 0.3048
            print(f"\nYour height when converted from {subsystem} to {convertto} is {height}m\n")
    elif (subsystem.lower() == "inches"):
        convertto = input("\nwhat do you want to convert your height to?(feet or centimetres or metres) ")
        if (convertto.lower() == "feet"):
            height = height / 12
            print(f"\nYour height when converted from {subsystem} to {convertto} is {height}feet\n")
        elif (convertto.lower() == "centimetres"):
            height = height * 2.54
            print(f"\nYour height when converted from {subsystem} to {convertto} is {height}cm\n")
        elif(convertto.lower() == "metres"):
            height = height * 0.0254
            print(f"\nYour height when converted from {subsystem} to {convertto} is {height}m\n")
elif (system.lower() == "metric"):
    height = float(input("Enter your height in centimetres or metres: "))
    subsystem = input("is your height in centimetres or metres: ")
    if (subsystem.lower() == "centimetres"):
        convertto = input("\nwhat do you want to convert your height to?(feet or inches or metres) ")
        if (convertto == "feet"):
            height = height/ 30.48
            print(f"\nYour height when converted from {subsystem} to {convertto} is {height}m\n")
        elif( convertto.lower() == "inches"):
            height = height/2.54
            print(f"\nYour height when converted from {subsystem} to {convertto} is {height}m\n")
        elif(convertto.lower() == "metres"):
            height = height / 100
            print(f"\nYour height when converted from {subsystem} to {convertto} is {height}m\n")
    elif (subsystem.lower() == "metres"):
        convertto = input("\nwhat do you want to convert your height to?(feet or inches or centimetres) ")
        if (convertto.lower() == "feet"):
            height = height / 0.3048
            print(f"\nYour height when converted from {subsystem} to {convertto} is {height}feet\n")
        elif( convertto.lower() == "inches"):
            height = height / 0.0254
            print(f"\nYour height when converted from {subsystem} to {convertto} is {height}inches\n")
        elif(convertto.lower() == "centimetres"):
            height = height * 100
            print(f"\nYour height when converted from {subsystem} to {convertto} is {height}cm\n")
    else:
        print("\nInvalid metric measurement unit entered\n")
else:
    print("please enter a valid measurement system")
