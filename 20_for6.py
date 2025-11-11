# display even number between 400 and 200 in reverse order
#400 398 396 394 ... 200
for number in range(400,199,-2):  #it means in each execution number will be incremented by 2  because 3 argument in range function is step value 
    print(number)
for j in range(100,200,2):
    print(f"even:{j}")
print("_"*100)
for k in range(101,303,2):
    print(f"odd:{k}")