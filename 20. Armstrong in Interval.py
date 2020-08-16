start =int(input("Enter the starting number: "))
end =int(input("Enter the ending number: "))

for num in range(start, end + 1):

   order = len(str(num))

   sum = 0

   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)