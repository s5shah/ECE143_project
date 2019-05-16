from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--start-maximized")

def scrape_etr(year):
    '''
    Input :-
    year - type: int, range: 2013 - 2019 (inclusive)
    
    Output :-
    {year}.csv file containing: Date, City, State, School Name, School Type
    
    The function takes in a year as input and returns a csv file that contains the above mentioned data from
    "www.everytownresearch.org" website.
    The data is specific to gun violence incidents in schools throughout United States.
    
    To run this program, you need the following:
        1. selenium package to be installed.
        2. google chrome installed
        3. chromedriver path added to path variables.
    '''
    assert year in range(2013, 2020)
    
    driver = webdriver.Chrome(options = chrome_options)
    driver.get("https://everytownresearch.org/gunfire-in-school/")
    
    element = driver.find_element_by_css_selector(f".btn-year[data-year = '{year}']")
    element.click()
    
    #Scrape here
    