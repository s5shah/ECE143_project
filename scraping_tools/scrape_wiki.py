from selenium import webdriver
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import bs4

def scrape_wiki():
    '''
    School_Shootings_Casualties_{year}.csv file containing: Date, Location, Deaths, Injured
    
    The function generates csv files for different years, from 2013 till date, that contains the above mentioned data from
    "en.wikipedia.org" website.
    The data is specific to gun violence incidents in schools throughout United States.
    
    To run this program, you need the following:
        1. selenium package to be installed.
        2. google chrome installed
        3. chromedriver path added to path variables.
    '''
    driver = webdriver.Chrome()
    driver.get("https://en.wikipedia.org/wiki/List_of_school_shootings_in_the_United_States")
    
    #Start scraping
    stuff = []
    soup = BeautifulSoup(driver.page_source)
    tables = soup.find_all('table', {'class': 'sortable wikitable jquery-tablesorter'})
    
    for table in tables: 
        links = table.find_all('td')
        for link in links:
            if type(link.contents[0]) == bs4.element.NavigableString:
                stuff.append(link.contents[0])
            if type(link.contents[0]) == bs4.element.Tag:
                if link.contents[0].get('title') != None:
                    stuff.append(link.contents[0].get('title'))
                else:
                    stuff.append(link.contents[0].text)
    #Scraping done
    driver.close()
    #Stuff ready here, modify it as required and generate a pandas dataframe
    new_stuff = []
    for i in range(len(stuff)):
        if (i+1) % 5 != 0:
            new_stuff.append(stuff[i])
            
    for i in range(len(new_stuff)):
        new_stuff[i] = new_stuff[i].rstrip()
        
    df = pd.DataFrame(np.array(new_stuff).reshape(int((len(new_stuff))/4), 4), columns = ['Date', 'Location', 'Deaths', 'Injuries'])
    
    for i in range(len(df['Deaths'])):
        df['Deaths'][i] = ''.join(j for j in df['Deaths'][i] if j.isdigit())
        
    for i in range(len(df['Injuries'])):
        df['Injuries'][i] = ''.join(j for j in df['Injuries'][i] if j.isdigit())
        
    for i in range(len(df['Date'])):
        if(int(df['Date'][i][-4:]) < 2013):
            df = df.drop(i, axis=0)
            
    df = df.reset_index()
    df['Deaths'] = df['Deaths'].astype(int)
    df['Injuries'] = df['Injuries'].astype(int)
    
    df['Year'] = 0
    for i in range(len(df['Date'])):
        df['Year'][i] = df['Date'][i][-4:]
    
    df_grouped = df.groupby('Year')
    for i in df_grouped.indices:
        df_grouped.get_group(i).to_csv(f'School_Schootings_Casualties_{i}.csv', encoding='utf-8', index=False, columns = ['Date', 'Location', 'Deaths', 'Injuries'])    