'''
1
2 3
4 5 6
7 8 9 10
'''
num=1
for raw in range(1,6):
    for col in range(0,raw):
        print(num,end=' ')
        num+=1
    print(' ')