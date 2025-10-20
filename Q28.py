word=input("Enter a string/word:")
l=word.lower()


vowel=0
consonant=0

for i in l:
    if(i=='a' or  i=="e" or i=="i" or i=='o' or i=='u'):
        vowel+=1
    else:
        consonant+=1
print(f"Total numbers of vowels and consonant are : {vowel} , {consonant}")