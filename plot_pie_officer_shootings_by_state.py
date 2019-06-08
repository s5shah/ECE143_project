import plotly
plotly.tools.set_credentials_file(username='s5shah', api_key='fPDjLEIsOUDGl0OTewZG')
import plotly.plotly as py
from gundata import gundata
import pandas as pd
import operator

years = ['2014', '2015', '2016', '2017', '2018']
Officers_Shootings = list()
for i in years:
    Officers_Shootings.append(gundata(pd.read_csv(f"Officers_Shootings_{i}.csv"), 'Officers_Shootings'))
    
data = list()
domain = [
    {
        'x': [0, 0.3],
        'y': [0.6, 1]
    },
    {
        'x': [0.333, 0.633],
        'y': [0.6, 1]
    },
    {
        'x': [0.666, 0.966],
        'y': [0.6, 1]
    },
    {
        'x': [0.1665, 0.4665],
        'y': [0.1, 0.5]
    },
    {
        'x': [0.4995, 0.7995],
        'y': [0.1, 0.5]
    }
]
os_list_dicts = list()
for i in range(len(Officers_Shootings)):
    os_list_dicts.append(Officers_Shootings[i].count_by_columns("State"))

for i in range(len(os_list_dicts)):
    temp = dict()
    temp_sorted = dict(sorted(os_list_dicts[i].items(), key = operator.itemgetter(1), reverse = True))
    total = sum(temp_sorted.values())
    to_plot = dict()
    for j in list(temp_sorted)[0:5]:
        to_plot[j] = temp_sorted[j]
    to_plot["Others"] = total - sum(to_plot.values())
    temp['labels'] = list(to_plot.keys())
    temp['values'] = list(to_plot.values())
    temp['type'] = 'pie'
    temp['hoverinfo'] = 'label+value'
    temp['direction'] = 'clockwise'
    temp['sort'] = False
    temp['domain'] = domain[i]
    temp['name'] = f"{years[i]}"
    data.append(temp)

layout = dict()
layout['title'] = {
        'font': {
            'size': 30
        },
        'text': "Distribution of Officer Shootings that occurred over time"
}

layout['showlegend'] = True
layout['height'] = 800
layout['width'] = 900
layout['autosize'] = False
layout['annotations'] = [
    {
        'font': {
            'size': 15
        },
        'showarrow': False,
        'text': '2014',
        'x': 0.125,
        'y': 0.575
    },
    {
        'font': {
            'size': 15
        },
        'showarrow': False,
        'text': '2015',
        'x': 0.483,
        'y': 0.575
    },
    {
        'font': {
            'size': 15
        },
        'showarrow': False,
        'text': '2016',
        'x': 0.846,
        'y': 0.575
    },
    {
        'font': {
            'size': 15
        },
        'showarrow': False,
        'text': '2017',
        'x': 0.29,
        'y': 0.05
    },
    {
        'font': {
            'size': 15
        },
        'showarrow': False,
        'text': '2018',
        'x': 0.6495,
        'y': 0.05
    }
]

fig = dict()
fig['data'] = data
fig['layout'] = layout

py.iplot(fig, filename='statewise_distribution')