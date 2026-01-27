#create chart to display no of ODI PLAYED in each year in mans cricket between year 2000 to 2025
import matplotlib.pyplot as plt

years=list(range(2000,2026))
odis_per_year = [131,120,145,147,128,107,160,191,126,53,
    140,150,155,160,165,170,175,180,185,
    218,104,115,110,108,102,99]

plt.figure(figsize=(12,6))

plt.plot(years,odis_per_year,marker='o',markersize=6,markerfacecolor='red',markeredgecolor='black')

plt.title("ODI PLAYED in each year in mans cricket between year 2000 to 2025")
plt.xlabel("years")
plt.ylabel("odis per year")
plt.xticks(years,rotation=60,ha='right',fontsize=9)

plt.grid(True,which='both')
plt.tight_layout()

plt.show()