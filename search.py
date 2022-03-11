import sys

if(len(sys.argv) > 1):
    text = sys.argv[1]
else:
    text = "corncob_lowercase.txt"
    
print(text)
file = open(text, "r")

def validWord(word, letters):
    for l in word:
        if(not l in letters):
            
            return False
    if(not letters[-1] in word):
   
        return False
    return True



arr = [x[:-1] for x in file.readlines() if len(x[:-1])>=4] # clean newline and check if word is greater than 4

letters = input("letters (put special last):")
while(not len(letters) == 7):
    print("Should be 7 letters")
    letters = input("letters (put special last):")

final=[]

for word in arr:
    if validWord(word, letters):
        final.append(word)
        
print(final)

