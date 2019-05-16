from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import bs4

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

def scrape_gva(year):
    '''
    Input :-
    year - type: int, range: 2014 - 2019 (inclusive)
    
    Output :-
    {year}.csv file containing: Incident Date, State, City/County, #killed, #injured
    
    The function takes in a year as input and returns a csv file that contains the above mentioned data from
    "www.gunviolencearchive.org" website.
    The data is specific to mass shootings throughout United States.
    
    To run this program, you need the following:
        1. selenium package to be installed.
        2. google chrome installed
        3. chromedriver path added to path variables.
    '''
    assert isinstance(year, int)
    assert year in range(2014, 2020)
    
    driver = webdriver.Chrome(options = chrome_options)
    driver.get(f"https://www.gunviolencearchive.org/reports/mass-shooting?year={year}")
    # https://www.gunviolencearchive.org/reports/officer-shot-killed?year={year}

    stuff = []
    x = True
    while x:
        #Scrape here    
        soup = BeautifulSoup(driver.page_source)
        links = soup.find_all('td')
        for link in links:
            if (type(link.contents[0]) == bs4.element.NavigableString):
                stuff.append(link.contents[0])
        #Scraping done
        try:
            element = driver.find_element_by_partial_link_text('next')
            element.click()
        except NoSuchElementException:
            x = False
            
    driver.close()
    
    #Stuff ready here. Write to CSV after using pandas
    df = pd.DataFrame(np.array(stuff).reshape(int((len(stuff))/6), 6), columns = ['Incident Date', 'State', 'City/County', 'Address', '# killed', '# injured'])
    df.to_csv(f'{year}.csv', encoding='utf-8', index=False)