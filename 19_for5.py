# nested list
delhi_aqi = [
    [330, 270, 290, 320, 275, 410, 380],  # Week 1
    [260, 305, 330, 285, 410, 395, 370],  # Week 2
    [420, 385, 440, 310, 295, 260, 355],  # Week 3
    [280, 360, 340, 455, 380, 410, 290],   # Week 4
    [300,400],   # Week 5
]
# findout average aqi
count = 0
total = 0 
for week in delhi_aqi: #outer for loop
    #print(week)
    for item in week:
        #print(item)
        total = total + item 
        count = count + 1
    
#average calculate 
average = total / count 
print(f"total = {total} count = {count} average = {average}")

#display days less then average aqi and also count it 
less_then_average_count = 0
for week in delhi_aqi:
    for item in week:
        if item<average:
            #print(item)
            less_then_average_count= less_then_average_count + 1

print(f"total no days where aqi is less then average = {less_then_average_count}")

#findout minimum and maximum aqi 
max=0
for ele in delhi_aqi:
    for i in ele:
        if i>max:
            max=i
print("Maximum aqi:",max) 

min=delhi_aqi[0][0]
#print(min)
for ele_2 in delhi_aqi:
   for j in ele_2:
         if j<min:
             min=j
print("Minimum aqi:",min) 

#average of week
total_avg=0
avg_week=0
count_avg=0
avg_list=[]
for week_avg in delhi_aqi:
    total_avg=0
    count_avg=0
    for k in week_avg:
        total_avg+=k
        count_avg+=1
    #print("Total by each week:",total_avg)
    #print("Count",count_avg)
    avg_week=total_avg/count_avg
    #print("Average",avg_week)
    avg_list.append(avg_week)
print(f'average by sublist : {avg_list}')

                   
#findout week whose average is least  other week average
least=avg_list[0]
for o in avg_list:
    if o<least:
        least=o
print("Least avg:",least)
    
#findout week whose average is maximum  other week average
maximum=0
for p in avg_list:
    if p>maximum:
        maximum=p
print("Maximum avg:",maximum)
    