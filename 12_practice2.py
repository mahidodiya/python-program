'''
Restaurant Discount System

Input total bill amount and payment method ("cash", "card", or "UPI").
Rules:

If bill > ₹1000 → 20% discount

If bill > ₹500 → 10% discount

Else → no discount
Then:

If payment is UPI → extra 5% off
Show total payable amount.
'''
bill=float(input("Enter total bill:"))

payment=input("Choose payment method cash , card , UPI:")

if bill>=1000:
    if payment.lower()=='upi':
       discount=bill*25/100
    else:
        discount=bill*20/100
        
    total_bill=bill-discount
    print(f'bill {bill} \ntotal bill after discount {total_bill}')
    
elif bill>=500:
    if payment.lower()=='upi':
        discount=bill*15/100
    else:
        discount=bill*10/100
    total_bill=bill-discount
    print(f'bill {bill} \ntotal bill after discount {total_bill}')

else:
    if payment.lower()=='upi':
        discount=bill*5/100
        total_bill=bill-discount
        print(f'bill {bill} \ntotal bill after 5% discount {total_bill}')
    else:
        print(f'total bill with no discount {bill}')

    