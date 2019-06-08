import matplotlib.pyplot as plt
from gundata import gundata
import pandas as pd

years = ['2014', '2015', '2016', '2017', '2018']
Mass_Shootings = list()
for i in years:
    Mass_Shootings.append(gundata(pd.read_csv(f"Mass_Shootings_{i}.csv"), 'Mass_Shootings'))
    
no_casualties_ms = list()
for i in range(len(Mass_Shootings)):
    no_casualties_ms.append(Mass_Shootings[i].count_casualties())

plt.bar(years, no_casualties_ms, label = "Casualties of Mass Shootings throughout United States", width = 0.6, color = 'xkcd:blood red')
labels = list()
for i in range(len(Mass_Shootings)):
    labels.append(str(no_casualties_ms[i]))
for i in range(len(Mass_Shootings)):
    plt.text(x = years[i] , y = no_casualties_ms[i] + 25, s = labels[i], size = 10, horizontalalignment='center')

plt.ylim(800, 2500)
plt.xlabel("Years", fontsize = 12)
plt.ylabel("Casualties", fontsize = 12)
plt.title("Casualties of Mass Shootings throughout United States\n", fontsize = 15)
plt.show()