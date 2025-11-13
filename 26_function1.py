'''
 create function that has arbitary arguments of string type and it display all strings into lower case.
toLowerCase('Apple','bAnana','ManGO','KIWI','graps')
output 
    apple banana mango kiwi graps

'''
def to_lowercase(*list1):
    for word in list1:
        print(word.lower(),end=' ')
        
    

list1=to_lowercase('Apple','bAnana','ManGO','KIWI','graps')
print(list1)
