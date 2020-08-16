def hcf_of_2_num(x, y):
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i 
    return hcf
num1 =int(input("Enter the 1st number: ")) 
num2 =int(input("Enter the 2nd number: "))
print("The H.C.F. is", hcf_of_2_num(num1, num2))
