value={'anu':9,'alan':21,'alice':111,'rose':3} 
                                       
lst=list(value.items()) 
print('original is :\n',lst)  

lst.sort()
print('Ascending order is :\n',lst)  

lst=list(value.items())
lst.sort(reverse=True)
print('Descending order is : \n',lst)

dict=dict(lst)
print("Dictionary :\n",dict) 