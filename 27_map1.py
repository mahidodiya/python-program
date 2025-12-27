'''use map function to findout binary of each number in list [10,20,40,80,100]'''
    
numbers=[10,20,40,80,100]

def tobinary(n):
    b=""
    while n>0:
        b=str(n%2)+b
        n=n//2
    return b

result=list(map(tobinary,numbers))
print(result)