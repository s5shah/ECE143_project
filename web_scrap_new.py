# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 23:11:33 2019

@author: linli
"""

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import bs4
import chardet
import csv

years = ['2014','2015','2016','2017','2018']
page_limit = 17
with open('project.csv','w',newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Date','State','City(Country)','Address','killed','injured'])
    for year in years:
        count = 0
        print(year, ' scrapping')
        while count <= page_limit:
            page = str(count)+'&'     
            url = 'https://www.gunviolencearchive.org/reports/total-number-of-incidents?{0}year={1}'.format(page,year)
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            web_byte = urlopen(req).read()
            # detect the encoding of the website
            charset = chardet.detect(web_byte)
            webpage = web_byte.decode(charset['encoding'])
            soup = BeautifulSoup(webpage, 'html.parser')
    
            soup_children = soup.find(class_ = 'small-12 columns').children
            i = 1
            table = []
            for children in soup_children:
                if (isinstance(children, bs4.element.Tag)):
                    if i == 3:
                        tmp = children.find_all('tr', class_ = ('even','odd'))
                        for content in tmp:
                            data = []
                            for idx,element in enumerate(content.contents):
                                if (isinstance(element, bs4.element.Tag)) and idx < 6:
                                    data.append(element.contents[0])
                            table.append(data)                        
                    i += 1
            count += 1
            writer.writerows(table)
print('done')