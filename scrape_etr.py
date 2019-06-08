from selenium import webdriver
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import bs4

def scrape_etr():
    '''
    Output :-
    School_Shootings_{year}.csv file containing: Date, City, State, School Name, School Type
    
    The function generates csv files for different years, from 2013 till date, that contains the above mentioned data from
    "www.everytownresearch.org" website.
    The data is specific to gun violence incidents in schools throughout United States.
    
    To run this program, you need the following:
        1. selenium package to be installed.
        2. google chrome installed
        3. chromedriver path added to path variables.
    '''
    driver = webdriver.Chrome()
    driver.get("https://everytownresearch.org/gunfire-in-school/")
    
    #Scrape here
    stuff = []
    soup = BeautifulSoup(driver.page_source)
    table = soup.find('table', {'class': 'row-border stripe dataTable no-footer'})
    links = table.findAll('td')
    
    for link in links:
        if type(link.contents[0]) == bs4.element.NavigableString:
            stuff.append(link.contents[0])
    #Scraping 
    driver.close()
    #Create data frame from stuff that was collected
    df = pd.DataFrame(np.array(stuff).reshape(int((len(stuff))/5), 5), columns = ['Date', 'City', 'State', 'School Name', 'School Type'])
    
    #Generate an extra column called years to make groups
    df['Year'] = 0
    for i in range(len(df['Date'])):
        df['Year'][i] = df['Date'][i][-4:]
    
    #Generate a grouped dataframe and write the groups to their respective csv files    
    df_grouped = df.groupby('Year')
    for i in range(2014, 2019):
        df_grouped.get_group(i).to_csv(f'School_Schootings_{i}.csv', encoding='utf-8', index=False, columns = ['Date', 'City', 'State', 'School Name', 'School Type'])
        
scrape_etr()