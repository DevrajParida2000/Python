def recurSum(n): 
    if n <= 1: 
        return n 
    return n + recurSum(n - 1) 
num =int(input("Enter the number: "))
print("The sum of the first",num, "numbers is",recurSum(num))