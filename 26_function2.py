'''
create function that returns average of player score of all 11 players (arbitary arguments)
steps:(data,total,avg)
1.enter data
2.total,count
3.avg=total/count
'''

def getavg(*data):
    count=0
    total=0
    for i in data:
        total+=i
        count+=1
    avg=total/count
    return avg
    
res=getavg(1,2,3,4,5)
print(res)