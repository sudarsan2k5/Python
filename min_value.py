# Read two int values from kyeboard and print the MIN value 
num1 = int(input("Enter Your First Num: "))
num2 = int(input("Enter Your Second Num: "))

min = num1 if num1 < num2 else num2    # Ternary Operator
print("The Min Value is: ", min)