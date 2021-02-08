word =str(input("Enter the word :"))
   
print("The original string is : "+word) 
  
res = [idx for idx, ele in enumerate(word) if ele in "aeiou"] 
  
print("The vowel indices are : " + str(res))  