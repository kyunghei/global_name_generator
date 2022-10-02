import requests
from bs4 import BeautifulSoup
import pandas as pd

# Scrape data of 1,000 korean names for forebears website and save as csv file
url = 'https://adoption.com/baby-names/origin/Irish?page='
for page in range(1,24):
    request = requests.get(url + str(page))

# Obtain page's information and change to python friendly format
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
    soup = BeautifulSoup(request.text, 'lxml')
    soup

# Find the location of the table in website using inspect
    name_table = soup.find('table')
    name_table

# Create a column list by inspecting the location of each column
    if page == 1:
        headers = []
        for header in name_table.find_all('th'):
            title = header.text
            headers.append(title)

# Dataframe is created using Pandas. Columns will be created for the first page to avoid header duplication
    mydata = pd.DataFrame(columns=headers)

    for elements in name_table.find_all('tr')[1:]:
        try:
            row_data = elements.find_all('td')
            row = [header.text for header in row_data]
            length = len(mydata)
            mydata.loc[length] = row
        except ValueError:
            # Exception handling for blank rows
            pass

# Export dataframe to csv file if scraping first page of web
    if page == 1:
        # Create a new csv for the first page data scrape and append the existing csv for the remaining web pages
        mydata.to_csv('irish_names.csv', index=False)
    else:
        # Append new dataframe to existing one
        mydata.to_csv('irish_names.csv', header=False, mode='a', index=False)


