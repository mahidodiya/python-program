''' 
write a program to findout which is cheaper approach to buy IPhone 17 pro max.  consider use is going usa should he buy iphone from usa or from india.
 
'''
inr=int(input("Enter price at india:"))
usd=int(input("Enter price at usa:"))

amount=88.36
rate1=inr
print("in inr",rate1)
rate2= amount*usd 
print("usd into inr",rate2)

if (rate1<rate2):
    print("buy it from india,it is cheaper")
else:
    print("buy it from usa,it is cheaper")
     
