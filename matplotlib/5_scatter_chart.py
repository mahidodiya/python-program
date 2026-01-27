#create scatter chart to display car sales in lakhs in india along with gdp rates between 2000 to 2025
import matplotlib.pyplot as plt
# Years for the X-axis
years = [
    "2000-01", "2005-06", "2010-11", "2015-16", 
    "2018-19", "2019-20", "2020-21", "2021-22", 
    "2022-23", "2023-24", "2024-25", "2025-26"
]

# Passenger Vehicle Sales (in Lakhs)
car_sales_lakhs = [
    6.50, 11.43, 25.01, 27.89, 
    33.77, 27.73, 27.11, 30.69, 
    38.90, 42.19, 43.02, 45.30
]

tw_sales_lakhs = [
    37.5, 70.5, 117.7, 164.5, 
    211.8, 174.1, 151.2, 135.7, 
    158.6, 179.7, 196.1, 205.0
]

# Annual GDP Growth Rate (as percentages)
gdp_growth_rate = [
    3.8, 7.9, 8.5, 8.0, 
    6.5, 3.9, -5.8, 9.7, 
    7.0, 8.2, 6.5, 7.8
]
plt.figure(figsize=(12,6))
plt.scatter(years,car_sales_lakhs,s=70,color='red',marker='o',label='car sales')
plt.plot(years,gdp_growth_rate,marker='^',markersize=7,markerfacecolor='blue',label='GDP Growth Rate')
plt.scatter(years,tw_sales_lakhs,s=70,color='yellow',marker='o',label='tw sales')
plt.xlabel('years')
plt.legend()
plt.xticks(years,rotation=60,ha='right',fontsize=9)
plt.ylabel('growth rate')
plt.title('Vehicle sales with gdp rates')
plt.grid(True,which='both')

plt.show()