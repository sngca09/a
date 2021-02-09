lst1 = [1,2,7,4,8] 
lst2 = [1, 7, 2, 3, 5]
s=int(0)
c=int(0)

print ("The first list is : "+ str(lst1)) 
print ("The second list is : "+ str(lst2)) 

print("how many value occur in both?")#7c
def Intersection(lst1, lst2): 
    return set(lst1).intersection(lst2) 
print(Intersection(lst1, lst2)) 
if len(lst1) == len(lst2): #7a
    print ("Length of the lists are same") 
else : 
    print ("Length of the lists are  not same")
    
for i in range(0,len(lst1) and len(lst2)):#7b
    s=s+lst1[i]
    c=c+lst2[i]
    
for i in range(0, len(lst1) and len(lst2)):
    if s==c:
        print("Sum of values are same")
        break
    else:
        print("Sum of values are different")
        break
