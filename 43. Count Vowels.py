def Check_Vow(string, vowels): 
    string = string.casefold() 
    count = {}.fromkeys(vowels, 0) 
    
    for character in string: 
        if character in count: 
            count[character] += 1    
    return count 
 
vowels = 'aeiou'
string = input("Enter your phrase: ")
print (Check_Vow(string, vowels))
