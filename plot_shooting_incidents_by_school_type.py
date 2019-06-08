'''
This script generates a plot the shows the number of gun violence incidents throughout different types of schools such as 
High Schools, College / University, Middle School, etc.
Before running this script, you need the data sets, which can either be scraped using the web crawler tool provided or
from https://drive.google.com/open?id=1Nj4TVz5X7tNc0DFDhLBgOsNAjVuuhSqY
'''

import matplotlib.pyplot as plt
from gundata import gundata
import pandas as pd
from collections import Counter
import operator
import collections

years = ['2014', '2015', '2016', '2017', '2018']
School_Shootings = list()
for i in years:
    School_Shootings.append(gundata(pd.read_csv(f"School_Shootings_{i}.csv"), 'School_Shootings'))
    
list_of_dicts = list()
for i in range(len(School_Shootings)):
    list_of_dicts.append(School_Shootings[i].count_by_columns("School Type"))
temp = Counter()
for i in range(len(list_of_dicts)):
    temp += Counter(list_of_dicts[i])
final_counts = dict(temp)
sorted_count = sorted(final_counts.items(), key=operator.itemgetter(1))
sorted_final_counts = collections.OrderedDict(sorted_count)
plt.barh(list(sorted_final_counts.keys()), list(sorted_final_counts.values()), height = 0.6)
labels = list()
list_counts = list(sorted_final_counts.values())
list_types = list(sorted_final_counts.keys())
for i in range(len(list_counts)):
    labels.append(str(list_counts[i]))
for i in range(len(list_counts)):
    plt.text(x = list_counts[i]+5 , y = list_types[i], s = labels[i], size = 10, horizontalalignment='center')
    
plt.xlim(0,160)
plt.xlabel("Number of Shootings", fontsize = 12)
plt.title("Number of Shootings at \ndifferent types of Schools throughout United States\n", fontsize = 15)
plt.show()