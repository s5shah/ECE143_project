import matplotlib.pyplot as plt
from gundata import gundata
import pandas as pd

years = ['2014', '2015', '2016', '2017', '2018']
School_Shootings = list()
for i in years:
    School_Shootings.append(gundata(pd.read_csv(f"School_Shootings_{i}.csv"), 'School_Shootings'))
    
no_incidents_ss = list()
for i in range(len(School_Shootings)):
    no_incidents_ss.append(School_Shootings[i].get_total_incidents())

plt.bar(years, no_incidents_ss, label = "Number of School Shootings throughout United States", width = 0.6)
labels = list()
for i in range(len(School_Shootings)):
    labels.append(str(no_incidents_ss[i]))
for i in range(len(School_Shootings)):
    plt.text(x = years[i] , y = no_incidents_ss[i] + 1, s = labels[i], size = 10, horizontalalignment='center')
    
plt.ylim(20, 120)
plt.xlabel("Years", fontsize = 12)
plt.ylabel("Number of School Shootings", fontsize = 12)
plt.title("Number of School Shootings throughout United States\n", fontsize = 15)
plt.show()