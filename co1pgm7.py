lst1 = [1,2,7,4,8] 
lst2 = [1, 7, 2, 3, 5]
print ("The first list is : "+ str(lst1)) 
print ("The second list is : "+ str(lst2)) 

print("how many value occur in both?")
def Intersection(lst1, lst2): 
    return set(lst1).intersection(lst2) 
print(Intersection(lst1, lst2)) 
if len(lst1) == len(lst2): 
    print ("Length of the lists are same") 
else : 
    print ("Length of the lists are  not same")
    
