'''create function getSeconds which has hours, minutes and seconds which return total seconds
steps:(hr,min,sec)

'''
def getsecond(hr,min,sec):
    total= (hr*3600)+(min*60)+(sec*1) 
    return total

hr=int(input("Enter hours:"))
min=int(input("Enter minutes:"))
sec=int(input("Enter seconds:"))

      
time=getsecond(hr,min,sec)
print(time)