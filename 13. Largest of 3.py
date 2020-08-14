num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))
num3 = float(input("Enter 3rd number: "))
lnum=0
if (num1 >= num2) and (num1 >= num3):
   lnum = num1
elif (num2 >= num1) and (num2 >= num3):
   lnum = num2
else:
   lnum = num3

print("The largest number is ",lnum)
