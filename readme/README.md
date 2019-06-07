# **Analysis of Gun Violence throughout United States (Group 16)**
### Team Members
* Hao Mei
* Ke Li
* Li-Kuo Lin
* Sneh Shah

### Problem
To analyze the occurrences of different types of gun violence, mainly mass shootings, school shootings, and officer shootings, over a timeline to assess the situation.

### Summary
With the increasing amounts of gun violence incidents in the United States, we analyze the number of such incidents over a period of time. We mainly focus on incidents of mass shootings (casualties count atleast 4), school shootings, and officer shootings. We also look at the number of casualties, and some statewise distribution, and try to get a trend as how the frequency of these events has changed over the past few years.

### Data Set
To generate our data set, we scraped gunviolencearchive.org, everytownresearch.org, and wikipedia.org to get a list of all incidents of mass shootings, school shootings, and officer shootings throughout United States. The data set includes the date, city, state, number of casualties, and in case of school shootings, the type of school.

### Methodology
* The data is present in tabular form in the above stated websites. We scrape that data using Selenium and BeautifulSoup.
* We make a class of the scraped data and use functions defined in the class, such as get_total_incidents, count_casualties, and casualties_per_state to extract data.
* Using the extracted data, we generate different plots to analyze trends that these events follow over time, or in different states.

### Requirements
1. Python 3.7
2. selenium
3. chromedriver.exe (Chrome)
4. beautifulsoup
5. numpy
6. pandas
7. matplotlib
8. plotly

##### Browser automation using selenium
The scraping tools use selenium with chrome and beautifulsoup. To install selenium, use
`pip install selenium`
and download chromedriver.exe from
`https://sites.google.com/a/chromium.org/chromedriver/downloads`
The chromedriver.exe has to be added to the path variables. To do so, follow the steps given below:
1. Search for advanced system settings
2. Click on Environment Variables
3. Under System Variables, select path, and click edit
4. Click new, and add the path to chromedriver.exe

##### Install plotly to generate pie charts
To install plotly, use
`pip install plotly`

### Running the codes
To run the codes, run scrape_gva.py, scrape_etr.py, and scrape_wiki.py to generate the data sets. Run ......, etc. to generate the plots.








