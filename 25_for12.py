'''
    1
   0 1
  1 0 1
 0 1 0 1
1 0 1 0 1
'''
num=int(input("Enter number of rows:"))
for row in range(1,num+1):
    for col in range(num-row):
        print(" ",end='')
    for col in range(0,row):
        if (((num-row)+col)%2==0):
            print("1",end=' ')
        else:
            print("0",end=' ')
    print( )
            
