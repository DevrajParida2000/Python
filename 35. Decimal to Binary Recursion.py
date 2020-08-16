def ToBinary(num):
   if num > 1:
       ToBinary(num//2)
   print(num % 2,end = '')
dec = int(input("Enter the decimal number: "))
ToBinary(dec)
print()
