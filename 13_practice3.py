'''
designing a mini “fare calculator” for a ride-sharing app like Ola/Uber.

Rules:

Base fare depends on the ride type:
Mini → ₹50 + ₹10/km
Sedan → ₹80 + ₹15/km
SUV → ₹100 + ₹20/km

Surge pricing:
If time = peak → add 25 % extra to the total
If time = night → add 10 % extra
Else → no surge

Discounts by payment:
UPI → 5 % off
Card → 2 % off
Cash → no discount

Output must include:
Base fare
Surge amount
Discount amount
Final payable fare

steps:
1.enter ride type
2.time chek
3.discount by payment
4.final payment
'''
km=int(input("Enter km: "))
ride=(input("Choose your ride type (mini/sedan/suv) :"))
surge=(input("Current time (peak/night/noraml) :"))
pay=input("Choose your payment method (cash/card/upi) :")

#base fare logic
if ride.lower()=='mini':
    base=50+(km*10)
    print(f"Base fare: {base}")
elif ride.lower()=='sedan':
    base=80+(km*15)
    print(f"Base fare: {base}")
elif ride.lower()=='suv':
    base=100+(km*20)
    print(f"Base fare: {base}")
    
else:
    ("Ride note available")
    base=0
    print(f"Base fare: {base}")
    
    
#surge logic    
if surge.lower()=='peak':
    add=base*25/100
    print(f"25% extra for peak timing!: {add}")
elif surge.lower()=='night':
    add=base*10/100
    print(f"10% extra for night timing!: {add}")
else:
    add=0
    print("no extra charge!")
    
#payment logic
if pay.lower()=='upi':
    disc=base*5/100
    print(f"you get 5% discount: {disc}")
elif pay.lower=='card':
    disc=base*2/100
    print(f"you get 2% discount: {disc}")
else:
    disc=0
    print("not any discount available!")
 
#main logic   
final=(base+add)-disc
print(f'Final payable fare is : {final}')
    
    
    
    
