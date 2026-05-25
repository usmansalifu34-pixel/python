print("Welcome to our BMI calculation program")
name = input("Enter your name: ")
decision = input(f"Hello {name}, do you want to calculate your BMI? (yes/no): ")
while (decision.lower() == "yes"):
    print(f"Well, {name} BMI means body mass index and is use to determine if one is obese, underweight or average\n")
    system = input("Please enter the measurement system you make use of(metric or imperial): ")
    if (system.lower() == "metric"):
        weight = float(input("Enter your weight in KG: "))
        height = float(input("Enter your height in meters: "))
        BMI = weight/(height * height)
        if (BMI < 18.5):
            print(f"{name}, your BMI is {BMI:.2f}.This means you are underweight and we highly suggest you improve your eating habits")
        elif (BMI>= 18.5 and BMI < 25):
            print(f"{name}, your BMI is {BMI:.2f}.This means you are average and we suggest you maintain your eating habits")
        elif (BMI >= 25 and BMI < 30):
            print(f"{name}, your BMI is {BMI:.2f}.This means you are overweight and we suggest you improve your eating habits")
        else:
            print(f"{name}, your BMI is {BMI:.2f}.This means you are obese and we highly suggest you improve your eating habits")
    elif (system.lower() == "imperial"):
        weight = float(input("Enter your weight in pounds: "))
        height = float(input("Enter your height in inches: "))
        BMI = (weight/(height * height)) * 703
        if (BMI < 18.5):
            print(f"{name}, your BMI is {BMI:.2f}.This means you are underweight and we highly suggest you improve your eating habits")
        elif (BMI>= 18.5 and BMI < 25):
            print(f"{name}, your BMI is {BMI:.2f}.This means you are average and we suggest you maintain your eating habits")
        elif (BMI >= 25 and BMI < 30):
            print(f"{name}, your BMI is {BMI:.2f}.This means you are overweight and we suggest you improve your eating habits")
        else:
            print(f"{name}, your BMI is {BMI:.2f}.This means you are obese and we highly suggest you improve your eating habits")
    else:
        print("Invalid measurement system. Please enter either 'metric' or 'imperial'.")
    decision = input("Do you want to calculate your BMI again? (yes/no): ")
print(f"Thank you for using our BMI calculation program, {name}. Have a great day!")