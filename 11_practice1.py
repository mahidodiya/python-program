'''
Electricity Bill Estimator
Write a program to calculate an electricity bill based on units consumed:

Up to 100 units → ₹5/unit
101–300 units → ₹8/unit
Above 300 → ₹10/unit

Add ₹50 fixed charge for all users.
Show total bill and category (“Low”, “Medium”, “High Usage”).

steps:
1.enter units
2.checks units & multiply with corrsponding rs.
3.disply low , medium , high
'''
units=float(input("Enter your current units:"))

if units<=100:
    total=(units*5)+50 #here 50 is fixed charge
    print(f"low usage with total bill {total}")

elif units>=101 and units<=300:
    total=(units*8)+50
    print(f"mediun usage with total bill {total}")
    
else:
    total=(units*10)+50
    print(f"high usage with total bill {total}")

    
