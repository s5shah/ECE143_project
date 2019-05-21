from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import bs4

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

def scrape_gva(data):
    '''
    Input :-
    data - type: str, len: 1, allowed characters: ['m', 'o']
    
    if data == m:
        scrape the mass shootings data.
    elif data == o:
        scrape the officers killing data.
    
    Output :-
    Mass_Shootings_{year}.csv / Officers_Shootings_{year}.csv file containing: Incident Date, State, City/County, #killed, #injured
    
    The function takes in a year as input and returns a csv file that contains the above mentioned data from
    "www.gunviolencearchive.org" website.
    The data is specific to either mass shootings or shootings involving police officers throughout United States.
    
    To run this program, you need the following:
        1. selenium package to be installed.
        2. google chrome installed
        3. chromedriver path added to path variables.
    '''
    assert isinstance(data, str)
    assert len(data) == 1
    assert data in ['m', 'o']
    
    for year in range(2014,2020):
        if data == 'm':
            url = f"https://www.gunviolencearchive.org/reports/mass-shooting?year={year}"
            fname = f"Mass_Shootings_{year}.csv"
        elif data == 'o':
            url = f"https://www.gunviolencearchive.org/reports/officer-shot-killed?year={year}"
            fname = f"Officers_Shootings_{year}.csv"
        
        driver = webdriver.Chrome(options = chrome_options)
        driver.get(url)
    
        stuff = []
        while True:
            #Scrape here    
            soup = BeautifulSoup(driver.page_source)
            scrollable = soup.find('table', {'class':"sticky-enabled tableheader-processed sticky-table"})
            links = scrollable.findAll('td')
            for link in links:
                if (type(link.contents[0]) == bs4.element.NavigableString):
                    stuff.append(link.contents[0])
            #Scraping done
            try:
                element = driver.find_element_by_partial_link_text('next')
                element.click()
            except NoSuchElementException:
                break
        driver.close()
        
        #Stuff ready here. Write to CSV after using pandas
        df = pd.DataFrame(np.array(stuff).reshape(int((len(stuff))/6), 6), columns = ['Incident Date', 'State', 'City/County', 'Address', '# killed', '# injured'])
        df.to_csv(fname, encoding='utf-8', index=False)