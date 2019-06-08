import matplotlib.pyplot as plt
from gundata import gundata
import pandas as pd

years = ['2014', '2015', '2016', '2017', '2018']
Mass_Shootings = list()
for i in years:
    Mass_Shootings.append(gundata(pd.read_csv(f"Mass_Shootings_{i}.csv"), 'Mass_Shootings'))
    
no_incidents_ms = list()
for i in range(len(Mass_Shootings)):
    no_incidents_ms.append(Mass_Shootings[i].get_total_incidents())
    
no_casualties_ms = list()
for i in range(len(Mass_Shootings)):
    no_casualties_ms.append(Mass_Shootings[i].count_casualties())
    
casualties_incidents_ratio_ms = list()
for i in range(len(no_casualties_ms)):
    casualties_incidents_ratio_ms.append(no_casualties_ms[i] / no_incidents_ms[i])

plt.plot(years, casualties_incidents_ratio_ms, label = "Average number of casualties per incident of Mass Shootings", marker = "o", markersize = 8, color = 'xkcd:blue', linewidth = 2.5)
plt.ylim(4,7)
plt.xlabel("Years", fontsize = 12)
plt.ylabel("Average Casualties per Incident", fontsize = 12)
plt.title("Average Number of Casualties per Incident of Mass Shootings\n", fontsize = 15)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.show()