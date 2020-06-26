from bs4 import BeautifulSoup as bs
import requests
import glob, os

download_link = 'https://www.statistics.gr:443/el/statistics?'

#returning html from the site
def get_soup(url):
    return bs(requests.get(url).text, 'html.parser')

#downloads all the excels from 2011 to 2014 that we use
def download_excel(url):
    for year in range(2011, 2015):
        name_id =str(year) + "-Q" + str(4) 
        new_url = str(url + name_id)
        bs(requests.get(new_url).text, 'html.parser')
        #searching into html for the link
        for link in get_soup(new_url).find_all('a'):
            excel_link = link.get('href')
            if download_link in excel_link:
                #the right link for the .xls file
                excel_link_checked = excel_link 

        with open(name_id + '.xls', 'wb') as excel:
            response = requests.get(excel_link_checked)
            excel.write(response.content)

#erases the excel files in the folder
def purge():
    for f in os.listdir():
        if f.endswith('.xls'):
            os.remove(f)




