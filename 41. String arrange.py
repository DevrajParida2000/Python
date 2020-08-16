def sortedSentence(Sentence): 
    words = Sentence.split(" ") 
    words.sort() 
    newSentence = " ".join(words) 
    return newSentence 
Sentence=input("Enter your Sentence: ")
print(sortedSentence(Sentence)) 
