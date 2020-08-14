start=int(input("Enter the start value: ")) 
end=int(input("Enter the end value: "))
  
for num in range(start, end + 1): 
    if num > 1: 
        for n in range(2, num//2 + 2): 
            if (num % n) == 0: 
                break
            else: 
                if n == num//2 + 1: 
                    print(num) 