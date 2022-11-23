num1 = int(input("Enter Your First Num: "))
num2 = int(input("Enter Your Second Num: "))
num3 = int(input("Enter Your Third Num: "))

min = num1 if num1 < num2 and num1 < num3 else num2 if num2 < num3 else num3

print("The Min Value Is: ", min)