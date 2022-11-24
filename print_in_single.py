# s = input("Enter Two Number: ")
# print(s) # '10 20 '
# l = s.split() #['10' , '20']
# print(l)
# l1 = [int(x) for x in l] # [10,20]
# a,b = l1
# print(a)
# print(b)
# print("The Sum: ", a + b)

a,b,c = [float(x) for x in input("Enter 3 Values With , Separeastion: ").split(",")]
print("The Sum: ", a + b + c)