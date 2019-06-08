import matplotlib.pyplot as plt
from gundata import gundata
import pandas as pd

years = ['2014', '2015', '2016', '2017', '2018']

School_Shootings = list()
for i in years:
    School_Shootings.append(gundata(pd.read_csv(f"School_Shootings_{i}.csv"), 'School_Shootings'))

list_of_dicts = list()
for i in range(len(School_Shootings)):
    list_of_dicts.append(School_Shootings[i].count_by_columns("School Type"))

hs_killings = list()
cu_killings = list()
for i in range(len(list_of_dicts)):
    hs_killings.append(list_of_dicts[i]['High School'])
    cu_killings.append(list_of_dicts[i]['College or University'])

plt.plot(years, hs_killings, cu_killings, label = "Number of High School and College or University Shootings over the years", marker = "o", markersize = 8, linewidth = 2.5)
plt.ylim(0,60)
plt.xlabel("Years", fontsize = 12)
plt.ylabel("Number of Shootings", fontsize = 12)
plt.title("Number of High School and \nCollege or University Shootings over the years\n", fontsize = 15)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.legend(['High School', 'College or University'], loc = 'best')
plt.show()    