#write a program to accept weight from user in kg. calculate BMI(body to mass index) and display it. handle all built in exception
try:   
    weight=float(input("Enter your weight(in kg):"))
    height=float(input("Enter your height(in m):"))
    bmi=weight/(height*height)
    print("BMI=",bmi)
    if bmi<18.5:
            print("Underweight")
    elif 18.5<= bmi <=24.9:
            print("Normal weight")
    elif 25<= bmi <=29.9:
            print("Overweight")
    elif bmi>=30:
            print("Obese")
except ValueError:
    print("Invalid value ,Enter integer value!!")
except ZeroDivisionError:
    print("Number does not divied by zero!!")
except Exception as e:
    print("Someting went wrong",e)   