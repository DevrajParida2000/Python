num =int(input("Enter a number: "))
if num < 0:
   print("Enter a +ve number")
else:
   sum = 0
   while(num > 0):
       sum += num
       num -= 1
   print("The sum = ", sum)
   