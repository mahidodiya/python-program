#create lambda function which return compound interest of given amount, rate, year 


compoud_interest=lambda p ,rate,t:p*((1+rate/100)**t-1)


p=float(input("Enter amount :"))
rate=float(input("Entar rate of intrest :"))
t=float(input("Enter period of time :"))

ci=compoud_interest(p,rate,t)
print(ci)
    